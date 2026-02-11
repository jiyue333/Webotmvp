# worker/

## 模块职责
异步任务消费层。通过 Redis Stream 消费者组拉取文档处理任务，调度 docparser + services 完成解析 → 分块 → 向量化 → 图谱抽取 → 状态回写的全流程。对标 WeKnora 的 Asynq Server + ProcessDocument 语义，替换为 Python + Redis Stream 实现。

## 边界
- **上游**：`services/knowledge_service.py` 在创建 knowledge 记录后通过 `queue.enqueue()` 投递任务。
- **下游**：调用 `docparser` 模块解析文档，调用 `services` 层完成分块/向量化/图谱抽取，调用 `repositories` 层写入数据库。
- **不做**：不对外暴露 HTTP 接口；不包含 API 路由或 Handler 逻辑。
- **不做**：不管理 Redis 连接（由 `infra/` 层提供连接实例）。

## 文件清单

| 文件                  | 职责                                                                                                           |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| `__init__.py`         | 包入口；统一导出 IngestionWorker、TaskQueue 等核心符号                                                         |
| `ingestion_worker.py` | 任务消费主循环（IngestionWorker 类）；从 Stream 拉取任务、路由到处理函数、ack 确认与 reclaim 崩溃恢复          |
| `queue.py`            | Redis Stream 队列封装（TaskQueue 类）；enqueue 接收 TaskEnvelope，dequeue 返回 ReceivedMessage                 |
| `tasks.py`            | TaskEnvelope 结构化信封 + TaskType 常量 + Payload 数据类；task_id 仅为 UUIDv7 唯一标识，元数据以 JSON 字段承载 |

## 数据结构分层

```
TaskEnvelope（业务层 — tasks.py 定义）
├── task_id: str          — UUIDv7 唯一标识
├── task_type: str        — "document:process"
├── user_id: str          — 提交任务的用户
├── created_at: datetime  — 创建时间
├── retry_count: int      — 当前重试次数
└── payload: dict         — 具体业务载荷（DocumentProcessPayload）

ReceivedMessage（传输层 — queue.py 定义）
├── stream_message_id: str  — Redis Stream 分配的 ID，用于 XACK
└── envelope: TaskEnvelope  — 反序列化后的任务信封
```

## 数据流（对标 mvp.md §3.2 文档入库流）

```
KnowledgeService.create_knowledge()
  │
  ├─ 同事务：写入 knowledge 记录 (parse_status = pending)
  │
  └─ 事务外：TaskQueue.enqueue(TaskEnvelope)
         │                          ↓ XADD (envelope → JSON)
         ▼
  Redis Stream ──► IngestionWorker.run_forever()
   (消费者组)          │
                     ├─ dequeue() → XREADGROUP → ReceivedMessage
                     │                            ├─ .stream_message_id
                     │                            └─ .envelope.task_type
                     │
                     ├─ 按 envelope.task_type 路由到处理函数
                     │
                     ├─ 状态更新：parse_status → processing
                     │
                     ├─ DocParser：解析 + OCR → 结构化文本块
                     │
                     ├─ ChunkService：分块 → chunks 表
                     │
                     ├─ EmbeddingClient：向量化 → embeddings 表
                     │
                     ├─ (M7) GraphService：实体/关系抽取 → Neo4j
                     │
                     ├─ 状态更新：parse_status → completed / failed
                     │
                     └─ TaskQueue.ack(stream_message_id) → XACK 确认
```

## 设计决策
1. **Redis Stream 消费者组**：使用 XREADGROUP + XACK 实现可靠消费。Worker 崩溃后，未 ack 的消息留在 pending 列表，其他 Worker 通过 XCLAIM 自动回收，不丢任务。
2. **支持水平扩展**：同一消费者组内的多个 Worker 实例自动分配消息，互不重复消费。MVP 阶段默认单 Worker，但架构支持 `docker compose up --scale worker=N`。
3. **补偿模式保底**：knowledge 创建与 Redis 投递不在同一事务内。除了 Stream pending 回收外，Worker 仍可定期扫描 `parse_status = 'pending'` 超时记录作为兜底补偿（对齐 mvp.md §4.6）。
4. **任务类型路由**：参考 WeKnora `RunAsynqServer()` 的 `mux.HandleFunc(type, handler)` 模式，在 `ingestion_worker.py` 中按 `envelope.task_type` 路由到对应的 service 方法。
5. **结构化信封替代字符串拼接**：task_id 为纯 UUIDv7，所有元数据（task_type / user_id / retry_count）以 TaskEnvelope JSON 字段承载，避免分隔符解析的隐性 bug。

# WeKnora 知识库 Chatbot MVP 项目文档（Python 复现版）

## 0. 文档基线与约束

### 0.1 对齐原则（严格）
- 本文档仅基于 WeKnora 现有能力做 **删减、合并、语言迁移（Go -> Python）**。
- 不新增业务域，不扩展原项目没有的产品能力。
- 允许替换实现中间件（例如 Go Asynq -> Python Redis Worker），但语义与流程保持一致。

### 0.2 参考基线（仓库内）
- 架构与分层：`docs/system-architecture.md`、`internal/container/container.go`
- RAG 流程：`docs/WeKnora.md`、`internal/application/service/chat_pipline/README.md`
- 路由与接口：`docs/api/*.md`、`internal/router/router.go`
- 模型管理：`docs/api/model.md`、`docs/BUILTIN_MODELS.md`
- 鉴权：`internal/middleware/auth.go`、`internal/router/router.go`（auth routes）
- 数据模型：`docs/database-architecture.md`、`migrations/versioned/*.sql`
- 流式与事件：`internal/event/event.go`、`internal/stream/factory.go`、`internal/handler/session/stream.go`
- 知识图谱：`docs/KnowledgeGraph.md`、`docs/开启知识图谱功能.md`、`internal/application/service/chat_pipline/extract_entity.go`、`internal/application/service/chat_pipline/search_entity.go`、`internal/application/repository/retriever/neo4j/repository.go`
- 文档解析/OCR：`docreader/README.md`、`docreader/parser/*.py`
- 部署：`docker-compose.yml`、`docs/开发指南.md`、`docs/QA.md`

---

## 1. 背景与目标（Why）

### 1.1 复现动机
- 累积生产级后端经验：本地 Docker 部署、运行维护、故障定位、数据迁移。
- 掌握 WeKnora 亮点：知识库管理、混合检索、图谱增强检索、SSE 对话。
- 训练工程能力：分层架构、事件驱动流水线、可观测性、配置治理。

### 1.2 MVP Goals（必须完成）
- 多用户体系：注册/登录/刷新/登出，JWT 鉴权与 token 持久化。
- 模型管理链路：支持多厂商 provider 类型，支持模型 CRUD 与 provider 列表能力。
- 知识库主链路：KB 管理、知识导入（file/url/manual）、解析状态追踪。
- 文档理解链路：参考 DocReader 实现并内嵌到单服务，包含 OCR。
- 检索链路：关键词 + 向量混合检索，支持重排。
- 知识图谱链路：实体/关系抽取、Neo4j 存储、对话阶段图谱检索增强。
- 对话链路：Session/Message + `knowledge-chat` SSE 流式输出 + 引用返回，首版保留“继续流式输出/停止会话”。
- 本地 Docker 一键运行，具备日志/指标/追踪。

### 1.3 Non-goals（明确不做）
- 不做 Agent 模式（ReAct、工具注册、反思步骤）。
- 不做多租户（仅单工作空间），但保留多用户。
- 不做 MCP 能力。
- 不做多向量后端适配（仅一个后端，见 2.3 解释）。
- 不做多机集群和 K8s，仅本地 Docker。

---

## 2. 范围与对标（Scope & Parity）

### 2.1 模块对标表（WeKnora -> MVP）
| 模块 | WeKnora 参考 | MVP 保留 | 简化说明 |
|---|---|---|---|
| 用户与鉴权 | `internal/router/router.go` auth routes, `internal/middleware/auth.go` | 保留 | 去掉租户切换，仅多用户 JWT |
| 模型管理 | `docs/api/model.md`, `internal/router/router.go` | 保留 | 保留 provider 列表与模型 CRUD |
| 知识库管理 | `docs/api/knowledge-base.md` | 保留 | 保留核心 CRUD |
| 知识管理 | `docs/api/knowledge.md`, `internal/application/service/knowledge.go` | 保留 | 保留 file/url/manual；删除与 Agent 绑定字段 |
| 文档解析 | `docreader/parser/*.py` | 保留 | 不再 gRPC 分服务，按 docreader 思路内置实现 |
| OCR | `docreader/README.md` | 保留 | 具体后端实现遵循 docreader 方案，不在 MVP 文档固化 |
| RAG Pipeline | `internal/application/service/chat_pipline/*` | 保留 | 仅 Chat 模式，移除 Agent 相关事件 |
| 混合检索 | `search.go`, `rerank.go`, `merge.go` | 保留 | 向量后端固定单一实现 |
| 知识图谱 | `extract_entity.go`, `search_entity.go`, `neo4j/repository.go` | 保留 | 仅 Neo4j，一条图谱实现 |
| 会话与消息 | `docs/api/session.md`, `docs/api/message.md` | 保留 | 保留 continue-stream / stop 能力 |
| SSE 流 | `internal/handler/session/stream.go`, `internal/stream/*` | 保留 | 使用 Redis StreamManager |
| 异步任务 | `Asynq` 路径（container/router/task） | 保留语义 | Python Worker + Redis Queue |
| 可观测性 | tracing/logger/middleware | 保留 | 采用 Python OTel/日志栈 |

### 2.2 MVP 包含 / 不包含
| 分类 | 包含 | 不包含 |
|---|---|---|
| 核心功能 | 多用户 JWT、模型管理、知识库、检索、图谱、对话、continue-stream/stop | Agent、MCP、租户 |
| FAQ | 首版不纳入 | 可作为后续增量 |
| 存储 | PostgreSQL + pgvector + pg_search(使用paradeDb镜像即可)、Redis、Neo4j、MinIO/本地 | Qdrant、Elasticsearch 多适配 |
| 部署 | Docker Compose 本地部署 | K8s/Helm、多节点 |
| 前端 | 使用 Vue 重新实现（仅覆盖 MVP 接口） | 无需要参考原项目风格 |

### 2.3 关键术语说明（对应你提出的问题）
- “不做多向量后端适配（仅一个后端）”的含义：
  - WeKnora 支持 PostgreSQL / Qdrant / Elasticsearch 等多检索后端切换。
  - MVP 只选 **PostgreSQL + pgvector + pg_search** 这一套，不做多后端抽象适配与切换。
- `Ingestion Worker` 的含义：
  - 指“知识导入后台处理进程”，消费 Redis 队列中的导入任务，执行：解析 -> OCR -> 分块 -> 向量化 -> 图谱抽取 -> 入库。
  - 对标 WeKnora 的异步任务处理语义（Asynq Server + ProcessDocument）。

---

## 3. 系统架构（High-level Design）

### 3.1 架构图（对齐 WeKnora 架构风格，按 MVP 子集裁剪）
```mermaid
flowchart TB
    subgraph External_Left["外部服务 - AI 模型"]
        direction LR
        LLM["Chat LLM"]
        EMB["Embedding Model"]
        RRK["Rerank Model"]
        OCR["OCR Service"]
    end

    subgraph Core["MVP 核心服务（Python Monolith）"]
        direction TB

        subgraph Client["客户端层"]
            direction TB
            FE["Frontend"]
            APIU["API Users / SDK"]
        end

        subgraph Gateway["接入层"]
            direction TB
            ROUTER["FastAPI Router /api/v1"]
            MW["Middleware: JWT/Auth, Logger, Trace, Error"]
        end

        subgraph Handler["Handler 层"]
            direction TB 
            H_AUTH["Auth"]
            H_KB["KnowledgeBase"]
            H_KNOW["Knowledge"]
            H_SESS["Session"]
            H_CHAT["Chat"]
            H_MSG["Message"]
            H_MODEL["Model"]
        end

        subgraph Service["业务服务层"]
            subgraph service1["service1"]
                direction TB
                S_USER["UserService"]
                S_AUTH["AuthService"]
                S_KB["KBService"]
                S_KNOW["KnowledgeService"] 
            end
            subgraph service2["service2"]
                direction TB
                S_CHUNK["ChunkService"]
                S_SESS["SessionService"]
                S_RET["RetrieverService"]
                S_GRAPH["GraphService"] 
            end
        end

        subgraph Engine["核心引擎"]
            direction TB
            PIPE["Chat Pipeline<br/>LoadHistory → Rewrite → ExtractEntity → SearchParallel<br/>→ Rerank → Merge → FilterTopK → IntoChatMessage → ChatCompletionStream"]
            DOC["DocReader模块(内嵌实现)<br/>Parser + OCR"]
            EVT["EventBus"]
            STREAM["StreamManager(Redis)"]
            CTX["ContextManager(Redis)"]
        end

        subgraph Repository["数据访问层"]
            direction TB
            REPO["User/AuthToken/KB/Knowledge/Chunk/Embedding/Session/Message/Model"]
            GREPO["GraphRepository(Neo4j)"]
        end

        subgraph Async["异步处理"]
            direction LR
            QUEUE["Redis Queue"]
            WORKER["Ingestion Worker"]
        end
    end

    subgraph External_Right["外部服务 - 数据存储"]
        direction LR
        PG[("PostgreSQL </br> + pgvector </br> + pg_search")]
        REDIS[("Redis")]
        NEO4J[("Neo4j")]
        MINIO[("MinIO </br> Local Storage")]
    end

    Client --> Gateway
    Gateway --> Handler
    Handler --> Service
    Service --> Engine
    Service --> Repository
    Engine --> Repository
    Async --> Engine
    Async --> Repository
```

### 3.2 关键数据流

#### 文档入库流（异步）
1. 上传知识（file/url/manual）创建 `knowledge` 记录，状态 `pending`。
2. 投递 Redis 队列任务。
3. Worker 消费任务，执行内嵌解析模块（参考 docreader）：解析 + OCR。
4. 分块、向量化写入 `chunks/embeddings`。
5. 若开启图谱抽取，写入 Neo4j。
6. 更新 `parse_status` 为 `completed/failed`。

#### 对话流（同步 + SSE）
1. `knowledge-chat/{session_id}` 接收查询，落库 user/assistant 占位消息。
2. 触发 Pipeline：历史加载、重写、实体抽取、并行检索（chunk + entity graph）。
3. 结果重排、合并、TopK、组装 Prompt。
4. 流式调用 LLM，SSE 推送 answer/references。
5. 完成后更新 assistant 消息内容与状态。

### 3.3 模块职责（输入/输出/边界）
| 模块 | 输入 | 输出 | 边界 |
|---|---|---|---|
| Router/Handler | HTTP 请求 | JSON/SSE | 不写复杂业务逻辑 |
| Service | DTO + 上下文 | 领域结果 | 编排事务、状态流转 |
| Pipeline | query/session/config | 检索结果 + 生成文本流 | 只负责 RAG 编排 |
| DocReader(内置) | 文件/URL/配置 | 结构化文本块 + OCR结果 | 不感知 HTTP |
| Repository | 查询条件 | 持久化对象 | 不含策略逻辑 |
| Worker | Redis任务 | 处理结果与状态更新 | 不直接对外暴露 API |

### 3.4 技术栈与版本
| 类别 | 选型 |
|---|---|
| 语言 | Python 3.11 |
| Web | FastAPI + Uvicorn |
| ORM | SQLAlchemy 2.x |
| 迁移 | Alembic |
| 主库 | PostgreSQL 16 + pgvector + pg_search(使用paradeDb镜像即可) |
| 缓存/队列 | Redis |
| 图数据库 | Neo4j |
| 对象存储 | MinIO / 本地文件 |
| 可观测 | OpenTelemetry + Prometheus + JSON Logging |
| 部署 | Docker Compose |

---

## 4. 数据与接口设计（Data & API）

### 4.1 鉴权与用户模型
- 模式：多用户 JWT（Access + Refresh）。
- Token 持久化：`auth_tokens` 表，支持撤销与刷新。
- 不支持多租户：去除 `tenant_id` 业务隔离逻辑。
- 参考：`internal/middleware/auth.go`、`internal/router/router.go`（auth routes）、`docs/database-architecture.md` 的 `users/auth_tokens`。

### 4.2 API 设计（语义对齐 WeKnora，路径不要求兼容）
基础路径建议：`/api/v1`（可按项目约定调整）

| 分类 | 方法 | 路径 | 对齐来源 |
|---|---|---|---|
| Auth | POST | `/auth/register` | `router.go` |
| Auth | POST | `/auth/login` | `router.go` |
| Auth | POST | `/auth/refresh` | `router.go` |
| Auth | POST | `/auth/logout` | `router.go` |
| Auth | GET | `/auth/me` | `router.go` |
| Model | GET | `/models/providers` | `docs/api/model.md` |
| Model | POST/GET/GET/PUT/DELETE | `/models` / `/{id}` | `docs/api/model.md` |
| KB | POST/GET/GET/PUT/DELETE | `/knowledge-bases` / `/{id}` | `docs/api/knowledge-base.md` |
| Knowledge | POST | `/knowledge-bases/{id}/knowledge/file` | `docs/api/knowledge.md` |
| Knowledge | POST | `/knowledge-bases/{id}/knowledge/url` | `docs/api/knowledge.md` |
| Knowledge | POST | `/knowledge-bases/{id}/knowledge/manual` | `docs/api/knowledge.md` |
| Knowledge | GET | `/knowledge-bases/{id}/knowledge` | `docs/api/knowledge.md` |
| Knowledge | GET/DELETE | `/knowledge/{id}` | `docs/api/knowledge.md` |
| Session | POST/GET/GET/PUT/DELETE | `/sessions` / `/{id}` | `docs/api/session.md` |
| Session | POST | `/sessions/{session_id}/stop` | `docs/api/session.md` |
| Session | GET | `/sessions/continue-stream/{session_id}` | `docs/api/session.md` |
| Message | GET | `/messages/{session_id}/load` | `docs/api/message.md` |
| Chat | POST | `/knowledge-chat/{session_id}` | `docs/api/chat.md` |
| Search | POST | `/knowledge-search` | `docs/api/chat.md` + `router.go` |

### 4.3 请求/响应与错误码规范
- 成功：
```json
{"success": true, "data": {}, "request_id": "req_xxx"}
```
- 失败：
```json
{"success": false, "error": {"code": 1000, "message": "bad request", "details": {}}}
```
- SSE（对齐 WeKnora）：
```json
{"id":"msg_xxx","response_type":"references|answer|error","content":"...","done":false,"knowledge_references":[]}
```
- 错误码风格对齐：`internal/errors/errors.go`。

### 4.4 幂等策略（MVP）
- 不新增独立幂等子系统（避免超出 WeKnora 能力域）。
- 写操作防重采用 WeKnora 现有语义：
  - 文件导入：`file_hash` 去重（`knowledge` 层）。
  - 请求追踪：`X-Request-ID`。
- 说明：如果后续需要“严格幂等键”，作为后续增强，不纳入本 MVP。

### 4.5 数据模型（单租户多用户版）

#### 4.5.1 关系图（MVP）
```mermaid
erDiagram
    users ||--o{ auth_tokens : has
    users ||--o{ sessions : owns
    users ||--o{ knowledge_bases : creates

    knowledge_bases ||--o{ knowledges : contains
    knowledge_bases ||--o{ knowledge_tags : categorizes
    knowledges ||--o{ chunks : splits
    chunks ||--|| embeddings : embeds

    sessions ||--o{ messages : contains
    knowledge_bases ||--o| sessions : binds
```

#### 4.5.2 关键表（来源于 WeKnora 并裁剪）
- `users`
- `auth_tokens`
- `models`
- `knowledge_bases`
- `knowledge_tags`
- `knowledges`
- `chunks`
- `embeddings`
- `sessions`
- `messages`

说明：
- 以上均可在 `docs/database-architecture.md` 与 `migrations/versioned/*.sql` 找到对应原型。
- 裁剪点：去掉 `tenant_id` 主隔离逻辑，改为 `created_by/owner_id`（用户归属）。

### 4.6 数据一致性策略
- 事务边界：
  - 创建知识时，`knowledge` 记录与任务投递（Redis）要么都成功，要么回滚。
  - 消息创建（user + assistant 占位）同事务。
- 最终一致：
  - 导入任务异步执行，状态机：`pending -> processing -> completed/failed`。
- 删除策略：
  - 软删除优先，异步清理 `chunks/embeddings/neo4j` 关联数据。

### 4.7 数据迁移
- 工具：Alembic（对齐 WeKnora 的版本化迁移思路）。
- 流程：
  - 开发：`alembic revision --autogenerate -m "..."`
  - 发布：`alembic upgrade head`
  - 回滚：`alembic downgrade -1`
- 对标参考：`internal/database/migration.go`、`scripts/migrate.sh`、`migrations/versioned/*`。

---

## 5. 其他生产级能力（可观测性/部署/流水线/日志）

### 5.1 可观测性
- 日志：结构化 JSON，字段至少包含 `request_id/session_id/user_id/kb_id/latency/error_code`。
- 指标：
  - HTTP：QPS、状态码、时延
  - 导入：任务耗时、成功率、重试次数
  - 检索：召回耗时、重排耗时
  - 对话：首 token、总生成耗时
- 追踪：覆盖 ingest、retrieve、graph_search、chat_generate。
- 对标参考：`middleware/logger.go`、`middleware/trace.go`、`internal/tracing/*`。

### 5.2 部署（本地 Docker）
- 必选服务：`app`, `postgres`, `redis`, `neo4j`。
- 可选服务：`minio`（启用对象存储时）。
- 对标参考：`docker-compose.yml`（neo4j/profile/redis/minio）。

### 5.3 运行维护（Runbook）
- 启动：`docker compose up -d`
- 检查：`docker compose ps`
- 日志：`docker compose logs -f app`
- 健康：`GET /health`
- 图谱验证：Neo4j 执行 `MATCH (n) RETURN n LIMIT 50;`
- 参考：`docs/QA.md`、`docs/开启知识图谱功能.md`。

### 5.4 CI（MVP 最小集）
- `ruff + mypy + pytest`
- `alembic upgrade head` 校验
- API smoke test（登录、导入、检索、对话）

---

## 6. 里程碑与计划（Plan）

### 6.1 分阶段计划（6 周，前后端并行）

> 采用垂直切片策略，每周交付可演示的功能切片，前后端同步推进。

#### Week 1: 基础骨架与用户体系

| 端 | 交付 |
|---|---|
| **后端** | 分层架构骨架、JWT 鉴权 (5 API)、KB CRUD (5 API)、Alembic 迁移、Docker Compose |
| **前端** | Vue 3 + Vite + TS 骨架、路由/状态管理、HTTP 封装、登录/注册页面 |
| **集成** | 前端可调用 Auth API、Token 自动刷新 |

#### Week 2: 模型管理 + 知识导入基础

| 端 | 交付 |
|---|---|
| **后端** | Model Provider 列表、Model CRUD (6 API)、Knowledge 导入 API (file/url/manual)、Redis Queue、Worker 骨架 |
| **前端** | 知识库列表/详情页、模型管理页、知识导入表单 |
| **集成** | 可创建模型、可上传文件并看到 pending 状态 |

#### Week 3: 文档解析 + 向量化

| 端 | 交付 |
|---|---|
| **后端** | DocReader 内嵌实现 (PDF/DOCX/TXT/MD)、OCR 集成（可选）、Chunking 分块、Embedding 向量化、pgvector 存储 |
| **前端** | 知识详情页（解析状态、chunk 预览）、解析进度展示 |
| **集成** | 文件上传 → 解析 → 分块 → 向量化 全流程可验证 |

#### Week 4: 检索 + 知识图谱 + 会话

| 端 | 交付 |
|---|---|
| **后端** | 混合检索（pgvector + pg_search BM25 + Rerank）、实体/关系抽取、Neo4j 存储与检索、Session/Message CRUD |
| **前端** | 会话列表页、对话界面骨架（非 SSE） |
| **集成** | `/knowledge-search` 返回检索结果、Neo4j 可查询 |

#### Week 5: SSE 对话 + 前端完善

| 端 | 交付 |
|---|---|
| **后端** | Chat Pipeline 完整实现、SSE 流式输出、continue-stream/stop、引用返回 |
| **前端** | SSE 对话实现、流式消息渲染、引用卡片、继续/停止按钮 |
| **集成** | 完整对话流程 E2E、引用正确展示、可中断对话 |

#### Week 6: 生产化收口

| 端 | 交付 |
|---|---|
| **后端** | 可观测性（日志/指标/追踪）、错误处理优化、限流（可选）、API 文档 |
| **前端** | UI/UX 优化、响应式适配、错误提示优化 |
| **质量** | pytest 覆盖率 > 80%、E2E 测试、故障演练 |
| **文档** | 部署文档、API 文档、运维手册 |

### 6.2 里程碑检查点

| 里程碑 | 周 | 验收标准 |
|---|---|---|
| M1 | Week 1 | 前端登录 → 获取用户信息 |
| M2 | Week 2 | 上传文件 → 任务入队 |
| M3 | Week 3 | 向量写入 → 检索返回结果 |
| M4 | Week 4 | 实体抽取 → Neo4j 可视化 |
| M5 | Week 5 | SSE 流式问答 + 引用 |
| M6 | Week 6 | E2E 测试通过 + 文档齐全 |

### 6.3 每阶段交付要求

- **代码**：功能可运行、可回归
- **测试**：新增功能有单元测试
- **文档**：接口/配置/运维手册同步更新
- **集成**：前后端联调验收通过

### 6.4 风险清单与缓解

| 风险 | 影响 | 概率 | 缓解 |
|---|---|---|---|
| OCR 集成复杂 | Week 3 延期 | 中 | 首版可选跳过 OCR |
| 图谱抽取质量差 | Week 4 延期 | 中 | 设置开关，可仅用向量检索 |
| SSE 前端实现难 | Week 5 延期 | 低 | 参考成熟库 (EventSource) |
| 模型 API 不稳定 | 对话失败 | 中 | 超时 + 重试 + fallback |
| 前后端进度不匹配 | 集成困难 | 中 | 每周联调验收 |
| Redis 队列堆积 | 导入延迟 | 低 | 控制 worker 并发、指数退避 |

### 6.5 前端技术栈

| 类别 | 选型 |
|---|---|
| 框架 | Vue 3 |
| 构建 | Vite |
| 语言 | TypeScript |
| 路由 | vue-router |
| 状态 | Pinia |
| HTTP | axios |
| UI | TailwindCSS / Element Plus |
| SSE | EventSource API |

---

## 7. 已确认项

### 7.1 确认决策
- 单工作空间（无租户隔离），但允许多用户并发使用。
- 模型能力需支持多厂商 provider 类型（对齐 WeKnora model provider 设计）。
- 主检索后端固定为 PostgreSQL + pgvector + pg_search(使用paradeDb镜像即可)。
- 图谱后端固定为 Neo4j。
- 文档解析能力参考 docreader 实现，不再走 gRPC，内嵌于同一服务。
- Redis 可用且用于队列、流式事件、上下文缓存。
- FAQ 首版不纳入，作为后续可选增量。
- 首版保留“继续流式输出 / 停止会话”能力。
- API 路径不要求兼容 WeKnora 原路径，仅语义对齐。
- 前端不复现原项目，使用 Vue 重新实现。
- OCR 具体后端实现由开发时按 docreader 方案确定，不在本文档强绑定。

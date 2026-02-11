# services/

## 职责

业务服务层，承载核心业务编排职责。上游由 `api/handler` 和 `worker` 调用，下游依赖 `repository`（数据访问）和外部客户端（AI 模型/Redis/Neo4j）。

## 边界

- **只负责业务编排与流程控制**，不直接处理 HTTP 协议（由 api 层负责）。
- **不包含持久化逻辑**，数据读写委托给 repository 层。
- **不包含基础设施初始化**，连接池/客户端实例由 infra 层提供并通过依赖注入传入。

## 文件清单

| 文件                        | 职责                                              | 对标 WeKnora                   | 所属里程碑 |
| --------------------------- | ------------------------------------------------- | ------------------------------ | ---------- |
| `__init__.py`               | 包入口，导出各 Service 类                         | —                              | M2+        |
| `auth_service.py`           | 注册/登录/JWT 令牌生成/刷新/撤销                  | `user.go`（auth 部分）         | M2         |
| `user_service.py`           | 用户信息 CRUD、密码修改                           | `user.go`（user 部分）         | M2         |
| `model_service.py`          | 模型 CRUD、provider 列表、模型实例工厂            | `model.go`                     | M3         |
| `knowledge_base_service.py` | 知识库 CRUD、分块配置管理、级联删除               | `knowledgebase.go`             | M3         |
| `knowledge_service.py`      | 知识导入(file/url/manual)、状态流转、异步任务投递 | `knowledge.go`                 | M3         |
| `knowledge_tag_service.py`  | 标签 CRUD、唯一校验、删除时清理引用               | `tag.go`                       | M3         |
| `chunk_service.py`          | 分块 CRUD、批量操作、按知识维度清理               | `chunk.go`                     | M5         |
| `embedding_service.py`      | 向量生成与写入/删除生命周期管理                   | `hybrid_indexer`(Index/Delete) | M5         |
| `session_service.py`        | 会话 CRUD、级联删除、自动标题生成                 | `session.go`（lifecycle）      | M4         |
| `message_service.py`        | 消息 CRUD、历史加载（before_id 分页）             | `message.go`                   | M4         |
| `chat_service.py`           | 知识对话编排入口、SSE 流控、stop/continue         | `session.go`（KnowledgeQA）    | M4         |
| `graph_service.py`          | 实体抽取、Neo4j 图写入/检索、图谱开关             | `graph.go`                     | M7         |
| `chat_pipeline/`            | RAG Pipeline 各步骤插件（已调整，跳过）           | `chat_pipline/`                | M4-M7      |
| `retriever/`                | 混合检索服务（已调整，跳过）                      | `retriever/`                   | M6         |

## 设计说明

### 与 WeKnora 的关键差异

1. **AuthService vs UserService 分离**：WeKnora 的 `user.go` 同时包含认证和用户管理。MVP 将认证流程（JWT/token）独立为 `auth_service.py`，用户基本信息管理保留在 `user_service.py`，职责更清晰。

2. **ChatService 独立**：WeKnora 的 `session.go` 同时包含会话管理和 KnowledgeQA 编排。MVP 将 RAG 编排独立为 `chat_service.py`，`session_service.py` 仅负责会话生命周期。

3. **去除 Tenant/Agent/MCP 相关服务**：MVP 不含多租户、Agent、MCP，因此不需要 `tenant.go`、`agent_service.go`、`mcp_service.go`、`custom_agent.go` 等对标文件。

4. **KnowledgeBaseService → KnowledgeService 单向依赖**：`KnowledgeBaseService` 级联删除时依赖 `KnowledgeService`（写操作走 Service 层，保证 Knowledge 删除逻辑只维护一处）。`KnowledgeService` 对 KB 的只读需求（校验存在性、读取 chunking_config）降级到 `KnowledgeBaseRepository`，**不依赖 KnowledgeBaseService**，避免循环依赖。

## 协作关系

```
api/handler → services → repository
                ↓
            chat_pipeline → retriever
                ↓
            infra（Redis/Neo4j/AI 模型客户端）
```

- `api` 层调用 Service 的公共方法
- `worker` 层调用 KnowledgeService（状态回写）和 ChunkService（分块写入）
- `ChatService` 编排 `ChatPipeline`，Pipeline 内部调用 `RetrieverService` 和 `GraphService`

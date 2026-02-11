# app/

## 模块职责
MVP 核心服务根包（Python Monolith）。按分层架构组织所有后端代码：接入层 → 业务层 → 引擎层 → 数据层 → 基础设施层。对标 WeKnora `internal/` 目录结构，从 Go 迁移到 Python/FastAPI。

## 边界
- 只提供文档化约束与协作说明；上游供研发阅读，下游不作为运行时行为来源。
- 模块间调用方向遵循分层依赖：`api → services → repositories / engine`，禁止反向依赖。

## 模块划分

### 接入层
- `api/`：HTTP 路由注册、参数校验、依赖注入（Router + Handler）。
- `middleware/`：鉴权（JWT）、日志、追踪、异常恢复中间件。
- `schemas/`：请求/响应 DTO（Pydantic 模型）。

### 业务层
- `services/`：业务编排层（状态流转、跨仓储聚合、事务管理）。
- `common/`：公共定义（错误码、自定义异常、统一响应壳、分页）。

### 引擎层
- `docparser/`：文档解析引擎（Parser + OCR），内嵌实现，不走 gRPC。
- `stream/`：流式事件管理（Redis StreamManager），支持 SSE 推送与续流。
- `event/`：事件总线（EventBus + EventType），供 chat_pipeline / worker 使用。
- `context/`：对话上下文管理（Redis ContextManager），缓存会话状态。
- `client/`：外部模型调用客户端（LLM / Embedding / Rerank / OCR）。

### 数据层
- `repositories/`：数据访问层（PostgreSQL + Neo4j），含 ORM 模型与检索器。

### 基础设施层
- `infra/`：连接管理（DB / Redis / Neo4j / Storage 连接工厂）。

### 异步处理
- `worker/`：异步任务消费（Redis Stream 消费者组 + Ingestion Worker），执行文档入库全流程。

### 工具
- `utils/`：通用工具函数（ID 生成、时间格式化、哈希计算等）。

### 入口文件
- `main.py`：FastAPI 应用入口，注册路由与中间件，启动 Uvicorn。
- `container.py`：依赖注入容器，装配 service / repository / infra 实例。


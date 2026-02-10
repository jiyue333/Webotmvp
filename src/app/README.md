# app/

## 文件夹职责
- `api/`: HTTP 接口层（路由与入参校验）
- `common/`: 全局配置与通用工具（常量、安全、异常、日志定义）
- `middleware/`: 请求中间件（鉴权、日志、追踪、异常恢复）
- `infra/`: 外部基础设施连接（DB、Redis、Neo4j、对象存储）
- `docparser/`: 文档解析与 OCR 相关逻辑
- `schemas/`: 请求/响应 DTO 与数据校验模型
- `repositories/`: 数据访问层（含 `models/` 与 retriever 持久化实现）
- `services/`: 业务编排层（含 `chat_pipeline/`、`context/`、`retriever/`）
- `event/`: 事件总线与事件定义
- `stream/`: 流式事件管理
- `worker/`: 异步任务消费与导入处理
- `client/`: AI 模型调用客户端（LLM/Embedding/Rerank）
- `utils/`: 通用工具

## TODO
- M2: 完成 auth 路由与服务层
- M3: 完成模型/知识库/知识管理接口
- M4+: 完成会话、SSE、检索流水线接入

# app/

## 文件职责
- 定义后端应用的分层结构与模块边界。
- 约束 API、Service、Repository、Infra、Worker 的职责归属。

## 边界
- 仅定义分层职责，不在该文档中描述具体业务实现细节。
- 所有跨层调用必须通过明确接口，避免跨层直接耦合。

## 模块划分
- `api/`：HTTP 接入层（路由、参数校验、依赖注入）。
- `services/`：业务编排层（状态流转、跨仓储聚合）。
- `repositories/`：数据访问层（数据库与检索存储）。
- `infra/`：连接管理层（DB/Redis/Neo4j/Storage）。
- `worker/`：异步任务消费与 ingest 执行。
- `schemas/`：请求/响应 DTO。
- `middleware/`：鉴权、日志、追踪、异常恢复。

## TODO
- [arch][P1][todo] 在 M1 为每个子目录补齐 README 与文件头约束。
- [auth][P1][todo] 在 M2 完成认证链路与中间件闭环。
- [chat][P1][todo] 在 M4 完成会话消息与 SSE 对话主链路。

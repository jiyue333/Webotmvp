# app/

## 文件职责
- 维护 `src/app/README.md` 的模块职责与协作边界。

## 边界
- 只提供文档化约束与协作说明；上游供研发阅读，下游不作为运行时行为来源。

## 模块划分
- `api/`：HTTP 接入层（路由、参数校验、依赖注入）。
- `client/`：外部模型调用层（LLM/Embedding/Rerank/OCR 客户端封装）。
- `services/`：业务编排层（状态流转、跨仓储聚合）。
- `repositories/`：数据访问层（数据库与检索存储）。
- `infra/`：连接管理层（DB/Redis/Neo4j/Storage）。
- `worker/`：异步任务消费与 ingest 执行。
- `schemas/`：请求/响应 DTO。
- `middleware/`：鉴权、日志、追踪、异常恢复。

## TODO
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/README.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/README.md`。


## 协作矩阵
| 协作单元     | 输入依赖           | 输出产物         | 并行边界                     | 主要阻塞点          |
| ------------ | ------------------ | ---------------- | ---------------------------- | ------------------- |
| api          | router/deps/schema | HTTP 协议与响应  | 可与 ui 并行                 | service 契约未稳定  |
| services     | api/worker 调用    | 业务编排结果     | 可与 repository 并行定义接口 | repository 能力缺口 |
| repositories | services 查询需求  | 持久化访问接口   | 可与 infra 并行              | 数据模型与索引未定  |
| infra        | config/compose     | 连接与资源实例   | 可独立推进                   | 外部服务参数变化    |
| worker       | queue/service      | 异步任务执行结果 | 可与 api 并行                | ingest 链路未齐全   |
| ui           | api 契约           | 页面与交互状态   | 可与后端并行联调             | API 字段不稳定      |

# 架构说明（M1）

## 文件职责
- 说明 MVP 当前结构分层与组件边界。
- 提供后续 M2-M8 的扩展锚点。

## 边界
- 本文档描述的是 M1 骨架，不包含完整业务实现细节。
- 不覆盖 Agent、MCP、多租户与多向量后端适配。

## 分层结构
- `api`：路由与输入输出契约。
- `services`：业务编排与状态流转。
- `repositories`：持久化读写。
- `infra`：数据库/缓存/图谱/存储连接。
- `worker`：异步任务消费与 ingest 链路。

## 关键链路
1. 健康检查链路：`/health` 与 `/api/v1/health`。
2. 文档入库链路（M5 目标）：上传 -> 队列 -> 解析/OCR -> 分块 -> 向量化。
3. 对话链路（M4-M7 目标）：会话 -> 检索/图谱 -> SSE 输出。

## TODO
- [arch][P1][todo] 在 M1 输出 Router/Service/Repository 依赖关系图。
- [retrieval][P2][todo] 在 M6 增加混合检索与重排数据流图。
- [graph][P2][todo] 在 M7 增加图谱增强与降级路径图。

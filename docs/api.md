# API 约定（M1）

## 文件职责
- 说明当前可用 API 与后续阶段接口规划。
- 统一响应格式与错误处理约定。

## 边界
- 本文档只定义 MVP 语义对齐，不保证与原项目路径完全兼容。
- M1 仅承诺健康检查接口稳定，其余接口为阶段占位。

## 当前可用接口
- `GET /health`
- `GET /api/v1/health`

## 规划接口（按阶段）
- M2：`/auth/register` `/auth/login` `/auth/refresh` `/auth/logout` `/auth/me`
- M3：`/models`、`/knowledge-bases`、`/knowledge`
- M4：`/sessions`、`/messages`、`/knowledge-chat/{session_id}`

## 响应约定
- 建议成功响应：`{"success": true, "data": ..., "request_id": "..."}`
- 建议失败响应：`{"success": false, "error": {"code": ..., "message": ...}}`

## TODO
- [arch][P1][todo] 在 M1 固化 API 路由挂载清单并与 `src/app/api` 保持一致。
- [auth][P1][todo] 在 M2 完成认证接口契约与错误码文档。
- [chat][P1][todo] 在 M4 增加 SSE 事件字段与终止语义说明。

# API 约定（M1）

## 文件职责
- 维护 `api.md` 文档的事实约束，向协作方说明当前实现边界与演进路径。

## 边界
- 只提供文档化约束与协作说明；上游供研发阅读，下游不作为运行时行为来源。

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
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`docs/api.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`docs/api.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`docs/api.md`。

# services/chat_pipeline/

## 文件职责
- 承载 chat pipeline 的 `README.md` 步骤职责，明确该步骤输入输出契约。

## 边界
- 只负责业务编排与流程控制；上游由 api/worker 调用，下游依赖 repository/client，不直接处理 HTTP 协议。

## 目标步骤
1. `load_history`
2. `rewrite`
3. `extract_entity`
4. `search_parallel`
5. `rerank`
6. `merge`
7. `filter_top_k`
8. `into_chat_message`
9. `chat_completion_stream`

## TODO
- [chat][P1][todo] 完成条件：补齐对话请求与流式响应编排；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/services/chat_pipeline/README.md`。
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/services/chat_pipeline/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/services/chat_pipeline/README.md`。

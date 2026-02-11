# 文件职责：知识对话编排服务，作为 RAG 问答的核心入口，负责触发 ChatPipeline、创建 user/assistant 占位消息、管理 SSE 流式推送、处理 stop/continue-stream。
# 边界：编排 SessionService/MessageService/ChatPipeline/StreamManager/ContextManager 完成完整对话流程；不直接处理 HTTP 协议（由 Handler 层负责 SSE 封装）。
# 对标：WeKnora internal/application/service/session.go 中的 KnowledgeQA/KnowledgeQAByEvent 逻辑（MVP 将这部分从 SessionService 中独立出来，职责更清晰）。

# TODO(M4): 实现 ChatService 类骨架。注入 SessionService、MessageService、ModelService、StreamManager、ContextManager、EventBus。
# TODO(M4): 实现 knowledge_chat()。接收 session_id + query，创建 user 消息和 assistant 占位消息（同事务），触发基础 Chat Pipeline（不接检索），通过 StreamManager 推送 SSE 事件。
# TODO(M4): 实现 stop_session()。校验消息完成状态后，向 StreamManager 写入 type="stop" 的 StreamEvent（对齐 WeKnora StopSession）；SSE 轮询侧检测到 stop event 后通过 EventBus.emit(EventStop) 触发 context.cancel()，中断 Pipeline 流式生成。
# TODO(M4): 实现 continue_stream()。接收 Last-Event-ID，从 StreamManager 回放断点之后的事件，支持 SSE 断线重连。
# TODO(M6): 扩展 knowledge_chat()。接入检索 Pipeline（Search → Rerank → Merge → FilterTopK → IntoChatMessage），SSE 返回 references + answer 事件。
# TODO(M7): 扩展 knowledge_chat()。在 NEO4J_ENABLE=true 时，Pipeline 中加入 ExtractEntity + SearchEntity 步骤，将图谱检索结果并入结果集。

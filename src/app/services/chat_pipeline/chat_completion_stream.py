# 文件职责：实现 ChatCompletionStream 插件，调用 LLM 进行流式生成，将 token 逐个推送到 EventBus/StreamManager，并在完成后更新 assistant 消息。
# 边界：仅负责 LLM 流式调用与事件推送，不组装 Prompt（由 into_chat_message.py 完成），不执行检索。
# 对标：WeKnora chat_completion_stream.go（PluginChatCompletionStream.OnEvent -> prepareChatModel -> stream 调用 -> 逐 token 推送 EventBus -> 更新消息状态）。

# TODO(M4): 实现 PluginChatCompletionStream 类。注册 CHAT_COMPLETION_STREAM 事件。
# TODO(M4): 调用 common.prepare_chat_model 获取模型实例，执行流式 chat completion。
# TODO(M4): 逐 token 推送到 EventBus，推送 SSE answer 事件（done=false），完成后推送 done=true。
# TODO(M4): 流式完成后更新 assistant message 的 content 和 is_completed 状态。

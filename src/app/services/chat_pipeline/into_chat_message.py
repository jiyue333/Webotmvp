# 文件职责：实现 IntoChatMessage 插件，将检索结果注入 System Prompt 模板，组装完整的 LLM 消息列表（system + history + user query）。
# 边界：仅负责 Prompt 组装，不调用 LLM，不执行检索。组装后的 messages 写入 ChatManage.messages。
# 对标：WeKnora into_chat_message.go（PluginIntoChatMessage.OnEvent -> 渲染上下文模板 -> 拼接 system/history/user -> 写入 ChatManage.Messages）。

# TODO(M4): 实现 PluginIntoChatMessage 类。注册 INTO_CHAT_MESSAGE 事件。
# TODO(M4): 基础实现：无检索结果时仅拼接 system prompt + history + user query（纯模型对话场景）。
# TODO(M6): 扩展实现：将 search_result 渲染到上下文模板，注入 system prompt 中。

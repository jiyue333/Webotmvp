# 文件职责：提供 Chat Pipeline 各插件共用的辅助函数，包括日志封装、模型准备、消息组装与 Prompt 渲染。
# 边界：仅包含无状态工具函数，不持有依赖实例，不感知具体步骤的业务语义。
# 对标：WeKnora common.go（pipelineInfo/Warn/Error + prepareChatModel + prepareMessagesWithHistory + renderSystemPromptPlaceholders）。

# TODO(M4): 实现 pipeline_info/warn/error 日志封装函数。接收 stage/action/fields，委托 infra.logger 输出结构化日志。
# TODO(M4): 实现 prepare_chat_model 函数。接收 model_service 和 chat_manage，返回 (chat_model, chat_options)。
# TODO(M4): 实现 prepare_messages_with_history 函数。渲染 system prompt 模板，拼接历史对话与当前查询，返回 messages 列表。
# TODO(M4): 实现 render_system_prompt_placeholders 函数。替换 {{current_time}} 等占位符。

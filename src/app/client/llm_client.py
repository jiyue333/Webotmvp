# 文件职责：封装 LLM（Chat 模型）的调用客户端，提供流式与非流式对话能力。
# 边界：仅负责 HTTP 请求发送与响应解析；不编排业务流程，不读写数据库。模型配置由调用方传入。
# 对齐来源：WeKnora internal/models/chat/chat.go（Chat 接口 + NewChat 工厂）。

# TODO(M4)：定义 LLMClient Protocol（继承 BaseModelClient），包含：
#   - async chat(messages: list[ChatMessage], *, temperature, max_tokens) -> ChatResponse
#   - async chat_stream(messages: list[ChatMessage], *, temperature, max_tokens) -> AsyncIterator[StreamChunk]
# TODO(M4)：实现 OpenAICompatibleLLMClient 类，对接 OpenAI 兼容 API（覆盖大部分 source）。入参 ModelClientConfig，使用 httpx.AsyncClient。
# TODO(M4)：实现 chat_stream 的 SSE 解析逻辑，逐 token 返回 StreamChunk。对齐 WeKnora internal/models/chat/sse_reader.go。
# TODO(M7)：如需图谱实体抽取调用 LLM，在此文件中不新增逻辑，由 service 层复用 chat 接口。

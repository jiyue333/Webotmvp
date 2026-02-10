# 文件职责：定义 ContextManager 协议与默认实现，管理 LLM 对话上下文的读写与压缩。对齐 WeKnora llmcontext/context_manager.go。
# 边界：编排 ContextStorage（存储） + CompressionStrategy（压缩）；不直接操作 Redis，不执行 LLM 调用（委托给 compression 策略）。

# TODO(M4)：将共享类型（ContextMessage、ContextStats）抽出到 context/types.py，
#   避免 storage.py / compression.py 反向导入 context_manager.py 导致循环依赖。
# TODO(M4)：定义 ContextMessage dataclass（role: str, content: str），对齐 WeKnora internal/models/chat/chat.go Message。
# TODO(M4)：定义 ContextStats dataclass（message_count, token_count, is_compressed, original_message_count），对齐 WeKnora interfaces.ContextStats。
# TODO(M4)：定义 ContextManager Protocol，包含：
#   - async add_message(session_id, message: ContextMessage) -> None
#   - async get_context(session_id) -> list[ContextMessage]
#   - async clear_context(session_id) -> None
#   - async get_context_stats(session_id) -> ContextStats
#   - async set_system_prompt(session_id, system_prompt: str) -> None
# TODO(M4)：实现 DefaultContextManager 类。接收 storage: ContextStorage, compression: CompressionStrategy, max_tokens: int。
#   add_message 时先 load -> append -> 判断是否需压缩 -> save。
# TODO(M4)：实现 create_context_manager(storage_type, max_tokens) 工厂函数，根据 storage_type 选择 Redis 或 Memory 后端。

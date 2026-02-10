# 文件职责：定义 ContextStorage 协议，将上下文的序列化存储与业务逻辑解耦。对齐 WeKnora llmcontext/storage.go。
# 边界：只定义存储接口；Redis 实现和 Memory 实现各自在本文件中提供。不包含压缩逻辑（由 compression.py 负责）。

# TODO(M4)：定义 ContextStorage Protocol，包含：
#   - async save(session_id, messages: list[ContextMessage]) -> None
#   - async load(session_id) -> list[ContextMessage]
#   - async delete(session_id) -> None
#   - async append(session_id, message: ContextMessage) -> None  ← 追加语义，避免全量覆盖的并发写入风险
#   注意：仅有 save（全量覆盖）时，并发会话写入会导致"后写覆盖前写"。
#   建议至少提供 append 原子追加接口，或基于版本号/CAS 的乐观更新策略。
# TODO(M4)：实现 MemoryContextStorage 类，使用 dict[str, list[ContextMessage]] 在内存中存储，用于开发调试。
# TODO(M4)：实现 RedisContextStorage 类，使用 Redis List/Hash 存储序列化后的上下文。
#   接收 redis client 依赖，key 格式为 "ctx:{session_id}"。
#   append 可直接使用 RPUSH 实现原子追加。

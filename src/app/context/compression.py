# 文件职责：定义 CompressionStrategy 协议与内置压缩策略实现。对齐 WeKnora llmcontext/compression_strategies.go。
# 边界：只负责消息列表的压缩/截断逻辑；不操作存储、不处理 HTTP 请求。

# TODO(M4)：定义 CompressionStrategy Protocol，包含：
#   - async compress(messages: list[ContextMessage], max_tokens: int) -> list[ContextMessage]
#   - estimate_tokens(messages: list[ContextMessage]) -> int
# TODO(M4)：实现 SlidingWindowStrategy 类。保留 system 消息和最近 N 条常规消息，丢弃较早的消息。对齐 WeKnora slidingWindowStrategy。
# TODO(M4)：实现 estimate_tokens 方法，使用 "4 字符 ≈ 1 token" 的粗略估算。
# TODO(M7)：可选实现 SmartCompressionStrategy 类（LLM 摘要压缩）。仅在图谱增强阶段按需引入，不作为 M4 必须项。

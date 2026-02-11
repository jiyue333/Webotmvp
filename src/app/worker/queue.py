# 文件职责：基于 Redis Stream（XADD / XREADGROUP / XACK）封装任务队列，提供消息投递、消费、确认与死信回收能力。对齐 WeKnora Asynq 的队列语义，底层用 Redis Stream 替代 Redis List。
# 边界：只负责队列读写与消息生命周期管理；不感知任务内容或业务逻辑（由 ingestion_worker 和 services 层承担）；不管理 Redis 连接（连接实例由 infra 层注入）。

# TODO(M5)：实现 TaskQueue 类。初始化接收 Redis 客户端实例、stream_name（默认 "tasks:document"）、group_name（默认 "worker-group"）、consumer_name（从环境变量或参数获取，支持多实例部署）。
# TODO(M5)：实现 ensure_group() 方法。调用 XGROUP CREATE（IF NOT EXISTS）创建消费者组；应用启动时调用一次。
# TODO(M5)：实现 enqueue(envelope: TaskEnvelope) -> str 方法。将 TaskEnvelope 序列化为 JSON，调用 XADD 写入 Stream，返回 stream_message_id。由 KnowledgeService 在创建 knowledge 记录后调用。
# TODO(M5)：实现 dequeue(count: int = 1, block_ms: int = 5000) -> list[ReceivedMessage] 方法。调用 XREADGROUP 读取新消息，反序列化为 ReceivedMessage 返回。
# TODO(M5)：实现 ack(stream_message_id: str) 方法。调用 XACK 确认消息已成功处理，Redis 从 pending 列表移除该消息。
# TODO(M5)：实现 reclaim_stale(min_idle_ms: int = 600000) -> list[ReceivedMessage] 方法。调用 XPENDING + XCLAIM 回收超时未确认的消息（默认 10 分钟），重新分配给当前 consumer 处理。
# TODO(M5)：定义 ReceivedMessage 数据类。字段：
#   - stream_message_id: str  — Redis Stream 分配的消息 ID（如 "1234567890-0"），用于 XACK
#   - envelope: TaskEnvelope  — 反序列化后的任务信封（来自 tasks.py），包含 task_id / task_type / payload 等业务字段
#   分层：ReceivedMessage 是传输层概念（Stream 消息），TaskEnvelope 是业务层概念（任务内容），两者不混用。

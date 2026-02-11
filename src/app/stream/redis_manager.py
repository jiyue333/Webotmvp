# 文件职责：基于 Redis 实现 StreamManager 协议，提供 SSE 事件流的追加与按 event_id 续读能力。对齐 WeKnora internal/stream/redis_manager.go，续流语义升级为 SSE 标准 Last-Event-ID。
# 边界：只负责事件在 Redis 中的序列化存取；不处理 SSE 协议编码（由 handler 层负责），不生成业务事件内容（由 chat_pipeline 负责）。

# TODO(M4)：实现 RedisStreamManager 类，注入 redis 异步客户端和配置（key_prefix, ttl）。
# TODO(M4)：实现 append_event() 方法。分配 event_id（格式 evt_{message_id}_{seq}，seq 通过 Redis INCR 原子自增），将 StreamEvent 序列化为 JSON 后 RPush 到 Redis List。额外维护 Hash key 记录 event_id → list_index 映射，用于 Last-Event-ID 定位。对 List key 设置 TTL。
# TODO(M4)：实现 get_events_after(session_id, message_id, after_event_id: str | None) -> list[StreamEvent] 方法。after_event_id 为 None 时 LRange(0, -1) 返回全量；非 None 时通过 Hash 查到对应 index，LRange(index+1, -1) 返回增量事件。
# TODO(M4)：实现 close() 方法，释放连接资源。
# TODO(M8)：考虑用 Redis Stream（XADD/XRANGE）替代 List+Hash，原生支持 ID 范围查询，简化实现。

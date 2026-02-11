# 文件职责：定义 StreamManager 协议（Protocol）和 StreamEvent 数据模型，以及流管理器工厂函数。对齐 WeKnora internal/stream/factory.go 和 internal/types/interfaces/stream_manager.go。
# 边界：只定义接口契约和数据结构；不实现具体的存储逻辑（由 redis_manager.py 负责），不感知 HTTP/SSE 层。

# TODO(M4)：定义 StreamEvent 数据类，包含 id: str, type: str (references/answer/error/stop/complete), content: str, done: bool, timestamp: datetime, data: dict 字段。id 格式：evt_{message_id}_{seq}，由 StreamManager 在 append 时分配，同时作为 SSE id: 字段推送给客户端。对齐 mvp.md §4.3.4 SSE 事件格式。
# TODO(M4)：定义 StreamManager Protocol，包含以下方法：
#   - append_event(session_id, message_id, event) -> StreamEvent：追加事件，分配唯一 event_id 并返回完整事件。
#   - get_events_after(session_id, message_id, after_event_id: str | None) -> list[StreamEvent]：返回 after_event_id 之后的所有事件。after_event_id 为 None 时返回全量。浏览器断线重连时 Last-Event-ID 即为 after_event_id。
# TODO(M4)：实现 create_stream_manager() 工厂函数，根据配置返回 RedisStreamManager 实例。MVP 仅支持 Redis 后端，不做 Memory 适配。

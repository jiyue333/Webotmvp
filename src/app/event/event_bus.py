# 文件职责：实现 EventBus 事件总线，提供 on/emit 发布-订阅机制，解耦 pipeline 各阶段与 SSE 推送之间的通知。对齐 WeKnora internal/event/event.go。
# 边界：仅管理 handler 注册与事件分发；不感知具体业务数据结构（由 events.py 定义），不直接操作 Redis/DB。

# TODO(M4)：定义 EventBus 类，包含 _handlers: dict[EventType, list[EventHandler]] 和 _async_mode: bool 字段。
# TODO(M4)：实现 on(event_type, handler) -> Callable[[], None] 方法。注册 handler 并返回 unsubscribe 闭包，调用该闭包可精确移除本次注册的 handler，不影响同类型下其他订阅方。
# TODO(M4)：实现 emit(event) 方法。同步模式下依次调用 handler，异步模式下使用 asyncio.create_task 触发。
# TODO(M4)：实现 emit_and_wait(event) 方法。异步触发后通过 asyncio.gather 等待所有 handler 完成。
# TODO(M4)：实现 clear(event_type=None) 方法。event_type 非空时清除该类型所有 handler，为空时清除全部。仅用于 shutdown / test 场景，日常移除请使用 on() 返回的 unsubscribe。
# TODO(M4)：提供模块级 get_event_bus() 单例工厂函数，供 container.py 注册和各模块获取全局实例。对齐 WeKnora internal/event/global.go。

# 文件职责：配置全局日志格式，并提供 get_logger(name) 工厂函数供各模块获取 logger 实例。对齐 WeKnora internal/logger/logger.go。
# 边界：只负责日志格式化、handler 配置、logger 实例分发；不负责 request_id 注入（由 middleware 层负责），不处理指标或追踪。

# TODO(M2)：配置 Python logging，使用 JSON 格式输出（可选 python-json-logger），包含 timestamp / level / logger / message 基础字段。
# TODO(M2)：提供 get_logger(name: str) -> logging.Logger 工厂函数，供各模块获取 logger 实例。对齐 WeKnora logger.GetLogger(ctx)。
# TODO(M8)：集成 structlog 或等效方案，将 request_id / user_id / session_id / kb_id / latency / error_code 绑定到上下文化日志中。
# TODO(M8)：配置日志级别从 AppSettings.LOG_LEVEL 读取，支持运行时调整。对齐 WeKnora logger.SetLogLevel。

# 文件职责：实现请求/响应日志中间件，记录每次 HTTP 请求的 method/path/status/latency 等结构化字段。对齐 WeKnora internal/middleware/logger.go 的 Logger() 中间件。
# 边界：只负责 HTTP 层访问日志；应用内部业务日志由各模块直接使用 logger，日志基础设施配置在 common/logger.py。

# TODO(M8)：实现 LoggerMiddleware。在请求开始时记录 request_id / method / path / client_ip，请求结束时记录 status_code / latency_ms / response_size。
# TODO(M8)：对敏感字段（password / api_key / token）做脱敏处理后再写入日志。
# TODO(M8)：对 /health 等高频探针路径可配置跳过日志，减少噪音。

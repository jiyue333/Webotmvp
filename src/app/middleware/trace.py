# 文件职责：实现 OpenTelemetry 追踪中间件，为每个 HTTP 请求创建 span，记录请求/响应属性，传播 trace context。对齐 WeKnora internal/middleware/trace.go 的 TracingMiddleware()。
# 边界：只负责 HTTP 层 span 创建和上下文传播；tracer/exporter 初始化在 infra/ 层，业务 span（如检索、生成）由各 service 自行创建。

# TODO(M8)：实现 TracingMiddleware。创建 server span，设置 http.method / http.route / http.status_code 等标准属性。
# TODO(M8)：从请求 header 提取上游 trace context（W3C Traceparent），保证分布式追踪链路完整。
# TODO(M8)：将 trace_id 注入 request.state.trace_id，供日志中间件关联使用。

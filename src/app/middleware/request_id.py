# 文件职责：实现请求 ID 中间件，为每个 HTTP 请求生成或提取唯一 request_id，注入 request.state 和响应 header。对齐 WeKnora internal/middleware/logger.go 的 RequestID() 中间件。
# 边界：只负责 request_id 的生成与传播；不生成 trace_id（由 trace.py 负责），下游中间件和 handler 通过 request.state.request_id 获取。

# TODO(M1)：实现 RequestIDMiddleware。优先从 X-Request-ID header 提取，不存在则生成 uuid4。写入 request.state.request_id 并在响应 header 回传 X-Request-ID。

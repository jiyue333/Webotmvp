# middleware/

## 目录职责
HTTP 请求链路中间件，处理横切关注点（鉴权、日志、追踪、请求标识）。

## 边界
- 只处理横切关注点，不执行业务领域逻辑。
- 上游由 `__init__.py` 的 `register_middlewares()` 统一注册到 FastAPI 应用。
- 下游传递给路由 handler。
- **异常处理器不在此目录**：全局异常处理器位于 `common/error_handler.py`，在 `main.py` 中注册。

## 中间件执行顺序（由外到内）
1. `request_id.py` — 请求 ID 生成/提取
2. `trace.py` — OpenTelemetry 追踪 span 创建
3. `logger.py` — HTTP 访问日志
4. `auth.py` — JWT 鉴权与用户上下文注入

## 文件清单
| 文件            | 职责                                         | 实现阶段 |
| --------------- | -------------------------------------------- | -------- |
| `__init__.py`   | 统一注册所有中间件，控制执行顺序             | M1       |
| `request_id.py` | 生成/提取 X-Request-ID，注入 request.state   | M1       |
| `auth.py`       | JWT token 校验，用户上下文注入，免鉴权白名单 | M2       |
| `logger.py`     | HTTP 请求/响应结构化日志                     | M8       |
| `trace.py`      | OpenTelemetry span 创建与 trace context 传播 | M8       |

## 与 WeKnora 的对照
- WeKnora 的 `error_handler.go` 在 `middleware/` 下，因为 Gin 没有独立的 exception_handler 机制。FastAPI 原生支持 `app.add_exception_handler()`，因此将其移至 `common/error_handler.py`，概念更清晰。
- WeKnora 的 `recovery.go` 在 Python/FastAPI 中不需要单独中间件，未捕获异常由 `common/error_handler.py` 兜底处理。
- WeKnora 的 `RequestID()` 在 `logger.go` 中，MVP 独立为 `request_id.py` 便于职责清晰。

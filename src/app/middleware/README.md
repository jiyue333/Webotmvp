# middleware/

## 文件职责
- 定义请求链路中的中间件职责与推荐注册顺序。
- 统一 request_id、鉴权、异常处理、日志与追踪行为。

## 边界
- 中间件不承载领域业务逻辑。
- 中间件应保持可复用、可观测、可回放。

## 推荐顺序
1. `request_id.py`
2. `trace.py`
3. `logger.py`
4. `recovery.py`
5. `error_handler.py`
6. `auth.py`

## TODO
- [arch][P1][todo] 在 M1 固化中间件注册顺序并在入口统一装配。
- [auth][P1][todo] 在 M2 完成 JWT 鉴权中间件。
- [obs][P2][todo] 在 M8 完善 trace/span 与日志关联。

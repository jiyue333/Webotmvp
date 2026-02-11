# 文件职责：统一注册所有 HTTP 中间件到 FastAPI 应用实例，控制中间件执行顺序。对齐 WeKnora internal/router/router.go 中间件注册段。
# 边界：只负责按序 app.add_middleware()；不实现具体中间件逻辑，不包含业务路由注册。异常处理器（exception_handler）由 common/error_handler.py 定义，在 main.py 中注册。

# TODO(M1)：定义 register_middlewares(app: FastAPI) 函数。
# TODO(M1)：注册 CORSMiddleware（allow_origins=["*"]，前端跨域必需）。
# TODO(M1)：注册 RequestIDMiddleware。从 request_id.py 导入并 app.add_middleware()。
# TODO(M2)：注册 JWTAuthMiddleware。从 auth.py 导入并 app.add_middleware()。
# TODO(M8)：注册 LoggerMiddleware。从 logger.py 导入并 app.add_middleware()。
# TODO(M8)：注册 TracingMiddleware。从 trace.py 导入并 app.add_middleware()。

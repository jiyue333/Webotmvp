# 文件职责：装配 FastAPI 应用实例，注册中间件与路由，管理应用生命周期（启动/关闭）。对齐 WeKnora cmd/main.go + internal/router/router.go。
# 边界：只负责应用装配（中间件 → 路由 → 生命周期）；不承载业务逻辑，资源初始化委托给 container.py。

# TODO(M1)：定义 lifespan(app) 异步上下文管理器。启动时调用 container.startup()，关闭时调用 container.shutdown()，将 container 挂到 app.state。
# TODO(M1)：创建 FastAPI 实例 app，传入 lifespan。
# TODO(M1)：调用 register_middlewares(app) 注册中间件（从 app.middleware 导入）。
# TODO(M2)：调用 register_exception_handlers(app) 注册全局异常处理器（从 app.common.error_handler 导入）。
# TODO(M1)：调用 app.include_router(api_router, prefix="/api/v1") 挂载路由（从 app.api.router 导入）。
# TODO(M1)：定义 GET /health 端点，返回 {"status": "ok"}，用于运维探针。

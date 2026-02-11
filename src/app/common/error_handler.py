# 文件职责：注册全局异常处理器（app.add_exception_handler），捕获 AppError 及其子类、Pydantic ValidationError、未预期异常，统一转换为 mvp.md §4.3.1 响应壳格式。对齐 WeKnora internal/middleware/error_handler.go。
# 边界：只负责异常到 HTTP 响应的映射；异常类定义在 exceptions.py，错误码定义在 error_codes.py。兜底捕获未预期异常返回 500 + error_code=1001。不是中间件，在 main.py 中通过 register_exception_handlers(app) 注册。

# TODO(M2)：定义 register_exception_handlers(app: FastAPI) 函数，集中注册以下三类异常处理器。
# TODO(M2)：注册 AppError 异常处理器。从异常实例读取 error_code / message / details / status_code，构造 {success: false, error: {code, message, details}, request_id} 响应。
# TODO(M2)：注册兜底 Exception 处理器。记录 error 日志（含 traceback），返回 500 + error_code=1001 内部错误。
# TODO(M2)：注册 RequestValidationError 处理器。将 Pydantic 校验错误转换为 422 + error_code=1000 响应（保留 FastAPI 默认 details 格式）。

# 文件职责：定义业务异常基类 AppError 和常用子类，供 service 层抛出、api 层（exception_handler）捕获并转换为统一响应。
# 边界：只定义异常类层次结构；不包含错误码定义（由 error_codes.py 负责），不处理 HTTP 响应封装（由 api 层中间件负责）。

# TODO(M2)：定义 AppError(Exception) 基类，包含 error_code: int, message: str, details: dict 字段。
# TODO(M2)：定义常用子类 NotFoundError(AppError) / ValidationError(AppError) / AuthenticationError(AppError) / PermissionError(AppError) / ConflictError(AppError)，各自设置默认 error_code 和 HTTP status_code。
# TODO(M2)：在 main.py 或 middleware 层注册 exception_handler，将 AppError 子类自动映射为 HTTP 状态码 + 统一响应壳 {success: false, error: {code, message, details}}。

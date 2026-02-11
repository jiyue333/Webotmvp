# 文件职责：实现 JWT 鉴权中间件，从 Authorization header 提取并验证 token，将当前用户信息注入请求上下文。对齐 WeKnora internal/middleware/auth.go。
# 边界：只负责 token 解析与上下文注入；token 签发/刷新/撤销由 AuthService 负责，白名单路由判断在此处维护但不处理业务逻辑。

# TODO(M2)：定义 JWTAuthMiddleware 类或函数。解析 Authorization: Bearer <token>，校验签名与过期时间，查询 auth_tokens 表确认未撤销。
# TODO(M2)：将解码后的 user_id 注入 request.state.user_id，供下游 handler 使用。
# TODO(M2)：定义免鉴权白名单 NO_AUTH_PATHS（如 /auth/register, /auth/login, /health），匹配时跳过鉴权。
# TODO(M2)：鉴权失败时抛出 AuthenticationError(1101) 或 TokenExpiredError(1102)，由 common/error_handler 异常处理器统一捕获。

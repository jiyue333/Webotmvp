# 文件职责：提供安全相关工具函数：密码哈希、JWT 令牌生成/验证、敏感字段脱敏。对齐 WeKnora internal/middleware/auth.go。
# 边界：只提供无状态的纯函数工具；不访问数据库（token 持久化由 repository 负责），不处理 HTTP 请求（鉴权中间件由 middleware/ 负责）。

# TODO(M2)：实现 hash_password(plain: str) -> str。使用 bcrypt 或 passlib 生成密码哈希。
# TODO(M2)：实现 verify_password(plain: str, hashed: str) -> bool。验证密码是否匹配。
# TODO(M2)：实现 create_access_token(data: dict, expires_delta: timedelta) -> str。使用 python-jose 或 PyJWT 生成 JWT access_token。
# TODO(M2)：实现 create_refresh_token(data: dict, expires_delta: timedelta) -> str。生成 refresh_token。
# TODO(M2)：实现 decode_token(token: str) -> dict。验证并解码 JWT，失败时抛出 AuthenticationError。
# TODO(M3)：实现 mask_api_key(key: str) -> str。将 API key 脱敏为 "sk-****xxxx" 格式，供模型详情接口返回。

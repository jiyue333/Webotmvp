# 文件职责：用户认证鉴权服务，负责注册、登录、JWT 令牌生成/刷新/撤销、密码哈希校验。
# 边界：编排 UserRepository 与 AuthTokenRepository 完成鉴权流程，不直接处理 HTTP 请求；JWT 密钥由 infra/config 注入。
# 对标：WeKnora internal/application/service/user.go（Register/Login/RefreshToken/RevokeToken/ValidateToken/GenerateTokens）。

# TODO(M2): 实现 AuthService 类骨架。注入 UserRepository、AuthTokenRepository、Config（JWT 密钥/过期时间）。
# TODO(M2): 实现 register()。接收 username/email/password，校验唯一性，bcrypt 哈希后写入 users 表，返回用户信息。
# TODO(M2): 实现 login()。接收 email/password，校验密码，调用 _generate_tokens() 生成 access_token + refresh_token，持久化到 auth_tokens 表。
# TODO(M2): 实现 refresh_token()。校验 refresh_token 有效性与撤销状态，撤销旧 token，生成新 token 对。
# TODO(M2): 实现 revoke_token()。将 auth_tokens 记录标记 is_revoked=True。
# TODO(M2): 实现 validate_token()。解析 JWT、校验签名/过期、查询 auth_tokens 确认未撤销，返回当前用户。
# TODO(M2): 实现 _generate_tokens()。内部方法，生成 access + refresh JWT 并写入 auth_tokens 表。

# 文件职责：定义鉴权相关 DTO（注册/登录/刷新/用户信息），约束 /auth/* 端点的请求与响应类型。对齐 mvp.md §4.2.1。
# 边界：只定义数据结构与 Pydantic 校验规则；不包含鉴权逻辑（由 AuthService 负责），不处理 token 签发/验证。

# TODO(M2)：定义 RegisterRequest(BaseModel)，字段 username: str, email: EmailStr, password: str，添加长度/格式校验。
# TODO(M2)：定义 LoginRequest(BaseModel)，字段 email: EmailStr, password: str。
# TODO(M2)：定义 RefreshRequest(BaseModel)，字段 refresh_token: str。
# TODO(M2)：定义 TokenResponse(BaseModel)，字段 access_token: str, refresh_token: str, expires_in: int。
# TODO(M2)：定义 UserDetail(BaseModel)，字段 id: str, username: str, email: str, is_active: bool, created_at: datetime。

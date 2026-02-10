# 文件职责：定义用户认证鉴权相关的 HTTP 路由（register/login/refresh/logout/me）。
# 边界：仅处理请求参数校验与响应封装，鉴权逻辑委托给 AuthService，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M2)：实现 POST /register 端点。接收 username/email/password，调用 AuthService.register()，返回用户信息。
# TODO(M2)：实现 POST /login 端点。接收 email/password，调用 AuthService.login()，返回 access_token + refresh_token。
# TODO(M2)：实现 POST /refresh 端点。接收 refresh_token，调用 AuthService.refresh()，返回新的 access_token。
# TODO(M2)：实现 POST /logout 端点。从 header 取当前 token，调用 AuthService.logout() 撤销该 token。
# TODO(M2)：实现 GET /me 端点。通过 CurrentUserDep 获取当前用户，返回用户基本信息。

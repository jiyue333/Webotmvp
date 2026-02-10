// 文件职责：定义用户认证鉴权相关的 HTTP 接口（login/register/refresh/logout/me）。
// 边界：仅定义接口签名与返回类型；不包含状态管理逻辑，状态由 stores/auth.ts 维护。

import type { LoginResponseData, UserProfile } from '../types/api'

export function login(_data: any): Promise<LoginResponseData> {
  throw new Error('Not implemented')
}

export function register(_data: any): Promise<UserProfile> {
  throw new Error('Not implemented')
}

export function refreshToken(): Promise<{ accessToken: string }> {
  throw new Error('Not implemented')
}

export function logout(): Promise<void> {
  throw new Error('Not implemented')
}

export function getMe(): Promise<UserProfile> {
  throw new Error('Not implemented')
}

// TODO(M2)：实现 login，POST /api/v1/auth/login，接收 email/password，返回 access_token + refresh_token。
// TODO(M2)：实现 register，POST /api/v1/auth/register，接收 username/email/password，返回用户信息。
// TODO(M2)：实现 refreshToken，POST /api/v1/auth/refresh，接收 refresh_token，返回新 access_token。
// TODO(M2)：实现 logout，POST /api/v1/auth/logout，撤销当前令牌。
// TODO(M2)：实现 getMe，GET /api/v1/auth/me，返回当前用户信息。

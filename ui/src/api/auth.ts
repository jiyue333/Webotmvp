/**
 * 文件职责：认证相关 API 调用。
 * TODO：补充 register/refresh/logout 的完整异常处理分层。
 */
import http from './http'
import type { ApiResponse, LoginResponseData, UserProfile } from '../types/api'

export interface LoginPayload {
  email: string
  password: string
}

export async function login(payload: LoginPayload): Promise<LoginResponseData> {
  const { data } = await http.post<ApiResponse<LoginResponseData>>('/auth/login', payload)
  return data.data
}

export async function getMe(): Promise<UserProfile> {
  const { data } = await http.get<ApiResponse<UserProfile>>('/auth/me')
  return data.data
}

export async function logout(): Promise<void> {
  await http.post('/auth/logout')
}

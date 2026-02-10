/**
 * 文件职责：维护 `ui/src/api/auth.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [auth][P1][todo] 在 M2 完成本模块能力实现与回归验证。
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

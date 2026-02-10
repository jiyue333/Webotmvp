/**
 * 文件职责：封装 `auth` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [auth][P1][todo] 完成条件：打通认证鉴权闭环并沉淀错误码约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/auth.ts`。
 */

import http from './http'
import type { ApiResponse, LoginResponseData, UserProfile } from '../types/api'

export interface LoginPayload {
  email: string
  password: string
}

/**
 * 登录接口调用。
 * 输入：邮箱与密码；输出：token 与用户信息。
 */
export async function login(payload: LoginPayload): Promise<LoginResponseData> {
  const { data } = await http.post<ApiResponse<LoginResponseData>>('/auth/login', payload)
  return data.data
}

/**
 * 获取当前登录用户信息。
 * 依赖请求拦截器自动注入 Authorization 头。
 */
export async function getMe(): Promise<UserProfile> {
  const { data } = await http.get<ApiResponse<UserProfile>>('/auth/me')
  return data.data
}

/**
 * 登出接口调用。
 * 后续由 store 负责本地 token 清理。
 */
export async function logout(): Promise<void> {
  await http.post('/auth/logout')
}

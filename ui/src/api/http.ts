/**
 * 文件职责：维护 `ui/src/api/http.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。
 */

import axios, { AxiosError, type AxiosInstance } from 'axios'
import type { ApiResponse } from '../types/api'

const baseURL = import.meta.env.VITE_API_BASE_URL ?? '/api/v1'

const http: AxiosInstance = axios.create({
  baseURL,
  timeout: 15000
})

http.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

http.interceptors.response.use(
  (response) => response,
  (error: AxiosError<ApiResponse<never>>) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
    return Promise.reject(error)
  }
)

export default http

/**
 * 文件职责：维护 `auth` 状态仓库，统一页面状态读写与派发入口。
 * 边界：只维护前端状态与动作；上游由视图触发，下游调用 api 模块，不直接拼装网络协议。
 * TODO：
 * - [auth][P1][todo] 完成条件：打通认证鉴权闭环并沉淀错误码约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/auth.ts`。
 */

import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { getMe, login as loginApi, logout as logoutApi, type LoginPayload } from '../api/auth'
import type { UserProfile } from '../types/api'

export const useAuthStore = defineStore('auth', () => {
  const accessToken = ref<string | null>(localStorage.getItem('access_token'))
  const refreshToken = ref<string | null>(localStorage.getItem('refresh_token'))
  const user = ref<UserProfile | null>(null)

  const isAuthenticated = computed(() => Boolean(accessToken.value))

  /**
   * 登录并落地 token 与用户信息。
   * 副作用：写入 localStorage。
   */
  async function login(payload: LoginPayload): Promise<void> {
    const res = await loginApi(payload)
    accessToken.value = res.accessToken
    refreshToken.value = res.refreshToken
    user.value = res.user
    localStorage.setItem('access_token', res.accessToken)
    localStorage.setItem('refresh_token', res.refreshToken)
  }

  /**
   * 在已有 access token 的前提下拉取用户资料。
   * 若未登录则直接返回，不触发网络请求。
   */
  async function loadProfile(): Promise<void> {
    if (!accessToken.value) {
      return
    }
    user.value = await getMe()
  }

  /**
   * 退出登录并清理本地认证状态。
   * 无论后端请求成功与否，都会清理本地 token。
   */
  async function logout(): Promise<void> {
    try {
      await logoutApi()
    } finally {
      accessToken.value = null
      refreshToken.value = null
      user.value = null
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
    }
  }

  return {
    accessToken,
    refreshToken,
    user,
    isAuthenticated,
    login,
    loadProfile,
    logout
  }
})

/**
 * 文件职责：管理登录态（token + 用户信息）并提供认证动作。
 * TODO：接入 refresh token 自动续期与跨标签页同步。
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

  async function login(payload: LoginPayload): Promise<void> {
    const res = await loginApi(payload)
    accessToken.value = res.accessToken
    refreshToken.value = res.refreshToken
    user.value = res.user
    localStorage.setItem('access_token', res.accessToken)
    localStorage.setItem('refresh_token', res.refreshToken)
  }

  async function loadProfile(): Promise<void> {
    if (!accessToken.value) {
      return
    }
    user.value = await getMe()
  }

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

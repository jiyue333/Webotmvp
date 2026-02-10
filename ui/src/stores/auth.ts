// 文件职责：维护 auth 状态仓库（token、用户信息），统一页面状态读写与派发入口。
// 边界：只维护前端状态与动作；上游由视图触发，下游调用 api/auth 模块，不直接拼装网络协议。

import { defineStore } from 'pinia'
import { ref } from 'vue'
import type { UserProfile } from '../types/api'

export const useAuthStore = defineStore('auth', () => {
  const accessToken = ref<string | null>(null)
  const refreshToken = ref<string | null>(null)
  const user = ref<UserProfile | null>(null)

  async function login(_payload: any): Promise<void> {
    throw new Error('Not implemented')
  }

  async function loadProfile(): Promise<void> {
    throw new Error('Not implemented')
  }

  async function logout(): Promise<void> {
    throw new Error('Not implemented')
  }

  return { accessToken, refreshToken, user, login, loadProfile, logout }
})

// TODO(M2)：实现 login Action，调用 api/auth.login()，存储 token 到 state 与 localStorage。
// TODO(M2)：实现 loadProfile Action，调用 api/auth.getMe()，更新 user state。
// TODO(M2)：实现 logout Action，调用 api/auth.logout()，清空 token 和 user state。

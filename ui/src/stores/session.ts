// 文件职责：维护 session 状态仓库（会话列表、当前选中），统一会话相关状态读写。
// 边界：只维护前端状态与动作；上游由视图触发，下游调用 api/session 模块。

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSessionStore = defineStore('session', () => {
  const list = ref<any[]>([])
  const currentId = ref<string | null>(null)

  async function fetchSessions() {
    throw new Error('Not implemented')
  }

  return { list, currentId, fetchSessions }
})

// TODO(M4)：实现 fetchSessions Action，调用 api/session.list()，更新 list state。
// TODO(M4)：实现 createSession Action，调用 api/session.create()，自动切换到新会话。
// TODO(M4)：实现 deleteSession Action，调用 api/session.delete()，刷新列表。

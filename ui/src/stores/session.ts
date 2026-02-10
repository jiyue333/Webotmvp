/**
 * 文件职责：会话状态管理（Pinia Store）。
 * TODO [session][M4] 实现会话列表、当前会话等状态。
 */
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSessionStore = defineStore('session', () => {
    const list = ref<{ id: string; title: string }[]>([])
    const currentId = ref<string | null>(null)

    // TODO [session][M4] 实现 fetchSessions、createSession 等 action

    return { list, currentId }
})

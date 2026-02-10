/**
 * 文件职责：维护 `ui/src/stores/session.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [session][P1][todo] 在 M4 完成本模块能力实现与回归验证。
 */

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSessionStore = defineStore('session', () => {
    const list = ref<{ id: string; title: string }[]>([])
    const currentId = ref<string | null>(null)

    // TODO [session][M4] 实现 fetchSessions、createSession 等 action

    return { list, currentId }
})

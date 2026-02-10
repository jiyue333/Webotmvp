/**
 * 文件职责：维护 `session` 状态仓库，统一页面状态读写与派发入口。
 * 边界：只维护前端状态与动作；上游由视图触发，下游调用 api 模块，不直接拼装网络协议。
 * TODO：
 * - [session][P1][todo] 完成条件：补齐会话生命周期管理与停止语义；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/session.ts`。
 */

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useSessionStore = defineStore('session', () => {
    const list = ref<{ id: string; title: string }[]>([])
    const currentId = ref<string | null>(null)

    // [session][P1][todo] 完成条件：实现 fetchSessions、createSession 等 action；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/session.ts`。

    return { list, currentId }
})

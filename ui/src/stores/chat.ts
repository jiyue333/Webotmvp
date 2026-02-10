/**
 * 文件职责：维护 `ui/src/stores/chat.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [chat][P1][todo] 在 M4 完成本模块能力实现与回归验证。
 */

import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface ChatMessage {
    id: string
    role: 'user' | 'assistant'
    content: string
}

export const useChatStore = defineStore('chat', () => {
    const messages = ref<ChatMessage[]>([])
    const isStreaming = ref(false)

    // TODO [chat][M4] 实现 sendMessage、appendChunk、clearMessages 等 action

    return { messages, isStreaming }
})

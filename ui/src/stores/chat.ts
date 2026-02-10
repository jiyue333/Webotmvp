/**
 * 文件职责：对话状态管理（Pinia Store）。
 * TODO [chat][M4] 实现消息列表、流式状态、加载状态等。
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

/**
 * 文件职责：维护 `chat` 状态仓库，统一页面状态读写与派发入口。
 * 边界：只维护前端状态与动作；上游由视图触发，下游调用 api 模块，不直接拼装网络协议。
 * TODO：
 * - [chat][P1][todo] 完成条件：补齐对话请求与流式响应编排；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/chat.ts`。
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

    // [chat][P1][todo] 完成条件：实现 sendMessage、appendChunk、clearMessages 等 action；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/chat.ts`。

    return { messages, isStreaming }
})

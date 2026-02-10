// 文件职责：维护 chat 状态仓库（消息列表、流式状态），统一对话相关状态读写。
// 边界：只维护前端状态与动作；上游由视图触发，下游调用 api/chat 和 api/message 模块。

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useChatStore = defineStore('chat', () => {
  const messages = ref<any[]>([])
  const isStreaming = ref(false)

  async function sendMessage(_content: string) {
    throw new Error('Not implemented')
  }

  return { messages, isStreaming, sendMessage }
})

// TODO(M4)：实现 sendMessage Action，调用 api/chat.sendChatMessage()，处理 SSE 流式接收。
// TODO(M4)：实现 loadHistory Action，调用 api/message.loadBySession()，支持向上翻页。
// TODO(M4)：实现 stopGeneration Action，调用 api/session.stop()，中断流式生成。

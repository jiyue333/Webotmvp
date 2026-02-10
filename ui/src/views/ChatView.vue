<!--
文件职责：承载 `ChatView` 页面交互逻辑与展示职责，编排用户动作与状态反馈。
边界：只负责页面渲染与交互编排；上游接收路由进入，下游调用 store/api，不沉淀底层请求实现。
TODO：
- [chat][P1][todo] 完成条件：补齐对话请求与流式响应编排；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/views/ChatView.vue`。
-->

<template>
  <section class="page chat-page">
    <h1>对话</h1>
    <p class="muted">M1 提供基础 SSE 骨架，M4/M6 按后端接口完善交互。</p>

    <div class="grid">
      <label>
        <span>Session ID</span>
        <input v-model="sessionId" class="input" placeholder="请输入 session_id" />
      </label>

      <label>
        <span>问题</span>
        <textarea v-model="query" class="textarea" rows="4" placeholder="输入问题"></textarea>
      </label>
    </div>

    <div class="actions">
      <button class="btn btn-primary" :disabled="streaming" @click="startStream">开始对话</button>
      <button class="btn btn-ghost" :disabled="!streaming" @click="stopStream">停止</button>
    </div>

    <div class="messages">
      <article v-for="(msg, idx) in messages" :key="`${idx}-${msg.type}`" class="message">
        <header>{{ msg.type }}</header>
        <pre>{{ msg.content }}</pre>
      </article>
    </div>

    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
/**
 * 文件职责：对话页面，负责发起知识对话并消费 SSE 流。
 * [chat][P1][todo] 完成条件：补充 references 卡片、continue-stream 与 stop API 联动。；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/views/ChatView.vue`。
 */
import { ref } from 'vue'
import type { ChatStreamEvent } from '../types/api'

const sessionId = ref('')
const query = ref('')
const messages = ref<Array<{ type: string; content: string }>>([])
const error = ref('')
const streaming = ref(false)
let controller: AbortController | null = null

async function startStream() {
  // 发起 SSE 对话并逐块消费响应；遇到 done 或异常时结束流状态。
  if (!sessionId.value || !query.value) {
    error.value = 'session_id 和 query 不能为空'
    return
  }

  error.value = ''
  streaming.value = true
  messages.value = []
  controller = new AbortController()

  try {
    const token = localStorage.getItem('access_token')
    const res = await fetch(`/api/v1/knowledge-chat/${sessionId.value}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(token ? { Authorization: `Bearer ${token}` } : {})
      },
      body: JSON.stringify({ query: query.value }),
      signal: controller.signal
    })

    if (!res.ok || !res.body) {
      throw new Error(`SSE 请求失败: ${res.status}`)
    }

    const reader = res.body.getReader()
    const decoder = new TextDecoder('utf-8')
    let buffer = ''

    while (streaming.value) {
      const { value, done } = await reader.read()
      if (done) {
        break
      }

      buffer += decoder.decode(value, { stream: true })
      const blocks = buffer.split('\n\n')
      buffer = blocks.pop() ?? ''

      for (const block of blocks) {
        const line = block
          .split('\n')
          .find((item) => item.startsWith('data:'))

        if (!line) {
          continue
        }

        const json = line.slice(5).trim()
        const event = JSON.parse(json) as ChatStreamEvent
        messages.value.push({ type: event.response_type, content: event.content ?? '' })

        if (event.done) {
          streaming.value = false
          break
        }
      }
    }
  } catch (err) {
    if ((err as Error).name !== 'AbortError') {
      error.value = err instanceof Error ? err.message : '流式对话失败'
    }
  } finally {
    streaming.value = false
    controller = null
  }
}

function stopStream() {
  // 手动停止：中断 fetch 流并重置 streaming 标记。
  streaming.value = false
  controller?.abort()
}
</script>

<style scoped>
.chat-page {
  display: grid;
  gap: 14px;
}

.grid {
  display: grid;
  gap: 12px;
}

label {
  display: grid;
  gap: 6px;
}

.actions {
  display: flex;
  gap: 10px;
}

.messages {
  display: grid;
  gap: 8px;
}

.message {
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px;
}

.message header {
  font-weight: 600;
  margin-bottom: 6px;
}

.message pre {
  white-space: pre-wrap;
  margin: 0;
}

.error {
  color: var(--danger);
}
</style>

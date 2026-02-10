/**
 * 文件职责：封装 `message` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [message][P1][todo] 完成条件：补齐消息加载与持久化约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/message.ts`。
 */

import http from './http'

export interface MessageItem {
    id: string
    session_id: string
    role: 'user' | 'assistant'
    content: string
}

export const messageApi = {
    listBySession: (sessionId: string) => http.get<MessageItem[]>(`/sessions/${sessionId}/messages`),
}

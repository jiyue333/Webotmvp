/**
 * 文件职责：封装 `chat` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [chat][P1][todo] 完成条件：补齐对话请求与流式响应编排；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/chat.ts`。
 */

export interface ChatRequest {
    session_id: string
    knowledge_base_id: string
    query: string
}

/**
 * 发起 SSE 流式对话请求。
 * TODO：
 * - [chat][P1][todo] 完成条件：使用 EventSource 或 fetch + ReadableStream 实现；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/chat.ts`。
 */
export function sendChatMessage(_req: ChatRequest): void {
    // placeholder
}

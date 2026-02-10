/**
 * 文件职责：对话（Chat）API 调用，含 SSE 流式请求。
 * TODO [chat][M4] 实现 SSE 流式对话接口调用。
 */

export interface ChatRequest {
    session_id: string
    knowledge_base_id: string
    query: string
}

/**
 * 发起 SSE 流式对话请求。
 * TODO [chat][M4] 使用 EventSource 或 fetch + ReadableStream 实现。
 */
export function sendChatMessage(_req: ChatRequest): void {
    // placeholder
}

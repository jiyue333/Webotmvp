// 文件职责：定义知识对话相关的 HTTP 接口（SSE 流式对话）。
// 边界：仅定义接口签名与请求类型；SSE 连接管理由 composables/useSSE.ts 封装。

export interface ChatRequest {
    session_id: string
    knowledge_base_id: string
    query: string
    temperature?: number
}

export function sendChatMessage(_req: ChatRequest): void {
    throw new Error('Not implemented')
}

// TODO(M4)：实现 sendChatMessage，POST /api/v1/knowledge-chat/{session_id}，使用 SSE 流式推送 answer/references。
// TODO(M4)：封装 SSE 事件解析，对齐 mvp.md §4.3.4 事件格式（references → answer → done）。

/**
 * 文件职责：维护 `ui/src/api/chat.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [chat][P1][todo] 在 M4 完成本模块能力实现与回归验证。
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

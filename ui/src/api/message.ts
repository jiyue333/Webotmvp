// 文件职责：定义消息管理相关的 HTTP 接口（历史消息加载）。
// 边界：仅定义接口签名与类型；不包含状态管理逻辑。

export interface MessageItem {
    id: string
    session_id: string
    role: 'user' | 'assistant'
    content: string
    knowledge_references?: unknown[]
    is_completed?: boolean
    created_at?: string
}

export const messageApi = {
    loadBySession: (_sessionId: string, _beforeId?: string, _limit?: number): Promise<MessageItem[]> => {
        throw new Error('Not implemented')
    }
}

// TODO(M4)：实现 loadBySession，GET /api/v1/messages/{session_id}/load，支持 before_id 和 limit 向上翻页。

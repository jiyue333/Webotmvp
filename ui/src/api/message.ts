/**
 * 文件职责：消息（Message）API 调用。
 * TODO [message][M4] 实现消息历史查询等接口调用。
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

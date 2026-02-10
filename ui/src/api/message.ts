/**
 * 文件职责：维护 `ui/src/api/message.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [message][P1][todo] 在 M4 完成本模块能力实现与回归验证。
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

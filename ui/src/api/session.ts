/**
 * 文件职责：会话（Session）API 调用。
 * TODO [session][M4] 实现会话的 CRUD 接口调用。
 */
import http from './http'

export interface SessionItem {
    id: string
    knowledge_base_id: string
    title: string
}

export const sessionApi = {
    list: (params?: { knowledge_base_id?: string }) => http.get<SessionItem[]>('/sessions', { params }),
    getById: (id: string) => http.get<SessionItem>(`/sessions/${id}`),
    create: (data: Partial<SessionItem>) => http.post('/sessions', data),
    delete: (id: string) => http.delete(`/sessions/${id}`),
}

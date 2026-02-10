/**
 * 文件职责：维护 `ui/src/api/session.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [session][P1][todo] 在 M4 完成本模块能力实现与回归验证。
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

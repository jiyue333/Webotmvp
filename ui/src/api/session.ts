/**
 * 文件职责：封装 `session` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [session][P1][todo] 完成条件：补齐会话生命周期管理与停止语义；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/session.ts`。
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

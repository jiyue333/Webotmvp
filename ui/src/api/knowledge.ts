/**
 * 文件职责：封装 `knowledge` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [knowledge][P1][todo] 完成条件：补齐知识条目管理与状态流转约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/knowledge.ts`。
 */

import http from './http'

export interface KnowledgeItem {
    id: string
    knowledge_base_id: string
    name: string
    source_type: string
}

export const knowledgeApi = {
    list: (kbId: string) => http.get<KnowledgeItem[]>(`/knowledge-bases/${kbId}/knowledge`),
    getById: (kbId: string, id: string) => http.get<KnowledgeItem>(`/knowledge-bases/${kbId}/knowledge/${id}`),
    create: (kbId: string, data: Partial<KnowledgeItem>) => http.post(`/knowledge-bases/${kbId}/knowledge`, data),
    delete: (kbId: string, id: string) => http.delete(`/knowledge-bases/${kbId}/knowledge/${id}`),
}

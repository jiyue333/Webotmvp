/**
 * 文件职责：知识（Knowledge）API 调用。
 * TODO [knowledge][M3] 实现知识条目的 CRUD 接口调用。
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

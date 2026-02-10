/**
 * 文件职责：维护 `ui/src/api/knowledge.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [knowledge][P1][todo] 在 M3 完成本模块能力实现与回归验证。
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

/**
 * 文件职责：维护 `ui/src/api/model.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [model][P1][todo] 在 M3 完成本模块能力实现与回归验证。
 */

import http from './http'

export interface ModelItem {
    id: string
    name: string
    provider_type: string
}

export const modelApi = {
    list: () => http.get<ModelItem[]>('/models'),
    getById: (id: string) => http.get<ModelItem>(`/models/${id}`),
    create: (data: Partial<ModelItem>) => http.post('/models', data),
    update: (id: string, data: Partial<ModelItem>) => http.put(`/models/${id}`, data),
    delete: (id: string) => http.delete(`/models/${id}`),
}

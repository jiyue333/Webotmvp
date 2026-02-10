/**
 * 文件职责：模型管理 API 调用。
 * TODO [model][M3] 实现 CRUD 接口调用。
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

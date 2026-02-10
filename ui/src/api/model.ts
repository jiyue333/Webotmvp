/**
 * 文件职责：封装 `model` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [model][P1][todo] 完成条件：补齐模型提供商与模型 CRUD 最小闭环；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/model.ts`。
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

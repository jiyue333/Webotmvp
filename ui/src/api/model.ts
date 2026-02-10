// 文件职责：定义模型管理相关的 HTTP 接口（provider 列表、模型 CRUD）。
// 边界：仅定义接口签名与类型；不包含状态管理逻辑。

export interface ProviderItem {
    provider: string
    display_name: string
    default_base_url: string
}

export interface ModelItem {
    id: string
    name: string
    type: 'llm' | 'embedding' | 'rerank'
    source: string
    description?: string
    parameters?: Record<string, unknown>
    is_default?: boolean
    status?: string
    created_at?: string
    updated_at?: string
}

export const modelApi = {
    listProviders: (): Promise<ProviderItem[]> => {
        throw new Error('Not implemented')
    },
    list: (_type?: string, _source?: string): Promise<ModelItem[]> => {
        throw new Error('Not implemented')
    },
    getById: (_id: string): Promise<ModelItem> => {
        throw new Error('Not implemented')
    },
    create: (_data: Partial<ModelItem>): Promise<ModelItem> => {
        throw new Error('Not implemented')
    },
    update: (_id: string, _data: Partial<ModelItem>): Promise<ModelItem> => {
        throw new Error('Not implemented')
    },
    delete: (_id: string): Promise<void> => {
        throw new Error('Not implemented')
    }
}

// TODO(M3)：实现 listProviders，GET /api/v1/models/providers，返回厂商列表。
// TODO(M3)：实现 list，GET /api/v1/models，支持 type/source 筛选。
// TODO(M3)：实现 getById，GET /api/v1/models/{id}，api_key 脱敏。
// TODO(M3)：实现 create，POST /api/v1/models，接收 name/type/source/parameters/is_default。
// TODO(M3)：实现 update，PUT /api/v1/models/{id}，可选字段更新。
// TODO(M3)：实现 delete，DELETE /api/v1/models/{id}，需检查是否被知识库引用。

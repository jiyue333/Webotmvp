// 文件职责：维护前端共享类型定义，统一 API 响应结构与业务实体约束。
// 边界：仅包含类型/接口声明；不包含运行时逻辑。各业务模块的局部类型在对应 api/*.ts 中定义。

export interface ApiError {
  code?: number
  message: string
  details?: unknown
}

export interface ApiResponse<T> {
  success: boolean
  data: T
  request_id?: string
  error?: ApiError
}

export interface PaginatedData<T> {
  items: T[]
  total: number
  page: number
  page_size: number
}

export interface UserProfile {
  id: string
  username: string
  email: string
  is_active?: boolean
  created_at?: string
}

export interface LoginResponseData {
  access_token: string
  refresh_token: string
  expires_in: number
}

export interface KnowledgeBaseItem {
  id: string
  name: string
  description?: string
  embedding_model_id?: string
  chunking_config?: Record<string, unknown>
  created_at?: string
  updated_at?: string
}

export interface ChatStreamEvent {
  id: string
  response_type: 'references' | 'answer' | 'error'
  content: string
  done: boolean
  knowledge_references?: Array<{
    chunk_id: string
    knowledge_id: string
    knowledge_title: string
    content: string
    score: number
  }>
}

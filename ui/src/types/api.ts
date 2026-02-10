/**
 * 文件职责：定义前端与后端交互的通用类型。
 * TODO：随接口稳定迭代细化业务实体字段。
 */
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

export interface UserProfile {
  id: string
  username: string
  email: string
}

export interface LoginResponseData {
  accessToken: string
  refreshToken: string
  user: UserProfile
}

export interface KnowledgeBaseItem {
  id: string
  name: string
  description?: string
  created_at?: string
}

export interface ChatStreamEvent {
  id: string
  response_type: 'references' | 'answer' | 'error' | 'stop' | 'complete' | string
  content: string
  done: boolean
  knowledge_references?: unknown[]
  data?: Record<string, unknown>
}

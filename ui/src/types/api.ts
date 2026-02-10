/**
 * 文件职责：维护 `ui/src/types/api.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。
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

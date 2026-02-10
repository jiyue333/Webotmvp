/**
 * 文件职责：维护前端共享类型定义，统一 API 与状态结构约束。
 * 边界：只维护类型约束；上游供各模块引用，下游不包含执行逻辑。
 * TODO：
 * - [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/types/api.ts`。
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

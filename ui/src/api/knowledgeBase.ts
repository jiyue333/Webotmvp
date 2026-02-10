/**
 * 文件职责：封装 `knowledgeBase` 前端 API 调用，隔离页面与 HTTP 实现细节。
 * 边界：只封装 HTTP 请求与响应解析；上游由 store/view 调用，下游对接后端 API，不管理页面状态。
 * TODO：
 * - [knowledge][P1][todo] 完成条件：补齐知识条目管理与状态流转约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/api/knowledgeBase.ts`。
 */

import http from './http'
import type { ApiResponse, KnowledgeBaseItem } from '../types/api'

/**
 * 拉取知识库列表。
 * 当前默认返回空数组兜底，避免页面层处理 null/undefined。
 */
export async function listKnowledgeBases(): Promise<KnowledgeBaseItem[]> {
  const { data } = await http.get<ApiResponse<KnowledgeBaseItem[]>>('/knowledge-bases')
  return data.data ?? []
}

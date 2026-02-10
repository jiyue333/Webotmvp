/**
 * 文件职责：知识库管理相关 API 调用。
 * TODO：补充分页参数、创建/更新/删除接口。
 */
import http from './http'
import type { ApiResponse, KnowledgeBaseItem } from '../types/api'

export async function listKnowledgeBases(): Promise<KnowledgeBaseItem[]> {
  const { data } = await http.get<ApiResponse<KnowledgeBaseItem[]>>('/knowledge-bases')
  return data.data ?? []
}

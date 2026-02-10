/**
 * 文件职责：维护 `ui/src/api/knowledgeBase.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [knowledge][P1][todo] 在 M3 完成本模块能力实现与回归验证。
 */

import http from './http'
import type { ApiResponse, KnowledgeBaseItem } from '../types/api'

export async function listKnowledgeBases(): Promise<KnowledgeBaseItem[]> {
  const { data } = await http.get<ApiResponse<KnowledgeBaseItem[]>>('/knowledge-bases')
  return data.data ?? []
}

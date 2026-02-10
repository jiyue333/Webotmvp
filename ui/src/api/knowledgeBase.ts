// 文件职责：定义知识库管理相关的 HTTP 接口（CRUD）。
// 边界：仅定义接口签名与类型；不包含状态管理逻辑。

import type { KnowledgeBaseItem } from '../types/api'

export function listKnowledgeBases(): Promise<KnowledgeBaseItem[]> {
  throw new Error('Not implemented')
}

export function getKnowledgeBase(_id: string): Promise<KnowledgeBaseItem> {
  throw new Error('Not implemented')
}

export function createKnowledgeBase(_data: any): Promise<KnowledgeBaseItem> {
  throw new Error('Not implemented')
}

export function updateKnowledgeBase(_id: string, _data: any): Promise<KnowledgeBaseItem> {
  throw new Error('Not implemented')
}

export function deleteKnowledgeBase(_id: string): Promise<void> {
  throw new Error('Not implemented')
}

// TODO(M3)：实现 listKnowledgeBases，GET /api/v1/knowledge-bases，支持 page/page_size 分页。
// TODO(M3)：实现 getKnowledgeBase，GET /api/v1/knowledge-bases/{id}，返回 KB 对象。
// TODO(M3)：实现 createKnowledgeBase，POST /api/v1/knowledge-bases，接收 name/description/embedding_model_id/chunking_config。
// TODO(M3)：实现 updateKnowledgeBase，PUT /api/v1/knowledge-bases/{id}，可选字段更新。
// TODO(M3)：实现 deleteKnowledgeBase，DELETE /api/v1/knowledge-bases/{id}，级联删除关联知识/标签。

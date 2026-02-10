// 文件职责：定义知识文档管理相关的 HTTP 接口（file/url/manual 导入、列表、详情、删除）。
// 边界：仅定义接口签名与类型；不包含状态管理逻辑。

export interface KnowledgeItem {
  id: string
  knowledge_base_id: string
  type: string
  title: string
  source: string
  parse_status: string
  enable_status: string
  file_name?: string
  file_type?: string
  file_size?: number
  tag_id?: string
  created_at?: string
  updated_at?: string
}

export const knowledgeApi = {
  list: (_kbId: string): Promise<KnowledgeItem[]> => {
    throw new Error('Not implemented')
  },
  getById: (_id: string): Promise<KnowledgeItem> => {
    throw new Error('Not implemented')
  },
  uploadFile: (_kbId: string, _file: File): Promise<KnowledgeItem> => {
    throw new Error('Not implemented')
  },
  importUrl: (_kbId: string, _url: string): Promise<KnowledgeItem> => {
    throw new Error('Not implemented')
  },
  createManual: (_kbId: string, _title: string, _content: string): Promise<KnowledgeItem> => {
    throw new Error('Not implemented')
  },
  delete: (_id: string): Promise<void> => {
    throw new Error('Not implemented')
  }
}

// TODO(M3)：实现 list，GET /api/v1/knowledge-bases/{id}/knowledge，支持 page/page_size/tag_id 筛选。
// TODO(M3)：实现 getById，GET /api/v1/knowledge/{id}，返回知识详情含 chunk_count。
// TODO(M3)：实现 uploadFile，POST /api/v1/knowledge-bases/{id}/knowledge/file，multipart 文件上传。
// TODO(M3)：实现 importUrl，POST /api/v1/knowledge-bases/{id}/knowledge/url，提交 URL 异步抓取。
// TODO(M3)：实现 createManual，POST /api/v1/knowledge-bases/{id}/knowledge/manual，手工 Markdown 录入。
// TODO(M3)：实现 delete，DELETE /api/v1/knowledge/{id}，软删除。

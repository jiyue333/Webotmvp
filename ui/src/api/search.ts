// 文件职责：封装独立检索相关 HTTP 接口（向量 + BM25 + Rerank）。
// 边界：处理 /api/v1/knowledge-search 独立检索请求；不包含对话流中的检索逻辑。

export interface SearchPayload {
  query: string
  knowledge_base_id: string
  top_k?: number
}

export interface SearchResultItem {
  chunk_id: string
  content: string
  score: number
  knowledge_id: string
  knowledge_title: string
}

export function searchKnowledge(_payload: SearchPayload): Promise<SearchResultItem[]> {
  throw new Error('Not implemented')
}

// TODO(M6)：实现 searchKnowledge，POST /api/v1/knowledge-search，返回混合检索结果列表。

# 文件职责：定义检索相关 DTO，包括内部层间传递的 RetrieveItem 和 API 响应的 SearchResultItem。约束 /knowledge-search 端点及 ChatPipeline 检索阶段的数据契约。对齐 mvp.md §4.2.9。
# 边界：只定义数据结构；检索逻辑由 RetrieverService 负责，结果组装（补查 knowledge_title）由 Service 层完成。

# TODO(M6)：定义 SearchRequest(BaseModel)，字段 query: str, knowledge_base_id: str, top_k: int = 5。

# TODO(M6)：定义 RetrieveItem(BaseModel)。Repository 层返回的轻量检索结果，只含 embeddings 表字段。
#   字段：chunk_id: str, content: str, score: float, knowledge_id: str, match_type: str（"vector" | "keywords"）。
#   用途：PostgresRetrieverRepository → HybridRetrieverService 之间的层间契约。

# TODO(M6)：定义 SearchResultItem(BaseModel)。API 响应 / ChatPipeline references 使用的完整结果。
#   字段：chunk_id: str, content: str, score: float, knowledge_id: str, knowledge_title: str。
#   组装：由 HybridRetrieverService 在 RRF 融合后，批量补查 knowledges 表获取 title，将 RetrieveItem 转换为 SearchResultItem。

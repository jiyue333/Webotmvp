# 文件职责：封装基于 PostgreSQL 的原子检索能力，提供 pgvector 向量相似度搜索和 pg_search BM25 全文检索两个独立方法。
# 边界：只负责单一类型的检索查询（vector_search 或 bm25_search）；不负责混合融合（RRF 融合由 HybridRetrieverService 在 Service 层完成）。不负责向量/文档写入（由 EmbeddingRepository 负责）。不包含重排逻辑。上游调用者为 HybridRetrieverService。
# 对标：WeKnora internal/application/repository/retriever/postgres/repository.go（Retrieve 路由 + VectorRetrieve + KeywordsRetrieve，不含 hybrid 融合）。
# 返回类型：list[RetrieveItem]（来自 schemas.search），只含 embeddings 表字段，不 JOIN knowledges 表。

# TODO(M6): 定义 PostgresRetrieverRepository 类，接收 AsyncSession。
# TODO(M6): 实现 vector_search(knowledge_base_id, query_embedding, top_k, threshold) → list[RetrieveItem]。使用 pgvector halfvec cosine 距离进行向量近邻搜索，子查询扩展 top_k*2 候选后按阈值过滤。每条结果的 match_type 设为 "vector"。
# TODO(M6): 实现 bm25_search(knowledge_base_id, query_text, top_k) → list[RetrieveItem]。使用 pg_search paradedb.match 进行 BM25 全文检索。每条结果的 match_type 设为 "keywords"。

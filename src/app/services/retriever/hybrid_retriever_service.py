# 文件职责：实现 HybridRetrieverService，编排 vector/keywords 两路检索，通过 RRF 融合结果，并批量补查 knowledge_title 组装完整的 SearchResultItem。
# 边界：仅负责检索查询、结果融合与结果组装（纯读）；不负责向量写入/删除（由 EmbeddingService 负责）。底层原子查询委托给 PostgresRetrieverRepository，knowledge_title 通过 KnowledgeRepository 批量补查。
# 对标：WeKnora knowledgebase.go HybridSearch() + processSearchResults()。Service 层编排两路查询 + RRF 融合 + 批量补查 knowledges 表组装最终结果。

# TODO(M6): 实现 HybridRetrieverService 类。注入 PostgresRetrieverRepository、KnowledgeRepository 和 ModelService。
# TODO(M6): 实现 retrieve(knowledge_base_id, query, retriever_type, top_k, threshold) → list[SearchResultItem]。
#   流程：
#   1. 根据 retriever_type 分派：vector 调 repo.vector_search()，keywords 调 repo.bm25_search()，hybrid 同时执行两路。
#   2. hybrid 模式下调用 _rrf_fusion() 融合两路 RetrieveItem 结果。
#   3. 从融合结果中收集不重复的 knowledge_id 集合。
#   4. 调用 KnowledgeRepository.get_by_ids(knowledge_ids) 批量查询 knowledges 表，获取 {id: title} 映射。
#   5. 遍历融合结果，用映射补充 knowledge_title，转换为 SearchResultItem 列表返回。
# TODO(M6): 实现 _rrf_fusion(vector_results, keyword_results, k=60) → list[RetrieveItem]。按 chunk_id 构建 rank 映射，计算 RRF score = sum(1/(k+rank))，去重后按 score 降序排序返回。

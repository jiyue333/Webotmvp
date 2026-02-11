# 文件职责：向量化写入服务，负责调用 Embedding 模型生成向量并通过 EmbeddingRepository 批量写入/删除 embeddings 表。
# 边界：仅负责向量的生成与持久化生命周期（写入/删除）；不负责检索查询（由 RetrieverService 负责）。上游由 Worker ingest 流程和 KnowledgeService 级联删除调用。
# 对标：WeKnora keywords_vector_hybrid_indexer.go 的 Index/BatchIndex/Delete 部分（MVP 将写入职责从检索服务中拆出为独立服务）。

# TODO(M5): 实现 EmbeddingService 类骨架。注入 EmbeddingRepository 和 ModelService（用于获取 Embedding 模型客户端）。
# TODO(M5): 实现 batch_embed_and_store(knowledge_base_id, chunks) 方法。调用 Embedding 模型批量向量化 chunk.content，构造 embedding 记录（含 source_id/chunk_id/knowledge_id/dimension/embedding），调用 EmbeddingRepository.bulk_create() 写入。
# TODO(M5): 实现 delete_by_knowledge_ids(knowledge_ids) 方法。调用 EmbeddingRepository.delete_by_knowledge() 物理删除对应 embeddings 记录（供知识删除时级联清理）。
# TODO(M5): 实现 delete_by_chunk_ids(chunk_ids) 方法。调用 EmbeddingRepository 按 chunk_id 列表删除 embeddings 记录（供分块重建时调用）。

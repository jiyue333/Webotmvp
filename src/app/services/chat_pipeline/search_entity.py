# 文件职责：实现 SearchEntity 插件（Graph RAG），基于抽取的实体在 Neo4j 中检索相关子图，将图节点映射回 Chunk 并合入检索结果。
# 边界：仅负责图谱检索与结果转换，不负责实体抽取（由 extract_entity.py 完成）。未启用图谱或无实体时直接跳过。
# 对标：WeKnora search_entity.go（PluginSearchEntity.OnEvent -> GraphRepository.SearchNode -> filterSeenChunk -> chunk2SearchResult）。

# TODO(M7): 实现 PluginSearchEntity 类。注册 ENTITY_SEARCH 事件，依赖 GraphRepository/ChunkRepository。
# TODO(M7): 实现并发图谱检索。按 entity_kb_ids 并行调用 GraphRepository.search_node。
# TODO(M7): 实现 filter_seen_chunk 函数。过滤已在 Chunk 检索中命中过的结果，避免重复。
# TODO(M7): 实现 chunk_to_search_result 函数。将图谱命中的 Chunk 转换为统一的 SearchResult 格式，标记 match_type=graph。

# 文件职责：实现 Search 插件，执行 Chunk 级别的混合检索（pgvector 向量 + pg_search BM25 关键词），将结果写入 ChatManage.search_result。
# 边界：仅负责 Chunk 检索逻辑（embedding 相似度 + 关键词匹配），不负责重排、合并或图谱检索。
# 对标：WeKnora search.go（PluginSearch.OnEvent -> searchByTargets -> 向量+关键词混合 -> 查询扩展 -> 历史引用补充）。

# TODO(M6): 实现 PluginSearch 类。注册 SEARCH 事件，调用 ChunkService 进行混合检索。
# TODO(M6): 实现 search_by_targets 方法。对每个 KB 执行 embedding + keyword 并行检索并合并。
# TODO(M6): 实现 expand_queries 方法。本地查询扩展（词序变换、停用词移除、关键短语提取），不依赖 LLM。
# TODO(M6): 实现 get_search_result_from_history 方法。从历史对话引用中补充检索结果。
# TODO(M6): 实现 remove_duplicate_results 方法。按 chunk_id 和内容签名去重。

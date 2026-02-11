# 文件职责：分块管理服务，负责 Chunk CRUD、批量创建/删除、按知识/知识库维度清理分块。
# 边界：编排 ChunkRepository 完成持久化；Chunk 的创建和向量化通常由 Worker 的 ingest 流程驱动，本服务主要负责元数据管理和删除时的数据清理。
# 对标：WeKnora internal/application/service/chunk.go（CreateChunks/GetChunkByID/ListChunksByKnowledgeID/DeleteChunksByKnowledgeID）。

# TODO(M5): 实现 ChunkService 类骨架。注入 ChunkRepository。
# TODO(M5): 实现 create_chunks()。批量创建分块记录（由 Worker ingest 流程调用）。
# TODO(M5): 实现 get_chunk_by_id()。按 ID 查询分块。
# TODO(M5): 实现 list_chunks_by_knowledge_id()。按知识 ID 查询分块列表（支持分页）。
# TODO(M5): 实现 delete_chunks_by_knowledge_id()。按知识 ID 删除所有分块（级联删除场景）。
# TODO(M5): 实现 delete_chunks()。按 ID 列表批量删除分块。

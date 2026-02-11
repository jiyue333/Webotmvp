# 文件职责：知识条目管理服务，负责知识创建（file/url/manual）、状态流转（pending→processing→completed/failed）、file_hash 去重、异步任务投递。
# 边界：编排 KnowledgeRepository 完成持久化，通过 Redis Stream XADD 投递异步处理任务；KB 信息（存在性校验、chunking_config）通过 KnowledgeBaseRepository 只读获取，不依赖 KnowledgeBaseService，避免循环依赖。
# 对标：WeKnora internal/application/service/knowledge.go（CreateKnowledgeFromFile/CreateKnowledgeFromURL/CreateKnowledgeFromManual/GetKnowledgeByID/ListKnowledge/DeleteKnowledge）。

# TODO(M3): 实现 KnowledgeService 类骨架。注入 KnowledgeRepository、KnowledgeBaseRepository（只读，用于校验 KB 存在性和获取 chunking_config）、RedisClient（用于 XADD 投递任务）。
# TODO(M3): 实现 create_from_file()。校验文件类型，计算 SHA-256 哈希去重，创建 knowledge 记录（parse_status=pending），保存文件到存储，事务外投递 Redis Stream 任务。
# TODO(M3): 实现 create_from_url()。校验 URL 格式，URL 哈希去重，创建 knowledge 记录，事务外投递 Redis Stream 任务。
# TODO(M3): 实现 create_from_manual()。校验标题和内容，创建 knowledge 记录（type=manual），投递处理任务。
# TODO(M3): 实现 get_knowledge_by_id()。按 ID 查询知识详情，含 chunk_count 统计。
# TODO(M3): 实现 list_knowledge()。分页查询，支持按 tag_id 筛选。
# TODO(M3): 实现 delete_knowledge()。软删除知识记录，异步清理 chunks/embeddings/neo4j 关联数据。
# TODO(M3): 实现 delete_by_kb_id()。按知识库 ID 批量删除所有知识记录及关联数据（供 KnowledgeBaseService 级联删除调用）。
# TODO(M5): 实现 update_parse_status()。供 Worker 回调更新解析状态（processing/completed/failed）和错误信息。

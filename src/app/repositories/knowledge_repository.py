# 文件职责：封装 knowledges 表的数据访问操作，提供知识条目 CRUD、按知识库筛选、状态流转更新、file_hash 去重查询等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 knowledges 表。
# 边界：只负责 knowledges 表的持久化读写；文件上传存储由 infra/storage 负责，解析状态机流转的业务规则由 KnowledgeService 负责。查询自动过滤 deleted_at IS NULL。上游调用者为 KnowledgeService、Worker。

# TODO(M3)：定义 KnowledgeRepository(SoftDeleteRepository) 类，绑定 Knowledge ORM 模型。
# TODO(M3)：实现 list_by_kb(knowledge_base_id, tag_id, page, page_size) 方法。支持 tag_id 筛选和分页。
# TODO(M3)：实现 check_file_hash(knowledge_base_id, file_hash) 方法。部分唯一索引检查，同知识库下未删除记录不允许哈希重复。
# TODO(M5)：实现 update_parse_status(knowledge_id, status, error_message) 方法。Worker 调用，更新解析状态和失败原因。
# TODO(M5)：实现 list_pending(limit) 方法。Worker 定期扫描 parse_status='pending' 的超时记录用于兜底补偿投递。
# TODO(M6)：实现 get_by_ids(knowledge_ids) → dict[str, Knowledge] 方法。按 ID 列表批量查询知识记录，返回 {id: Knowledge} 映射。供 HybridRetrieverService 批量补查 knowledge_title 使用。

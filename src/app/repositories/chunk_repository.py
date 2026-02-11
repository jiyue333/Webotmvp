# 文件职责：封装 chunks 表的数据访问操作，提供分块批量写入、按知识/知识库查询、分块链表维护等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 chunks 表。
# 边界：只负责 chunks 表的持久化读写；分块算法由 docparser/ChunkService 负责，本层只负责结果落库。查询自动过滤 deleted_at IS NULL。上游调用者为 ChunkService、Worker。

# TODO(M5)：定义 ChunkRepository(SoftDeleteRepository) 类，绑定 Chunk ORM 模型。
# TODO(M5)：实现 bulk_create(chunks) 方法。批量写入分块记录，设置 pre_chunk_id/next_chunk_id 双向链表关系。
# TODO(M5)：实现 list_by_knowledge(knowledge_id) 方法。按 chunk_index 排序返回指定知识的所有分块。
# TODO(M5)：实现 delete_by_knowledge(knowledge_id) 方法。软删除指定知识的所有分块（调用 soft_delete），用于知识重解析或删除。
# TODO(M6)：实现 get_by_ids(chunk_ids) 方法。根据检索返回的 chunk_id 列表获取分块详情，用于引用回传。

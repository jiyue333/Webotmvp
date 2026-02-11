# 文件职责：封装 embeddings 表的数据访问操作，提供向量批量写入、按知识库/知识删除等方法。继承 CrudRepository（非 SoftDeleteRepository，因 embeddings 表无 deleted_at 列，生命周期跟随 chunk 物理删除）。对齐 mvp.md §4.5.2 embeddings 表。
# 边界：只负责 embeddings 表的持久化读写；向量生成（调用 Embedding 模型）由 EmbeddingService 负责。向量检索（pgvector 相似度查询）属于 retriever/ 子模块职责，不在此处。删除语义为物理删除。上游调用者为 EmbeddingService、Worker。

# TODO(M5)：定义 EmbeddingRepository(CrudRepository) 类，绑定 Embedding ORM 模型。
# TODO(M5)：实现 bulk_create(embeddings) 方法。批量写入向量记录，包含 source_id/embedding/content/dimension 等字段。
# TODO(M5)：实现 delete_by_knowledge(knowledge_id) 方法。物理删除指定知识的所有向量记录（调用 hard_delete），用于知识重解析或删除。
# TODO(M5)：实现 update_enabled_by_kb(knowledge_base_id, is_enabled) 方法。批量启用/禁用指定知识库的向量记录。

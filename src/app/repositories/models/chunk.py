# 文件职责：定义 Chunk ORM 模型，映射 chunks 表。字段包括 id/knowledge_base_id/knowledge_id/content/chunk_index/chunk_type/is_enabled/start_at/end_at/链表指针/tag_id/时间戳/软删除。对齐 mvp.md §4.5.2 chunks 表结构。
# 边界：只定义表映射和字段约束；分块算法（分割策略、偏移计算）由 docparser 模块负责。

# TODO(M5)：定义 Chunk(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'chunks'。
# TODO(M5)：定义字段 knowledge_base_id(VARCHAR(36), not null), knowledge_id(VARCHAR(36), not null), content(Text, not null), chunk_index(Integer, not null), chunk_type(VARCHAR(20), default='text'), is_enabled(Boolean, default=True)。
# TODO(M5)：定义偏移字段 start_at(Integer, not null), end_at(Integer, not null)。链表字段 pre_chunk_id(VARCHAR(36)), next_chunk_id(VARCHAR(36)), parent_chunk_id(VARCHAR(36))。tag_id(VARCHAR(36))。
# TODO(M5)：定义索引 idx_chunks_knowledge(knowledge_id), idx_chunks_kb(knowledge_base_id)。
# TODO(M5)：定义 relationship('Knowledge', back_populates='chunks') 和 relationship('Embedding', back_populates='chunk', uselist=False)。

# 文件职责：定义 Embedding ORM 模型，映射 embeddings 表。字段包括 id(SERIAL)/source_id/source_type/chunk_id/knowledge_id/knowledge_base_id/content/dimension/embedding(HALFVEC)/is_enabled/tag_id/时间戳。对齐 mvp.md §4.5.2 embeddings 表结构。
# 边界：只定义表映射和字段约束；pgvector HALFVEC 类型需要 pgvector SQLAlchemy 扩展支持。HNSW 索引和 BM25 全文索引在 Alembic 迁移中创建，不在模型中声明。

# TODO(M5)：定义 Embedding(Base, TimestampMixin) 类，__tablename__ = 'embeddings'。注意 id 使用 SERIAL 自增，非 UUID。
# TODO(M5)：定义字段 source_id(VARCHAR(64), not null), source_type(Integer, not null), chunk_id(VARCHAR(64)), knowledge_id(VARCHAR(64)), knowledge_base_id(VARCHAR(64)), content(Text), dimension(Integer, not null), embedding(HALFVEC), is_enabled(Boolean, default=True), tag_id(VARCHAR(36))。
# TODO(M5)：定义唯一约束 UNIQUE(source_id, source_type)。索引 idx_embeddings_kb(knowledge_base_id)。
# TODO(M5)：定义 relationship('Chunk', back_populates='embedding')。

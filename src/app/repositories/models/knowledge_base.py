# 文件职责：定义 KnowledgeBase ORM 模型，映射 knowledge_bases 表。字段包括 id/name/description/embedding_model_id/chunking_config(JSONB)/created_by/时间戳/软删除。对齐 mvp.md §4.5.2 knowledge_bases 表结构。
# 边界：只定义表映射和字段约束；chunking_config 默认值 {chunk_size:512, chunk_overlap:50, split_markers:["\n\n","\n","。"], keep_separator:true} 在模型或 schema 层设置。

# TODO(M3)：定义 KnowledgeBase(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'knowledge_bases'。
# TODO(M3)：定义字段 name(VARCHAR(255), not null), description(Text), embedding_model_id(VARCHAR(64), not null), chunking_config(JSONB, not null, default=默认分块配置), created_by(VARCHAR(36), not null)。
# TODO(M3)：定义 relationship('Knowledge', back_populates='knowledge_base') 和 relationship('KnowledgeTag', back_populates='knowledge_base')。

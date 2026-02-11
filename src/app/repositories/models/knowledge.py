# 文件职责：定义 Knowledge ORM 模型，映射 knowledges 表。字段包括 id/knowledge_base_id/type/title/source/parse_status/enable_status/文件相关字段/tag_id/error_message/metadata(JSONB)/时间戳/软删除。对齐 mvp.md §4.5.2 knowledges 表结构。
# 边界：只定义表映射和字段约束；parse_status 状态机流转（pending→processing→completed/failed）的业务规则由 KnowledgeService 保障。

# TODO(M3)：定义 Knowledge(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'knowledges'。
# TODO(M3)：定义字段 knowledge_base_id(VARCHAR(36), not null), type(VARCHAR(50), not null), title(VARCHAR(255), not null), source(VARCHAR(128), not null), parse_status(VARCHAR(50), default='pending'), enable_status(VARCHAR(50), default='enabled')。
# TODO(M3)：定义文件相关字段 file_name(VARCHAR(255)), file_type(VARCHAR(50)), file_size(BIGINT), file_path(Text), file_hash(VARCHAR(64)), tag_id(VARCHAR(36)), error_message(Text), metadata(JSONB), created_by(VARCHAR(36), not null), processed_at(TIMESTAMPTZ)。
# TODO(M3)：定义索引 idx_knowledges_kb(knowledge_base_id), idx_knowledges_status(parse_status)。部分唯一索引 UNIQUE(knowledge_base_id, file_hash) WHERE deleted_at IS NULL。
# TODO(M3)：定义 relationship('KnowledgeBase', back_populates='knowledges') 和 relationship('Chunk', back_populates='knowledge')。

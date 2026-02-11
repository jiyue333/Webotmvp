# 文件职责：定义 Message ORM 模型，映射 messages 表。字段包括 id/request_id/session_id/role/content/knowledge_references(JSONB)/is_completed/时间戳/软删除。对齐 mvp.md §4.5.2 messages 表结构。
# 边界：只定义表映射和字段约束；knowledge_references JSONB 的内容结构由 ChatPipeline 产出，此处不做内容校验。

# TODO(M4)：定义 Message(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'messages'。
# TODO(M4)：定义字段 request_id(VARCHAR(36), not null), session_id(VARCHAR(36), not null), role(VARCHAR(50), not null), content(Text, not null), knowledge_references(JSONB, default='[]'), is_completed(Boolean, default=False)。
# TODO(M4)：定义索引 idx_messages_session(session_id)。
# TODO(M4)：定义 relationship('Session', back_populates='messages')。

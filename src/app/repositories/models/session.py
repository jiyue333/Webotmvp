# 文件职责：定义 Session ORM 模型，映射 sessions 表。字段包括 id/title/knowledge_base_id/created_by/时间戳/软删除。对齐 mvp.md §4.5.2 sessions 表结构。
# 边界：只定义表映射和字段约束；会话的检索参数从知识库继承或使用全局默认值，不在 sessions 表中存储（MVP 精简设计）。

# TODO(M4)：定义 Session(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'sessions'。
# TODO(M4)：定义字段 title(VARCHAR(255)), knowledge_base_id(VARCHAR(36)), created_by(VARCHAR(36), not null)。
# TODO(M4)：定义 relationship('Message', back_populates='session', cascade='all, delete-orphan')。

# 文件职责：定义 KnowledgeTag ORM 模型，映射 knowledge_tags 表。字段包括 id/knowledge_base_id/name/color/sort_order/时间戳/软删除。对齐 mvp.md §4.5.2 knowledge_tags 表结构。
# 边界：只定义表映射和字段约束；删除标签后置空关联知识 tag_id 的逻辑由 service 层编排。

# TODO(M3)：定义 KnowledgeTag(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'knowledge_tags'。
# TODO(M3)：定义字段 knowledge_base_id(VARCHAR(36), not null), name(VARCHAR(128), not null), color(VARCHAR(32)), sort_order(Integer, default=0)。
# TODO(M3)：定义部分唯一索引 UNIQUE(knowledge_base_id, name) WHERE deleted_at IS NULL。
# TODO(M3)：定义 relationship('KnowledgeBase', back_populates='knowledge_tags')。

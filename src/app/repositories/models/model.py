# 文件职责：定义 Model ORM 模型，映射 models 表。字段包括 id/name/type/source/description/parameters(JSONB)/is_default/status/created_by/时间戳/软删除。对齐 mvp.md §4.5.2 models 表结构。
# 边界：只定义表映射和字段约束；parameters JSONB 的内容校验（api_key/base_url 等）由 schema 层负责。

# TODO(M3)：定义 Model(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'models'。
# TODO(M3)：定义字段 name(VARCHAR(255), not null), type(VARCHAR(50), not null), source(VARCHAR(50), not null), description(Text), parameters(JSONB, not null), is_default(Boolean, default=False), status(VARCHAR(50), default='active'), created_by(VARCHAR(36), not null)。
# TODO(M3)：定义索引 idx_models_type(type), idx_models_source(source)。

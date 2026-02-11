# 文件职责：定义 AuthToken ORM 模型，映射 auth_tokens 表。字段包括 id/user_id/token/token_type/expires_at/is_revoked/created_at。对齐 mvp.md §4.5.2 auth_tokens 表结构。
# 边界：只定义表映射和字段约束；token 的签发与验证逻辑在 AuthService 中实现。

# TODO(M2)：定义 AuthToken(Base, UUIDPrimaryKeyMixin) 类，__tablename__ = 'auth_tokens'。
# TODO(M2)：定义字段 user_id(VARCHAR(36), ForeignKey('users.id', ondelete='CASCADE'), not null), token(Text, not null), token_type(VARCHAR(50), not null), expires_at(TIMESTAMPTZ, not null), is_revoked(Boolean, default=False), created_at(TIMESTAMPTZ)。
# TODO(M2)：定义索引 idx_auth_tokens_user_id(user_id), idx_auth_tokens_expires(expires_at)。
# TODO(M2)：定义 relationship('User', back_populates='auth_tokens')。

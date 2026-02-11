# 文件职责：定义 User ORM 模型，映射 users 表。字段包括 id/username/email/password_hash/is_active/时间戳/软删除。对齐 mvp.md §4.5.2 users 表结构。
# 边界：只定义表映射和字段约束（UNIQUE/NOT NULL）；密码加密由 service 层处理，不在模型中操作。

# TODO(M2)：定义 User(Base, UUIDPrimaryKeyMixin, TimestampMixin, SoftDeleteMixin) 类，__tablename__ = 'users'。
# TODO(M2)：定义字段 username(VARCHAR(100), unique, not null), email(VARCHAR(255), unique, not null), password_hash(VARCHAR(255), not null), is_active(Boolean, default=True)。
# TODO(M2)：定义 relationship('AuthToken', back_populates='user', cascade='all, delete-orphan')。

# 文件职责：封装 users 表的数据访问操作，提供按 id/username/email 查询用户、创建用户等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 users 表。
# 边界：只负责 users 表的持久化读写；密码哈希验证由 AuthService 负责，不在此处处理。查询自动过滤 deleted_at IS NULL。上游调用者为 UserService/AuthService。

# TODO(M2)：定义 UserRepository(SoftDeleteRepository) 类，绑定 User ORM 模型。
# TODO(M2)：实现 get_by_email(email) 方法。用于登录时查询用户，自动过滤软删除。
# TODO(M2)：实现 get_by_username(username) 方法。用于注册时检查用户名重复。
# TODO(M2)：实现 create_user(username, email, password_hash) 方法。创建用户记录。

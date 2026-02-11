# 文件职责：封装 auth_tokens 表的数据访问操作，提供 token 创建、查询、撤销、清理过期 token 等方法。继承 CrudRepository（非 SoftDeleteRepository，因 auth_tokens 表无 deleted_at 列）。对齐 mvp.md §4.5.2 auth_tokens 表。
# 边界：只负责 auth_tokens 表的持久化读写；token 签发（JWT 编码）和验证逻辑由 AuthService 负责。删除语义为物理删除或标记 is_revoked，不使用软删除。上游调用者为 AuthService。

# TODO(M2)：定义 AuthTokenRepository(CrudRepository) 类，绑定 AuthToken ORM 模型。
# TODO(M2)：实现 create_token(user_id, token, token_type, expires_at) 方法。持久化新 token 记录。
# TODO(M2)：实现 get_valid_token(token) 方法。查询未撤销且未过期的 token，用于鉴权中间件校验。
# TODO(M2)：实现 revoke_token(token) 方法。将指定 token 的 is_revoked 设为 true，用于登出。
# TODO(M2)：实现 revoke_all_user_tokens(user_id) 方法。撤销用户的所有有效 token。
# TODO(M8)：实现 cleanup_expired_tokens() 方法。物理删除已过期的 token 记录（调用 hard_delete），减少表膨胀。

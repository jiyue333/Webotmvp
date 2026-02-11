# 文件职责：封装 sessions 表的数据访问操作，提供会话 CRUD、按用户查询、按知识库筛选等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 sessions 表。
# 边界：只负责 sessions 表的持久化读写；会话级别的停止/续流控制由 SessionService + StreamManager 协调。查询自动过滤 deleted_at IS NULL。上游调用者为 SessionService。

# TODO(M4)：定义 SessionRepository(SoftDeleteRepository) 类，绑定 Session ORM 模型。
# TODO(M4)：实现 list_by_user(created_by) 方法。按 updated_at 倒序返回用户的会话列表。
# TODO(M4)：实现 get_with_kb(session_id) 方法。查询会话详情并关联加载绑定的知识库信息。

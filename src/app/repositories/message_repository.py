# 文件职责：封装 messages 表的数据访问操作，提供消息创建、历史加载（向上翻页）、更新 assistant 消息内容等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 messages 表。
# 边界：只负责 messages 表的持久化读写；消息内容的流式组装由 ChatPipeline 负责，knowledge_references JSON 字段由 Pipeline 结果填充。查询自动过滤 deleted_at IS NULL。上游调用者为 MessageService、ChatPipeline。

# TODO(M4)：定义 MessageRepository(SoftDeleteRepository) 类，绑定 Message ORM 模型。
# TODO(M4)：实现 create_pair(session_id, request_id, user_content) 方法。单事务内同时创建 user 消息和 assistant 占位消息。
# TODO(M4)：实现 load_history(session_id, before_id, limit) 方法。按 created_at 倒序加载消息，支持 before_id 游标分页。
# TODO(M4)：实现 update_assistant_message(message_id, content, references, is_completed) 方法。流式完成后更新 assistant 消息。
# TODO(M4)：实现 list_recent(session_id, limit) 方法。获取最近 N 条消息，用于 Pipeline 的 LoadHistory 步骤。

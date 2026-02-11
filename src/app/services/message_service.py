# 文件职责：消息管理服务，负责消息 CRUD、会话消息历史加载（向上翻页 before_id 分页）、assistant 消息内容与完成状态更新。
# 边界：编排 MessageRepository 完成持久化，消息创建前校验 Session 存在性；不处理 SSE 推送。
# 对标：WeKnora internal/application/service/message.go（CreateMessage/GetMessage/GetMessagesBySession/UpdateMessage/DeleteMessage）。

# TODO(M4): 实现 MessageService 类骨架。注入 MessageRepository、SessionRepository。
# TODO(M4): 实现 create_message()。创建消息记录，校验 session_id 有效性。
# TODO(M4): 实现 load_messages()。按 session_id 加载消息历史，支持 before_id + limit 向上翻页。
# TODO(M4): 实现 update_message()。更新消息内容和 is_completed 状态（供 ChatService 流式完成后回写）。
# TODO(M4): 实现 get_recent_messages()。获取最近 N 条消息（供 Pipeline LoadHistory 步骤使用）。

# 文件职责：会话生命周期管理服务，负责 Session CRUD、删除时级联清理消息和 Redis 上下文缓存。
# 边界：编排 SessionRepository 完成持久化；级联删除消息时依赖 MessageService（写操作走 Service 层，保证消息删除逻辑只维护一处）；不负责 RAG 编排（由 ChatService 负责）。
# 对标：WeKnora internal/application/service/session.go（CreateSession/GetSession/UpdateSession/DeleteSession/GenerateTitle 部分）。

# TODO(M4): 实现 SessionService 类骨架。注入 SessionRepository、MessageService、ContextManager（Redis）、ModelService（标题生成用）。
# TODO(M4): 实现 create_session()。创建会话记录，绑定 knowledge_base_id 和 created_by。
# TODO(M4): 实现 get_session()。按 ID 查询会话详情。
# TODO(M4): 实现 list_sessions()。查询当前用户的会话列表（按 updated_at 倒序）。
# TODO(M4): 实现 update_session()。更新会话标题等可选字段。
# TODO(M4): 实现 delete_session()。软删除会话，通过 MessageService 级联删除关联消息，清理 ContextManager 中的 Redis 上下文缓存。
# TODO(M4): 实现 generate_title_async()。异步调用 ModelService 获取 Chat 模型为会话生成标题（首次用户发问后触发）。

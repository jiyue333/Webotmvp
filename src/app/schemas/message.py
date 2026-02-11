# 文件职责：定义消息相关 DTO（详情/列表项/加载查询参数），约束 /messages/* 端点的响应类型。对齐 mvp.md §4.2.7。
# 边界：只定义数据结构；消息创建由 ChatService 内部完成（user + assistant 占位同事务），不暴露独立创建接口。

# TODO(M4)：定义 MessageDetail(BaseModel)，包含 id / session_id / role / content / knowledge_references: list / is_completed: bool / created_at。
# TODO(M4)：定义 MessageLoadQuery(BaseModel)，字段 before_id: str | None, limit: int = 20，用于向上翻页加载。

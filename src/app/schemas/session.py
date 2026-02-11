# 文件职责：定义会话管理相关 DTO（创建/更新/详情/列表），约束 /sessions/* 端点的请求与响应类型。对齐 mvp.md §4.2.6。
# 边界：只定义数据结构与校验规则；会话生命周期（stop/continue-stream）由 handler/service 层处理。

# TODO(M4)：定义 SessionCreate(BaseModel)，字段 knowledge_base_id: str, title: str | None。
# TODO(M4)：定义 SessionUpdate(BaseModel)，字段 title: str | None。
# TODO(M4)：定义 SessionDetail(BaseModel)，包含 id / title / knowledge_base_id / created_at / updated_at。

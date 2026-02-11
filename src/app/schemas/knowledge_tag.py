# 文件职责：定义知识标签相关 DTO（创建/更新/详情），约束 /knowledge-bases/{id}/tags/* 端点的请求与响应类型。对齐 mvp.md §4.2.4。
# 边界：只定义数据结构与校验规则；标签唯一性验证由 Service 层负责。

# TODO(M3)：定义 TagCreate(BaseModel)，字段 name: str, color: str | None, sort_order: int = 0。
# TODO(M3)：定义 TagUpdate(BaseModel)，所有字段可选。
# TODO(M3)：定义 TagDetail(BaseModel)，包含 id / knowledge_base_id / name / color / sort_order / created_at / updated_at。

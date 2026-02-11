# 文件职责：定义知识条目相关 DTO（文件/URL/手工导入请求、详情、列表项、查询参数），约束 /knowledge-bases/{id}/knowledge/* 端点的请求与响应类型。对齐 mvp.md §4.2.5。
# 边界：只定义数据结构与校验规则；文件上传校验（类型/大小）由 handler 层处理，解析状态流转由 KnowledgeService 负责。

# TODO(M3)：定义 KnowledgeURLImport(BaseModel)，字段 url: HttpUrl。
# TODO(M3)：定义 KnowledgeManualImport(BaseModel)，字段 title: str, content: str。
# TODO(M3)：定义 KnowledgeDetail(BaseModel)，包含 id / knowledge_base_id / type / title / source / parse_status / enable_status / file_name / file_type / file_size / tag_id / created_at / updated_at / chunk_count（详情接口额外计算）。
# TODO(M3)：定义 KnowledgeListItem(BaseModel)，列表项响应（不含 chunk_count）。
# TODO(M3)：定义 KnowledgeQuery(BaseModel)，可选字段 page / page_size / tag_id，用于列表筛选。

# 文件职责：定义知识库管理相关 DTO（创建/更新/详情/列表），约束 /knowledge-bases/* 端点的请求与响应类型。对齐 mvp.md §4.2.3。
# 边界：只定义数据结构与校验规则；不包含知识库业务逻辑（由 KBService 负责），chunking_config 仅提供默认值和结构约束。

# TODO(M3)：定义 ChunkingConfig(BaseModel)，字段 chunk_size: int = 512, chunk_overlap: int = 50, split_markers: list[str], keep_separator: bool = True。
# TODO(M3)：定义 KBCreate(BaseModel)，字段 name: str, description: str | None, embedding_model_id: str, chunking_config: ChunkingConfig | None（使用默认值）。
# TODO(M3)：定义 KBUpdate(BaseModel)，所有字段可选。
# TODO(M3)：定义 KBDetail(BaseModel)，包含 id / name / description / embedding_model_id / chunking_config / created_at / updated_at。

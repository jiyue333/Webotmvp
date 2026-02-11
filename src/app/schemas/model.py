# 文件职责：定义模型管理相关 DTO（创建/更新/详情/列表/筛选），约束 /models/* 端点的请求与响应类型。对齐 mvp.md §4.2.2。
# 边界：只定义数据结构与校验规则；不包含模型调用逻辑，不处理 api_key 加解密（由 Service 层负责）。

# TODO(M3)：定义 ModelCreate(BaseModel)，字段 name: str, type: Literal["llm","embedding","rerank"], source: str, parameters: dict, is_default: bool = False, description: str | None。
# TODO(M3)：定义 ModelUpdate(BaseModel)，所有字段可选。
# TODO(M3)：定义 ModelDetail(BaseModel)，包含 id / name / type / source / description / parameters / is_default / status / created_at / updated_at。parameters 中 api_key 需脱敏。
# TODO(M3)：定义 ModelQuery(BaseModel)，可选字段 type / source，用于列表筛选。
# TODO(M3)：定义 ProviderItem(BaseModel)，字段 provider: str, display_name: str, default_base_url: str，用于厂商列表响应。

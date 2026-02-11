# 文件职责：封装 models 表的数据访问操作，提供模型 CRUD、按 type/source 筛选、默认模型查询等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 models 表。
# 边界：只负责 models 表的持久化读写；模型可用性校验和业务规则（如删除被引用模型的限制）由 ModelService 负责。查询自动过滤 deleted_at IS NULL。上游调用者为 ModelService。

# TODO(M3)：定义 ModelRepository(SoftDeleteRepository) 类，绑定 Model ORM 模型。
# TODO(M3)：实现 list_by_filter(type, source) 方法。支持按 type（llm/embedding/rerank）和 source 筛选，自动过滤软删除。
# TODO(M3)：实现 get_default_model(type) 方法。查询指定类型下 is_default=true 的模型。
# TODO(M3)：实现 check_referenced(model_id) 方法。检查模型是否被 knowledge_bases.embedding_model_id 引用，返回布尔值。

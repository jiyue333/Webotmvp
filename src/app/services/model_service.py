# 文件职责：AI 模型配置与管理服务，负责模型 CRUD、provider 列表查询、模型实例工厂（Chat/Embedding/Rerank 客户端创建）。
# 边界：编排 ModelRepository 完成持久化，通过模型配置创建 AI 客户端实例；不处理 Ollama 本地下载（MVP 仅远程模型）。
# 对标：WeKnora internal/application/service/model.go（CreateModel/GetModelByID/ListModels/UpdateModel/DeleteModel/GetChatModel/GetEmbeddingModel/GetRerankModel）。

# TODO(M3): 实现 ModelService 类骨架。注入 ModelRepository。
# TODO(M3): 实现 get_providers()。返回内置 provider 列表（openai/ollama/azure 等），含 display_name 和 default_base_url。
# TODO(M3): 实现 create_model()。创建模型记录，远程模型直接设为 active 状态。
# TODO(M3): 实现 get_model_by_id()。按 ID 查询模型，校验状态。
# TODO(M3): 实现 list_models()。支持按 type 和 source 筛选。
# TODO(M3): 实现 update_model()。更新模型配置。
# TODO(M3): 实现 delete_model()。删除前检查是否被 knowledge_base 引用（embedding_model_id）。
# TODO(M4): 实现 get_chat_model()。根据模型配置创建 Chat 客户端实例。
# TODO(M5): 实现 get_embedding_model()。根据模型配置创建 Embedding 客户端实例。
# TODO(M6): 实现 get_rerank_model()。根据模型配置创建 Rerank 客户端实例。

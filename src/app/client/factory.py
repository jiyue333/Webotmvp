# 文件职责：统一的 client 工厂入口，根据能力类型和配置创建对应的客户端实例。
# 边界：仅负责路由分发与实例创建；具体客户端实现在各自文件中定义。不包含业务逻辑。
# 对齐来源：WeKnora internal/models/chat/chat.go NewChat, embedding/embedder.go NewEmbedder, rerank/reranker.go NewReranker。

# TODO(M4)：定义 ClientCapability 枚举（llm / embedding / rerank / ocr）。
# TODO(M4)：实现 create_client(capability, config) -> AnyClient 统一工厂入口。
#   - 内部根据 capability 分发到 _create_llm_client / _create_embedding_client / _create_rerank_client / _create_ocr_client。
#   - 各内部工厂根据 config.source 路由到具体实现类（如 OpenAICompatibleLLMClient）。
#   - 未知 source 回退到 OpenAI 兼容实现（与 WeKnora 行为一致）。
# TODO(M4)：异常统一抛出 common/exceptions.py 中定义的 ClientError（AppError 子类），供 service 层捕获。
# TODO(M4+)：当 source 数量增长后，评估是否抽取 registry 模式（provider 注册表），避免工厂函数膨胀。

# 文件职责：封装 Embedding 模型的调用客户端，提供单条与批量文本向量化能力。
# 边界：仅负责 HTTP 请求发送与响应解析；不编排业务流程，不读写数据库。模型配置由调用方传入。
# 对齐来源：WeKnora internal/models/embedding/embedder.go（Embedder 接口 + NewEmbedder 工厂）。

# TODO(M5)：定义 EmbeddingClient Protocol（继承 BaseModelClient），包含：
#   - get_dimensions() -> int
#   - async embed(text: str) -> list[float]
#   - async batch_embed(texts: list[str]) -> list[list[float]]
# TODO(M5)：实现 OpenAICompatibleEmbeddingClient 类，对接 OpenAI 兼容 Embedding API。入参 ModelClientConfig，使用 httpx.AsyncClient。
# TODO(M5)：实现 batch_embed 的并发分批策略（pool），避免单次请求文本数过多。对齐 WeKnora embedding/batch.go BatchEmbedWithPool。

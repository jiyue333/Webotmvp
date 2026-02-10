# 文件职责：封装 Rerank 模型的调用客户端，提供文档重排打分能力。
# 边界：仅负责 HTTP 请求发送与响应解析；不编排业务流程，不读写数据库。模型配置由调用方传入。
# 对齐来源：WeKnora internal/models/rerank/reranker.go（Reranker 接口 + NewReranker 工厂）。

# TODO(M6)：定义 RerankClient Protocol（继承 BaseModelClient），包含：
#   - async rerank(query: str, documents: list[str], *, top_n: int | None) -> list[RankResult]
# TODO(M6)：实现 OpenAICompatibleRerankClient 类，对接 Jina/Cohere 等兼容 Rerank API。入参 ModelClientConfig，使用 httpx.AsyncClient。
# TODO(M6)：处理 relevance_score vs score 字段兼容（不同 source 返回字段名不同）。对齐 WeKnora RankResult.UnmarshalJSON。

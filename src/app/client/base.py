# 文件职责：定义 client 层的公共协议（Protocol）与数据结构，为 LLM/Embedding/Rerank/OCR 客户端提供统一抽象。
# 边界：仅定义接口契约与数据类型；不包含具体实现逻辑，不依赖第三方 SDK。
# 对齐来源：WeKnora internal/models/ 下各模型接口的公共方法签名（GetModelName / GetModelID）。

# TODO(M4)：定义 ModelClientConfig dataclass（frozen=True），字段包括 model_id, source, base_url, api_key, model_name, extra。
#   - source 对应 DB models.source（openai/ollama/azure/...），工厂路由基于此字段分发。
#   - 注意：WeKnora 原设计将 Source（local/remote）与 Provider（厂商）分为两级路由，MVP 已扁平化为单一 source。
# TODO(M4)：定义 BaseModelClient Protocol（runtime_checkable），包含 get_model_name() -> str, get_model_id() -> str。
# TODO(M4)：定义 ChatMessage dataclass（role: str, content: str），对齐 WeKnora internal/models/chat/chat.go Message。
# TODO(M4)：定义 ChatResponse dataclass（content, finish_reason, usage），对齐 WeKnora types.ChatResponse。
# TODO(M4)：定义 StreamChunk dataclass（delta, done, finish_reason），对齐 WeKnora types.StreamResponse。
# TODO(M6)：定义 RankResult dataclass（index, text, relevance_score），对齐 WeKnora rerank.RankResult。

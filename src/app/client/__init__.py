# 文件职责：client 包入口；统一导出公共协议与数据结构，供 service 层导入使用。
# 边界：仅做 re-export，不包含实现逻辑。

# TODO(M4)：从 base.py 导出 BaseModelClient, ModelClientConfig, ChatMessage, ChatResponse, StreamChunk。
# TODO(M4)：从 factory.py 导出 ClientCapability, create_client。
# TODO(M4)：从 llm_client.py 导出 LLMClient 协议。
# TODO(M5)：从 embedding_client.py 导出 EmbeddingClient 协议。
# TODO(M5)：从 ocr_client.py 导出 OCRClient 协议。
# TODO(M6)：从 rerank_client.py 导出 RerankClient 协议。

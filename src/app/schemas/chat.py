# 文件职责：定义对话请求和 SSE 事件相关 DTO，约束 /knowledge-chat/{session_id} 端点的请求类型和 SSE 推送格式。对齐 mvp.md §4.2.8 和 §4.3.4。
# 边界：只定义数据结构；流式编排逻辑由 ChatService / Pipeline 负责，SSE 传输由 handler 层负责。

# TODO(M4)：定义 ChatRequest(BaseModel)，字段 query: str, temperature: float | None。
# TODO(M4)：定义 KnowledgeReference(BaseModel)，字段 chunk_id: str, knowledge_id: str, knowledge_title: str, content: str, score: float。
# TODO(M4)：定义 SSEEvent(BaseModel)，字段 id: str, response_type: Literal["references","answer","error"], content: str, done: bool, knowledge_references: list[KnowledgeReference]。

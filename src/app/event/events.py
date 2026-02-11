# 文件职责：定义 EventType 枚举常量和 Event 数据类，以及各阶段事件附带的数据结构（QueryData / RetrievalData / ChatData 等）。对齐 WeKnora internal/event/event_data.go。
# 边界：仅声明类型与数据结构；不包含发布/订阅逻辑（由 event_bus.py 负责），不依赖 infra 层。MVP 去除 Agent 相关事件类型。

# TODO(M4)：定义 EventType(str, Enum) 枚举。包含 query.received / query.rewrite / chat.start / chat.stream / chat.complete / error / stop / session_title 等。不包含 agent.* 相关事件。
# TODO(M4)：定义 Event 数据类（dataclass 或 Pydantic BaseModel）。字段：id(str) / type(EventType) / session_id(str) / data(Any) / metadata(dict) / request_id(str)。
# TODO(M6)：定义 RetrievalData 数据类。字段：query / knowledge_base_id / method / result_count / duration_ms。
# TODO(M6)：定义 RerankData 数据类。字段：query / input_count / output_count / threshold / duration_ms。
# TODO(M6)：定义 ChatData 数据类。字段：query / model_id / content / token_count / duration_ms / is_stream。
# TODO(M7)：定义 EntitySearchData 数据类。字段：query / entity_count / relation_count / duration_ms。用于图谱检索事件。

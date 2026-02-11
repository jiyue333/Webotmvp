# 文件职责：提供 JSON 序列化辅助工具函数，处理 Pydantic 模型、datetime、UUID 等非标准类型的 JSON 编码。对齐 WeKnora internal/utils/json.go。
# 边界：只提供序列化/反序列化工具函数；不依赖 ORM 模型（由 repository 层负责），不处理 HTTP 响应格式（由 common/response.py 负责）。

# TODO(M2)：实现 CustomJSONEncoder(json.JSONEncoder) 类，支持 datetime / UUID / Decimal / Pydantic BaseModel 的自动序列化。
# TODO(M2)：实现 to_json(obj: Any) -> str 函数，使用 CustomJSONEncoder 将对象序列化为 JSON 字符串。

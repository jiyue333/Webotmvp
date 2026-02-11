# 文件职责：定义文档解析产物的数据模型 Document 和 Chunk，作为 parser → splitter → ingest 链路的统一数据契约。
# 边界：仅定义数据结构（Pydantic 模型），不包含解析逻辑、不依赖外部服务。

# TODO(M5)：定义 Chunk(BaseModel) 模型，字段含 content: str, seq: int, start: int, end: int, images: list[dict], metadata: dict。
# TODO(M5)：定义 Document(BaseModel) 模型，字段含 content: str, images: dict[str,str], chunks: list[Chunk], metadata: dict。提供 is_valid() 方法判断内容非空。

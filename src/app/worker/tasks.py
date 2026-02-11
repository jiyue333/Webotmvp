# 文件职责：定义异步任务类型常量、TaskEnvelope 结构化信封和业务载荷数据类，供 queue.py 序列化和 ingestion_worker.py 路由使用。
# 边界：只定义任务类型与数据结构；不包含任务处理逻辑（由 ingestion_worker 调度到 services 层）；不依赖 infra 层。

# TODO(M5)：定义 TaskType 常量。MVP 阶段仅需 DOCUMENT_PROCESS = "document:process"（对标 WeKnora types.TypeDocumentProcess）。
# TODO(M5)：定义 TaskEnvelope 数据类（Pydantic BaseModel），作为 Redis Stream 消息体。字段：
#   - task_id: str           — 唯一标识（UUIDv7），通过 default_factory 内联生成，无需独立模块
#   - task_type: str         — 任务类型（如 "document:process"）
#   - user_id: str           — 提交任务的用户 ID
#   - created_at: datetime   — 任务创建时间
#   - retry_count: int       — 当前重试次数（默认 0）
#   - payload: dict          — 业务载荷（具体结构由 task_type 决定）

# TODO(M5)：定义数据来源 Discriminated Union（Pydantic v2 判别联合），按 source_type 字段自动选择正确的类：
#   - FileSource(source_type="file", file_path: str, file_name: str, file_type: str)
#   - UrlSource(source_type="url", url: str)
#   - ManualSource(source_type="manual", content: str)
#   类型：DocumentSource = Annotated[FileSource | UrlSource | ManualSource, Discriminator("source_type")]

# TODO(M5)：定义 DocumentProcessPayload 数据类。字段：
#   - knowledge_id: str
#   - knowledge_base_id: str
#   - source: DocumentSource  — 判别联合，Pydantic 反序列化时按 source_type 自动选择对应 Source 类，字段缺失直接报错
#   Worker 中使用 match payload.source 按来源类型分派处理逻辑，新增来源只需加一个 Source 类。

# TODO(M7)：新增 CHUNK_EXTRACT = "chunk:extract" 任务类型及 ExtractChunkPayload（知识图谱阶段需要）。

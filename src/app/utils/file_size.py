# 文件职责：提供文件上传大小限制和文件类型校验工具函数。供 KnowledgeService 文件上传和 middleware 层调用。对齐 WeKnora internal/utils/filesize.go（GetMaxFileSize / GetMaxFileSizeMB）。
# 边界：只提供大小和类型校验的纯函数；不处理文件 I/O（由 docparser 负责），不依赖数据库。

# TODO(M3)：实现 get_max_file_size() -> int 函数。从环境变量 MAX_FILE_SIZE_MB 读取上限（默认 50MB），返回字节数。
# TODO(M3)：实现 get_max_file_size_mb() -> int 函数。返回 MB 单位的上限值。
# TODO(M3)：定义 ALLOWED_FILE_TYPES: dict[str, list[str]] 常量。映射文件类型到 MIME 类型列表，如 {"pdf": ["application/pdf"], "docx": [...], ...}。对齐 mvp.md §4.2.5 支持的文件类型。
# TODO(M3)：实现 validate_file_type(filename: str, content_type: str) -> bool 函数。根据文件扩展名和 MIME 类型校验是否在允许列表中。

# 文件职责：定义全局业务常量，供 service/api/worker 层引用，避免魔法值散落在代码中。
# 边界：只包含纯常量定义；不含配置加载逻辑（由 config.py 负责），不含枚举类（简单字符串常量即可，复杂枚举放各自 schema）。

# TODO(M2)：定义分页默认常量。DEFAULT_PAGE_SIZE = 20, MAX_PAGE_SIZE = 100。
# TODO(M2)：定义 parse_status 字符串常量。统一使用 pending/processing/completed/failed（全项目已对齐）。
# TODO(M2)：定义 knowledge type 字符串常量。KNOWLEDGE_TYPE_FILE / KNOWLEDGE_TYPE_URL / KNOWLEDGE_TYPE_MANUAL。
# TODO(M2)：定义 model type 字符串常量。MODEL_TYPE_LLM / MODEL_TYPE_EMBEDDING / MODEL_TYPE_RERANK。
# TODO(M3)：定义文件大小限制常量。MAX_UPLOAD_SIZE_BYTES，允许的文件类型列表 ALLOWED_FILE_TYPES。
# TODO(M4)：定义消息角色常量。ROLE_USER / ROLE_ASSISTANT / ROLE_SYSTEM。

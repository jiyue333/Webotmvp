# 文件职责：初始迁移脚本，创建 MVP 所需的全部基础表（users / auth_tokens / models / knowledge_bases / knowledge_tags / knowledges / chunks / embeddings / sessions / messages），并启用 pgvector 和 pg_search 扩展。
# 边界：仅负责 DDL 变更（CREATE TABLE / CREATE INDEX / CREATE EXTENSION）；不包含数据填充或业务逻辑；表结构严格对齐 mvp.md §4.5.2 定义。

# TODO(M1)：补充 Alembic revision 元数据。revision = "0001"，down_revision = None，branch_labels = None，depends_on = None。
# TODO(M1)：启用 pgvector 扩展。op.execute("CREATE EXTENSION IF NOT EXISTS vector")。
# TODO(M1)：启用 pg_search 扩展（ParadeDB BM25）。op.execute("CREATE EXTENSION IF NOT EXISTS pg_search")。
# TODO(M1)：创建 users 表。字段与索引对齐 mvp.md §4.5.2 users 定义（id/username/email/password_hash/is_active/created_at/updated_at/deleted_at + UNIQUE(username) + UNIQUE(email)）。
# TODO(M1)：创建 auth_tokens 表。字段与索引对齐 mvp.md §4.5.2 auth_tokens 定义（id/user_id/token/token_type/expires_at/is_revoked/created_at + FK user_id → users.id ON DELETE CASCADE + idx 索引）。
# TODO(M1)：创建 models 表。字段与索引对齐 mvp.md §4.5.2 models 定义（id/name/type/source/description/parameters(JSONB)/is_default/status/created_by/timestamps + idx_models_type + idx_models_source）。
# TODO(M1)：创建 knowledge_bases 表。字段对齐 mvp.md §4.5.2 knowledge_bases 定义（id/name/description/embedding_model_id/chunking_config(JSONB)/created_by/timestamps）。
# TODO(M1)：创建 knowledge_tags 表。字段与索引对齐 mvp.md §4.5.2 knowledge_tags 定义（id/knowledge_base_id/name/color/sort_order/timestamps + 部分唯一索引 UNIQUE(kb_id, name) WHERE deleted_at IS NULL）。
# TODO(M1)：创建 knowledges 表。字段与索引对齐 mvp.md §4.5.2 knowledges 定义（id/knowledge_base_id/type/title/source/parse_status/enable_status/file_*/tag_id/error_message/metadata(JSONB)/timestamps + 部分唯一索引 UNIQUE(kb_id, file_hash) WHERE deleted_at IS NULL）。
# TODO(M1)：创建 chunks 表。字段与索引对齐 mvp.md §4.5.2 chunks 定义（id/knowledge_base_id/knowledge_id/content/chunk_index/chunk_type/is_enabled/start_at/end_at/pre_chunk_id/next_chunk_id/parent_chunk_id/tag_id/timestamps）。
# TODO(M1)：创建 embeddings 表。字段与索引对齐 mvp.md §4.5.2 embeddings 定义（id(SERIAL)/source_id/source_type/chunk_id/knowledge_id/knowledge_base_id/content/dimension/embedding(HALFVEC)/is_enabled/tag_id/timestamps + UNIQUE(source_id, source_type) + HNSW 向量索引 + BM25 全文索引）。
# TODO(M1)：创建 sessions 表。字段对齐 mvp.md §4.5.2 sessions 定义（id/title/knowledge_base_id/created_by/timestamps）。
# TODO(M1)：创建 messages 表。字段与索引对齐 mvp.md §4.5.2 messages 定义（id/request_id/session_id/role/content/knowledge_references(JSONB)/is_completed/timestamps + idx_messages_session）。
# TODO(M1)：实现 downgrade() 函数。按依赖逆序删除所有表，删除 pg_search 和 vector 扩展。

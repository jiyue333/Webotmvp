# 文件职责：知识库管理服务，负责知识库 CRUD、分块配置管理、级联删除编排（关联 knowledge/tag/chunk/embedding 清理）。
# 边界：编排 KnowledgeBaseRepository 完成持久化；级联删除时依赖 KnowledgeService（写操作走 Service 层保证业务完整性），单向依赖不会形成循环（KnowledgeService 只读 KB 信息通过 Repository 层获取）。
# 对标：WeKnora internal/application/service/knowledgebase.go。

# TODO(M3): 实现 KnowledgeBaseService 类骨架。注入 KnowledgeBaseRepository、KnowledgeService、ChunkRepository、Config（chunking_config 默认值）。
# TODO(M3): 实现 create_kb()。创建知识库记录，设置默认 chunking_config（chunk_size=512, overlap=50, split_markers）。
# TODO(M3): 实现 get_kb_by_id()。按 ID 查询知识库。
# TODO(M3): 实现 list_kbs()。分页查询当前用户的知识库列表，含 knowledge_count/chunk_count 统计。
# TODO(M3): 实现 update_kb()。更新名称/描述/分块配置等可选字段。
# TODO(M3): 实现 delete_kb()。软删除知识库，投递异步任务；Worker 回调 process_kb_delete() 通过 KnowledgeService 级联清理 knowledge 及其关联的 chunk/embedding/graph 数据。

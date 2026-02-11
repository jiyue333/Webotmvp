# 文件职责：知识标签管理服务，负责标签 CRUD、同知识库下标签名唯一校验、删除时关联知识 tag_id 置空。
# 边界：编排 KnowledgeTagRepository 完成持久化，删除标签时需协调 KnowledgeRepository 清理引用；不跨知识库操作。
# 对标：WeKnora internal/application/service/tag.go。

# TODO(M3): 实现 KnowledgeTagService 类骨架。注入 KnowledgeTagRepository、KnowledgeRepository。
# TODO(M3): 实现 create_tag()。校验同 KB 下 name 唯一（部分唯一索引 WHERE deleted_at IS NULL），创建标签记录。
# TODO(M3): 实现 list_tags()。按 knowledge_base_id 查询标签列表，含关联知识数量统计。
# TODO(M3): 实现 update_tag()。更新 name/color/sort_order 等可选字段。
# TODO(M3): 实现 delete_tag()。软删除标签，将引用该标签的 knowledges.tag_id 置空。

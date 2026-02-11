# 文件职责：封装 knowledge_tags 表的数据访问操作，提供标签 CRUD、同知识库下名称唯一性校验等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 knowledge_tags 表。
# 边界：只负责 knowledge_tags 表的持久化读写；删除标签后置空关联知识 tag_id 的操作由 KnowledgeTagService 编排。查询自动过滤 deleted_at IS NULL。上游调用者为 KnowledgeTagService。

# TODO(M3)：定义 KnowledgeTagRepository(SoftDeleteRepository) 类，绑定 KnowledgeTag ORM 模型。
# TODO(M3)：实现 list_by_kb(knowledge_base_id) 方法。返回指定知识库的标签列表，附带关联知识数量统计。
# TODO(M3)：实现 check_name_unique(knowledge_base_id, name) 方法。检查同知识库下未删除标签名是否重复（部分唯一索引）。

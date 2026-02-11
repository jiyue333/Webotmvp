# 文件职责：封装 knowledge_bases 表的数据访问操作，提供知识库 CRUD、按创建者筛选、分页列表等方法。继承 SoftDeleteRepository。对齐 mvp.md §4.5.2 knowledge_bases 表。
# 边界：只负责 knowledge_bases 表的持久化读写；级联删除关联知识/标签的逻辑由 KBService 编排。查询自动过滤 deleted_at IS NULL。上游调用者为 KBService。

# TODO(M3)：定义 KnowledgeBaseRepository(SoftDeleteRepository) 类，绑定 KnowledgeBase ORM 模型。
# TODO(M3)：实现 list_by_user(created_by, page, page_size) 方法。按创建者分页查询知识库列表。
# TODO(M3)：实现 get_with_stats(kb_id) 方法。查询知识库详情，附带关联的知识条数统计。

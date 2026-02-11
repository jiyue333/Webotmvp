# 文件职责：封装基于 Neo4j 的知识图谱检索能力，包括实体/关系写入和图谱增强检索。对齐 WeKnora internal/application/repository/retriever/neo4j/repository.go。
# 边界：只负责 Neo4j 的读写操作；实体/关系抽取逻辑（调用 LLM 从文本中提取实体）由 GraphService 负责。图谱功能受 NEO4J_ENABLE 开关控制，关闭时不应调用本仓储。上游调用者为 GraphService、RetrieverService。

# TODO(M7)：定义 Neo4jRetrieverRepository 类，接收 Neo4j AsyncDriver。
# TODO(M7)：实现 save_entities(knowledge_base_id, entities) 方法。批量写入实体节点和关系边到 Neo4j。
# TODO(M7)：实现 search_entities(knowledge_base_id, query_entities, top_k) 方法。根据查询中提取的实体名称，在图谱中搜索相关实体及其关系链路，返回增强上下文文本。
# TODO(M7)：实现 delete_by_knowledge(knowledge_id) 方法。删除指定知识关联的所有实体和关系。

# 文件职责：知识图谱服务，负责实体/关系抽取（LLM 驱动）、Neo4j 图写入、图检索增强（按实体查询关联 Chunk）、图谱开关与降级。
# 边界：编排 GraphRepository（Neo4j）完成图数据持久化和检索，调用 ModelService 获取 Chat 模型执行实体抽取；受 NEO4J_ENABLE 开关控制，关闭时跳过所有图谱操作。
# 对标：WeKnora internal/application/service/graph.go（BuildGraph/extractEntities/extractRelationships/calculateWeights）和 chat_pipline/extract_entity.go、search_entity.go。

# TODO(M7): 实现 GraphService 类骨架。注入 GraphRepository（Neo4j）、ModelService、Config（NEO4J_ENABLE 开关）。
# TODO(M7): 实现 build_graph()。接收 chunks 列表，并发抽取实体和关系，计算权重，批量写入 Neo4j。
# TODO(M7): 实现 search_entities()。按关键词在 Neo4j 中检索实体及其关联 Chunk（供 Pipeline SearchEntity 步骤使用）。
# TODO(M7): 实现 delete_graph_by_knowledge_id()。按知识 ID 删除关联的图数据（级联删除场景）。

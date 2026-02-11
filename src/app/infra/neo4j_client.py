# 文件职责：创建并管理 Neo4j 异步驱动连接，提供图数据库访问入口。对齐 WeKnora internal/application/repository/retriever/neo4j 的连接逻辑。
# 边界：仅负责 Neo4j Driver 创建与生命周期管理；不执行 Cypher 查询（由 repositories/graph_repository 负责），受 NEO4J_ENABLE 配置开关控制。

# TODO(M7)：定义 create_neo4j_driver(uri, user, password) 函数。使用 neo4j.AsyncGraphDatabase.driver 创建异步驱动。
# TODO(M7)：定义 init_neo4j(driver) 协程。应用启动时验证连接并检查 APOC 插件可用性。
# TODO(M7)：定义 close_neo4j(driver) 协程。应用关闭时调用 driver.close() 释放连接。
# TODO(M7)：在 NEO4J_ENABLE=false 时返回 None，确保图谱关闭时主链路不受影响。

# 文件职责：infra 包入口；统一导出数据库引擎、Redis 客户端、Neo4j 客户端、存储客户端等基础设施实例，供 container.py 装配使用。
# 边界：仅控制包级导出边界；不实现连接逻辑（由各子模块负责），不承载业务状态。

# TODO(M2)：导出 get_db_engine / get_redis / get_neo4j_client / get_storage_client 等工厂函数。

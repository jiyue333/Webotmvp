# 文件职责：维护应用依赖容器，管理基础设施资源（DB/Redis/Neo4j）的创建与销毁顺序，对外提供全局容器单例。对齐 WeKnora internal/container/container.go 的 BuildContainer。
# 边界：只管理资源生命周期编排；各资源的具体初始化由 infra/ 层实现，不包含业务逻辑。

# TODO(M2)：定义 AppContainer 类，包含 startup() 和 shutdown() 异步方法。
# TODO(M2)：startup() 中按依赖顺序初始化：get_settings() → create_async_db_engine() → create_redis_client() → init_db() / init_redis() 验证连接。
# TODO(M2)：shutdown() 中按反向顺序释放：close_redis() → close_db()。
# TODO(M7)：startup() 中若 NEO4J_ENABLE=true，初始化 Neo4j driver；shutdown() 中释放。
# TODO(M2)：定义模块级 get_container_instance() 函数，返回全局 AppContainer 单例。

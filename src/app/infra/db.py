# 文件职责：创建并管理 SQLAlchemy AsyncEngine 和 AsyncSession 工厂，提供 PostgreSQL 连接池生命周期管理。对齐 WeKnora internal/database 的连接初始化逻辑。
# 边界：仅负责引擎创建、连接池配置与 session 工厂；不执行 SQL/ORM 查询（由 repositories/ 负责），不处理迁移（由 Alembic 负责）。

# TODO(M2)：定义 create_async_db_engine(database_url) 函数。使用 create_async_engine 创建异步引擎，配置 pool_size / max_overflow / pool_pre_ping 等连接池参数。
# TODO(M2)：定义 get_async_session_factory(engine) 函数。返回 async_sessionmaker 实例，供 repository 层注入使用。
# TODO(M2)：定义 init_db() 协程。在应用启动时调用，验证数据库连接是否正常。
# TODO(M2)：定义 close_db(engine) 协程。在应用关闭时调用 engine.dispose()，释放连接池资源。

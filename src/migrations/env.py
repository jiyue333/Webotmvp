# 文件职责：Alembic 迁移环境配置，负责读取 SQLAlchemy metadata、注入数据库连接 URL，驱动 online/offline 两种迁移模式。
# 边界：只负责迁移环境初始化与 migration context 配置；数据库连接 URL 从 AppSettings 获取，不硬编码；不包含具体的表定义（由 ORM model 层维护）。

# TODO(M1)：从 alembic.ini 读取日志配置并初始化。调用 fileConfig(config.config_file_name)。
# TODO(M1)：导入 app.infra.database 中的 Base.metadata，赋值给 target_metadata，使 autogenerate 能感知所有 ORM 模型。
# TODO(M1)：实现 run_migrations_offline() 函数。调用 context.configure(url=..., target_metadata=..., literal_binds=True)，用于生成纯 SQL 脚本而不连接数据库。
# TODO(M1)：实现 run_migrations_online() 函数。从 AppSettings 获取 DATABASE_URL，创建 Engine，调用 context.configure(connection=..., target_metadata=...)，在 context.begin_transaction() 内执行 context.run_migrations()。
# TODO(M1)：在模块末尾根据 context.is_offline_mode() 分支调用 offline 或 online 函数。

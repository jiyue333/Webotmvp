"""
文件职责：维护数据库迁移配置与版本入口，约束迁移执行边界。
边界：只描述迁移配置或版本变更；上游由 alembic 调用，下游作用于数据库 schema，不处理业务请求。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/migrations/env.py`。
"""

from logging.config import fileConfig
from alembic import context
from sqlalchemy import engine_from_config, pool

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = None


def run_migrations_offline() -> None:
    """执行 `run_migrations_offline` 逻辑。

    输入：按函数签名参数接收。
    输出：返回当前函数声明对应的数据结果。
    副作用：可能读取或更新进程内状态与外部依赖。
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """执行 `run_migrations_online` 逻辑。

    输入：按函数签名参数接收。
    输出：返回当前函数声明对应的数据结果。
    副作用：可能读取或更新进程内状态与外部依赖。
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

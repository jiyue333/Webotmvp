# infra/

## 目录职责
封装所有外部基础设施的连接创建与生命周期管理，为上层（container / repository / worker）提供开箱即用的客户端实例。

## 边界
- **只负责**：连接创建、连接池配置、健康检查、连接释放。
- **不负责**：业务查询/写入（由 repositories/ 负责）、配置声明（由 common/config.py 负责）、数据迁移（由 Alembic 负责）。
- **上游调用方**：container.py（应用启动/关闭时调用 init/close）、api/deps.py（注入 session）。
- **下游依赖**：common/config.py（获取连接 URL 等配置项）。

## 文件清单

| 文件                | 职责                         | 首次实现阶段 |
| ------------------- | ---------------------------- | ------------ |
| `__init__.py`       | 包入口，导出工厂函数         | M1           |
| `db.py`             | PostgreSQL 连接池管理        | M1           |
| `redis.py`          | Redis 异步客户端管理         | M1           |
| `neo4j_client.py`   | Neo4j 异步驱动管理           | M7           |
| `storage_client.py` | 对象存储客户端（MinIO/本地） | M5           |

## 设计原则
- 每个外部依赖对应一个独立文件，职责单一。
- 工厂函数统一命名为 `create_xxx(config)` 或 `get_xxx()`，方便 container 装配。
- 生命周期管理拆分为 `init_xxx()`（验证连接）与 `close_xxx()`（释放资源），对应 FastAPI lifespan 的 startup/shutdown。
- Neo4j 受 `NEO4J_ENABLE` 开关控制，关闭时返回 None，确保主链路不受影响。

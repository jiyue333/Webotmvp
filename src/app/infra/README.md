# infra/

## 概述

外部基础设施连接层。管理与数据库、缓存、图数据库、对象存储的连接生命周期。

## 文件说明

| 文件                | 职责                               | 配置来源                          |
| ------------------- | ---------------------------------- | --------------------------------- |
| `db.py`             | PostgreSQL engine 与 async session | `common/config.py → DATABASE_URL` |
| `redis.py`          | Redis 连接池                       | `common/config.py → REDIS_URL`    |
| `neo4j_client.py`   | Neo4j driver 管理                  | `common/config.py → NEO4J_URI`    |
| `storage_client.py` | MinIO / 本地文件存储               | `common/config.py → STORAGE_*`    |

## 设计原则

- 每个文件提供 **init / get / close** 三个生命周期函数，由 `container.py` 统一编排。
- 所有连接只读取 `common/config.py` 的配置，不直接访问环境变量。
- 与 `client/`（AI 模型远程调用）的区别：`infra/` 管理的是 **有状态的持久连接**，`client/` 是 **无状态的 HTTP 调用**。

## TODO

- [infra][M1] 实现各连接的初始化与关闭逻辑
- [infra][M1] 在 `container.py` 中注册生命周期

# migrations — 数据库迁移

## 职责
管理 PostgreSQL 数据库 schema 的版本化变更，使用 Alembic 驱动迁移。对齐 WeKnora `migrations/versioned/*` 和 `scripts/migrate.sh` 的迁移思路。

## 边界
- **只负责** DDL 变更（CREATE/ALTER/DROP TABLE/INDEX/EXTENSION）和必要的数据迁移。
- **不负责** 数据填充（seed data）、业务逻辑、ORM 模型定义（由 `app/infra/database.py` 和各 repository 层维护）。
- **不直接暴露** 给 HTTP 请求；由 CLI（`alembic upgrade/downgrade`）或 CI 流水线触发。

## 文件结构
```
migrations/
├── env.py              # Alembic 环境配置，注入数据库连接和 ORM metadata
├── script.py.mako      # 迁移脚本模板（Alembic autogenerate 使用）
├── versions/           # 版本化迁移脚本目录
│   └── 0001_init.py    # 初始迁移：创建 MVP 全部基础表
└── README.md           # 本文件
```

## 常用命令
```bash
# 生成新迁移（基于 ORM model 变更自动检测）
cd src && alembic revision --autogenerate -m "描述"

# 升级到最新版本
cd src && alembic upgrade head

# 回滚一个版本
cd src && alembic downgrade -1

# 查看当前版本
cd src && alembic current

# 查看迁移历史
cd src && alembic history
```

## 设计原则
1. **一次迁移一个主题**：每个迁移脚本只做一件事（如"创建 users 表"或"添加 tag_id 列"），便于回滚。
2. **upgrade/downgrade 对称**：每个 upgrade 操作必须有对应的 downgrade 操作。
3. **部分唯一索引**：含 `deleted_at` 软删除的表，唯一约束使用 `WHERE deleted_at IS NULL`，确保删除后可重建同名记录。
4. **扩展管理**：pgvector 和 pg_search 扩展在初始迁移中启用。

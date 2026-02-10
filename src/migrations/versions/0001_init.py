"""
文件职责：维护数据库迁移配置与版本入口，约束迁移执行边界。
边界：只描述迁移配置或版本变更；上游由 alembic 调用，下游作用于数据库 schema，不处理业务请求。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/migrations/versions/0001_init.py`。
"""


from __future__ import annotations

# revision identifiers, used by Alembic.
revision = "0001_init"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Apply schema changes for this revision."""
    pass


def downgrade() -> None:
    """Revert schema changes for this revision."""
    pass

"""M1 initial migration skeleton.

Revision ID: 0001_init
Revises: 
Create Date: 2026-02-10
"""

"""
文件职责：维护 `src/migrations/versions/0001_init.py` 的首个 Alembic 迁移占位版本。
边界：仅定义迁移版本锚点，不在 M1 写入业务表结构细节。
TODO：
- [arch][P1][todo] 在 M1 后续阶段按领域逐步补齐 users/models/kb/session/message 等表迁移。
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

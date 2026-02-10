# 文件职责：维护 `src/migrations/script.py.mako` 的 M1 骨架与结构约束。
# 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
# TODO：
# - [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。

"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision | comma,n}
Create Date: ${create_date}
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

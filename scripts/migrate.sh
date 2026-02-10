#!/usr/bin/env bash
# 文件职责：维护 `scripts/migrate.sh` 的 Alembic 迁移命令封装。
# 边界：仅透传 Alembic 参数，不在脚本中硬编码迁移策略或环境切换逻辑。
# TODO：
# - [ops][P2][todo] 在 M8 增加迁移前置检查与失败回滚提示。

set -euo pipefail

cd src
alembic "$@"

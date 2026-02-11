#!/usr/bin/env bash
# 文件职责：封装 Alembic 迁移命令，在项目根目录执行时自动切换到 src/ 目录，透传所有参数给 alembic CLI。对齐 WeKnora scripts/migrate.sh。
# 边界：仅做目录切换和命令透传；不包含 DDL 逻辑（由迁移脚本负责）。

# TODO(M1)：实现命令透传。`set -euo pipefail && cd src && alembic "$@"`。

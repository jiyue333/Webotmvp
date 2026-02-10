#!/usr/bin/env bash
# 文件职责：维护 `scripts/lint.sh` 的本地静态检查入口。
# 边界：仅做基础语法与风格检查，不执行会改写代码的格式化动作。
# TODO：
# - [obs][P2][todo] 在 M8 接入统一 lint 规则（ruff/mypy/eslint）并与 CI 对齐。

set -euo pipefail

echo "[lint] backend compile check"
python -m compileall -q src/app

if command -v ruff >/dev/null 2>&1; then
  echo "[lint] ruff check"
  (cd src && ruff check app tests)
else
  echo "[lint] ruff not found, skip"
fi

echo "[lint] done"

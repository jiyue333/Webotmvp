#!/usr/bin/env bash
# 文件职责：维护 `scripts/smoke.sh` 的最小健康检查脚本。
# 边界：仅验证健康接口可访问，不覆盖鉴权、入库、检索、对话等业务链路。
# TODO：
# - [test][P2][todo] 在 M8 扩展为登录-上传-检索-对话的完整 smoke 用例。

set -euo pipefail

HEALTH_URL="${1:-http://localhost:8000/health}"
BODY="$(curl -fsS "$HEALTH_URL")"

echo "$BODY" | grep -q '"status"' || {
  echo "[smoke] health response missing status field: $BODY"
  exit 1
}

echo "[smoke] ok -> $HEALTH_URL"

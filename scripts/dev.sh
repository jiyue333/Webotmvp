#!/usr/bin/env bash
# 文件职责：维护 `scripts/dev.sh` 的本地开发流程编排脚本。
# 边界：仅封装启动/停止/日志等开发命令，不处理部署编排与环境初始化细节。
# TODO：
# - [ops][P2][todo] 在 M8 增加端到端健康探针与依赖连通性检查命令。

set -euo pipefail

COMPOSE_FILE="docker-compose.dev.yml"

usage() {
  echo "Usage: ./scripts/dev.sh {start [--full]|stop|backend|ui|status|logs|help}"
}

start_services() {
  if [[ "${1:-}" == "--full" ]]; then
    docker compose -f "$COMPOSE_FILE" --profile full up -d
  else
    docker compose -f "$COMPOSE_FILE" up -d postgres redis
  fi
}

case "${1:-help}" in
  start)
    start_services "${2:-}"
    ;;
  stop)
    docker compose -f "$COMPOSE_FILE" down
    ;;
  backend)
    cd src
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ;;
  ui|frontend)
    cd ui
    npm run dev
    ;;
  status)
    docker compose -f "$COMPOSE_FILE" ps
    ;;
  logs)
    docker compose -f "$COMPOSE_FILE" logs -f
    ;;
  help|*)
    usage
    ;;
esac

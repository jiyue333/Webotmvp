#!/usr/bin/env bash
# 文件职责：封装 `dev.sh` 对应的开发运维命令，减少重复操作与误用风险。
# 边界：只封装命令入口与流程控制；上游由开发者执行，下游调用系统工具，不定义业务规则。
# TODO：
# - [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：执行 `bash -n scripts/*.sh` 并通过脚本分支自检；归属模块：`scripts/dev.sh`。

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
    # 启动依赖服务，默认仅基础依赖；传 --full 时带上可选服务。
    start_services "${2:-}"
    ;;
  stop)
    # 停止并清理当前 compose 资源。
    docker compose -f "$COMPOSE_FILE" down
    ;;
  backend)
    # 本地启动后端开发服务（热更新）。
    cd src
    uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    ;;
  ui|frontend)
    # 本地启动前端开发服务。
    cd ui
    npm run dev
    ;;
  status)
    # 查看 compose 服务状态。
    docker compose -f "$COMPOSE_FILE" ps
    ;;
  logs)
    # 跟随查看 compose 日志输出。
    docker compose -f "$COMPOSE_FILE" logs -f
    ;;
  help|*)
    usage
    ;;
esac

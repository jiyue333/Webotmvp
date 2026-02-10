#!/usr/bin/env bash
set -euo pipefail

case "${1:-help}" in
  start)
    docker compose -f docker-compose.dev.yml up -d
    ;;
  stop)
    docker compose -f docker-compose.dev.yml down
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
    docker compose -f docker-compose.dev.yml ps
    ;;
  logs)
    docker compose -f docker-compose.dev.yml logs -f
    ;;
  *)
    echo "Usage: ./scripts/dev.sh {start|stop|backend|ui|status|logs}"
    ;;
esac

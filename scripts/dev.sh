#!/usr/bin/env bash
# 文件职责：本地开发工作流入口脚本，封装依赖服务启停（docker compose）、后端热更新启动（uvicorn --reload）、前端开发服务（npm run dev）等常用操作，通过子命令分派。
# 边界：仅编排 CLI 命令调用；不包含业务逻辑；依赖 docker-compose.dev.yml 和 pyproject.toml 已就绪。

# TODO(M1)：实现 start 子命令。默认 `docker compose -f docker-compose.dev.yml up -d postgres redis`，传 --full 时追加 neo4j + minio（使用 --profile full）。
# TODO(M1)：实现 stop 子命令。`docker compose -f docker-compose.dev.yml down`。
# TODO(M1)：实现 backend 子命令。`cd src && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`。
# TODO(M1)：实现 ui 子命令。`cd ui && npm run dev`。
# TODO(M1)：实现 status 子命令。`docker compose -f docker-compose.dev.yml ps`。
# TODO(M1)：实现 logs 子命令。`docker compose -f docker-compose.dev.yml logs -f`。
# TODO(M1)：实现 help 子命令和 usage 函数。打印可用命令列表。

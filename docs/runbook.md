# Runbook（M1）

## 文件职责
- 记录本地运行、检查、排障与回滚的最小操作路径。
- 为 M8 可观测增强提供操作基线。

## 边界
- 仅覆盖本地 Docker/开发环境，不包含生产级容量与高可用预案。
- 不替代故障根因分析流程，只提供最小检查顺序。

## 启动与停止
```bash
./scripts/dev.sh start
./scripts/dev.sh start --full
./scripts/dev.sh stop
```

## 健康检查
```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/health
./scripts/smoke.sh
```

## 常见问题排查
1. 后端不可达：检查 `./scripts/dev.sh status` 与 `./scripts/dev.sh logs`。
2. 数据库连接失败：确认 `DATABASE_URL` 与 `postgres` 端口映射。
3. Redis 连接失败：确认 `REDIS_URL` 与 `redis` 服务状态。

## TODO
- [ops][P2][todo] 在 M8 补齐 Neo4j/MinIO 故障排查手册。
- [obs][P2][todo] 在 M8 增加 trace_id/request_id 关联排查示例。

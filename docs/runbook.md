# Runbook（M1）

## 文件职责
- 维护 `runbook.md` 文档的事实约束，向协作方说明当前实现边界与演进路径。

## 边界
- 只提供文档化约束与协作说明；上游供研发阅读，下游不作为运行时行为来源。

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
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`docs/runbook.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`docs/runbook.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`docs/runbook.md`。

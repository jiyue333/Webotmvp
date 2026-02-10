# WeKnora MVP

Python 复现版 WeKnora 知识库 Chatbot MVP。

## 文件职责
- 作为仓库主入口文档，定义 M1 基线能力、运行方式和阶段性研究议题。
- 统一说明后端、前端、基础设施和脚本的最小协作契约。

## 边界
- 本文档只覆盖 MVP 单工作空间方案，不扩展 Agent/MCP/多租户能力。
- 仅承诺 M1 骨架可运行与可迭代，不在此承诺 M2-M8 业务完整实现。

## M1 已完成内容
- 建立后端/前端/脚本/部署骨架，并统一文件级职责、边界、TODO 规范。
- 提供健康检查接口：`GET /health` 与 `GET /api/v1/health`。
- 提供本地开发编排：`docker-compose.dev.yml` + `scripts/dev.sh`。

## 技术栈
- 后端：Python 3.11, FastAPI, SQLAlchemy 2.x, Alembic
- 前端：Vue 3, Vite, TypeScript, Pinia
- 数据库：PostgreSQL 16 + pgvector + pg_search (ParadeDB)
- 缓存：Redis
- 图数据库：Neo4j（可选）
- 存储：MinIO（可选）

## 快速开始

### 前置条件
- Docker 与 Docker Compose
- Python 3.11+
- Node.js 20+

### 1. 配置环境变量
```bash
cp .env.example .env
```

### 2. 启动基础设施
```bash
# 默认启动 PostgreSQL + Redis
./scripts/dev.sh start

# 启动完整依赖（含 Neo4j + MinIO）
./scripts/dev.sh start --full
```

### 3. 启动后端（新终端）
```bash
./scripts/dev.sh backend
```

### 4. 启动前端（新终端）
```bash
./scripts/dev.sh ui
```

### 5. 运行最小 smoke
```bash
./scripts/smoke.sh
```

## 常用命令
```bash
./scripts/dev.sh status
./scripts/dev.sh logs
./scripts/dev.sh stop
./scripts/test.sh
./scripts/lint.sh
```

## 环境变量契约（最小集）
- `DATABASE_URL`：后端主数据库连接。
- `REDIS_URL`：缓存与队列连接。
- `JWT_SECRET_KEY`：JWT 签名密钥。
- `NEO4J_ENABLE`：图谱能力开关。
- `STORAGE_BACKEND`：`local|minio`。
- `VITE_API_BASE_URL`：前端 API 前缀。

## 待研究内容（M2-M8）
| 阶段 | 研究问题 | 决策输出 | 验证标准 |
|---|---|---|---|
| M2 | refresh token 轮换与撤销模型如何落库 | Token 生命周期与撤销策略文档 | 注册/登录/刷新/登出链路 smoke 通过 |
| M3 | 模型 Provider 抽象最小字段集合 | `models` 领域 schema 与 CRUD 约束 | 模型与知识库管理前后端闭环 |
| M4 | stop/continue-stream 的事件与 offset 语义 | SSE 事件协议与恢复规则 | 流式中断后可继续消费且无重复 |
| M5 | 文档解析与 OCR 失败重试策略 | ingest 状态机与重试策略 | 上传后状态可观测且失败可追踪 |
| M6 | 混合检索与重排参数如何分层配置 | retrieval/rerank 配置规范 | 检索结果可返回引用且耗时可观测 |
| M7 | 图谱失败时如何降级不阻塞主链路 | graph 开关与 fallback 设计 | 图谱开关开/关均可完成对话 |
| M8 | 最小可观测口径如何覆盖核心链路 | 指标/日志/追踪清单与告警草案 | runbook 可支撑定位常见故障 |

## TODO
- [arch][P1][todo] 在 M1 完成目录 README 与文件头注释的持续一致性治理。
- [test][P2][todo] 在 M8 增加登录/上传/检索/对话的端到端回归脚本。
- [ops][P2][todo] 在 M8 为 compose 编排补充健康检查与重启策略。

## License
MIT

# WeKnora MVP - 项目开发规范

> 基于 OpenSpec 工作流的项目 AI 开发指南

## 项目概述

Python 复现版 WeKnora 知识库 Chatbot，核心功能包括：
- 多用户 JWT 鉴权
- 知识库管理与导入
- 混合检索 + 知识图谱增强
- SSE 流式对话

## 快速开始

```bash
# 启动服务
docker compose up -d

# 检查状态
docker compose ps

# 查看日志
docker compose logs -f app
```

## 开发工作流

### CCG 多模型协作命令

| 阶段 | 命令 | 用途 |
|------|------|------|
| 研究 | `/ccg:spec-research` | 需求分析，生成约束集 |
| 规划 | `/ccg:spec-plan` | 细化提案为可执行计划 |
| 实施 | `/ccg:spec-impl` | 多模型协作执行 |
| 审查 | `/ccg:spec-review` | 归档前合规审查 |

### OpenSpec 目录

```
.openspec/
├── proposals/   # 需求提案
├── plans/       # 实施计划
├── specs/       # 正式规范
└── archive/     # 归档文件
```

## 技术栈

- **后端**: Python 3.11, FastAPI, SQLAlchemy 2.x, Alembic
- **数据库**: PostgreSQL 16 + pgvector + pg_search (ParadeDB)
- **缓存/队列**: Redis
- **图数据库**: Neo4j
- **存储**: MinIO / 本地
- **部署**: Docker Compose

## 代码规范

- 使用 `ruff` 进行代码格式化和检查
- 使用 `mypy` 进行类型检查
- 使用 `pytest` 进行测试

## 参考文档

- 项目规范: `mvp.md`
- OpenSpec 环境: `.openspec/README.md`

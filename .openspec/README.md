# OpenSpec Environment

> WeKnora 知识库 Chatbot MVP 项目的规范化开发环境

## 目录结构

```
.openspec/
├── README.md          # 本文件 - 环境说明
├── proposals/         # 需求提案（待细化）
├── plans/             # 可执行计划（已细化，待批准/执行）
├── specs/             # 正式规范（已批准，指导实施）
└── archive/           # 归档文件（已完成/废弃）
```

## 工作流

```
需求 → proposals/ → plans/ → specs/ → 实施 → archive/
       [研究]      [规划]    [规范]   [执行]   [归档]
```

## 文件命名规范

- `proposals/YYYYMMDD-feature-name.md` - 提案文档
- `plans/YYYYMMDD-feature-name-plan.md` - 实施计划
- `specs/SPEC-NNN-feature-name.md` - 正式规范

## CCG 命令

| 命令 | 用途 |
|------|------|
| `/ccg:spec-research` | 将需求转化为约束集（并行探索） |
| `/ccg:spec-plan` | 将提案细化为零决策可执行计划 |
| `/ccg:spec-impl` | 按规范执行多模型协作实施 |
| `/ccg:spec-review` | 归档前的多模型合规审查 |

## 项目概述

**WeKnora MVP** - Python 复现版知识库 Chatbot

### 核心功能
- 多用户 JWT 鉴权
- 模型管理（多厂商 provider）
- 知识库管理与导入（file/url/manual）
- 文档解析 + OCR（内嵌实现）
- 混合检索（向量 + 关键词 + 重排）
- 知识图谱增强（Neo4j）
- SSE 流式对话

### 技术栈
- Python 3.11 + FastAPI + SQLAlchemy 2.x
- PostgreSQL 16 + pgvector + pg_search (ParadeDB)
- Redis + Neo4j + MinIO
- Docker Compose 本地部署

### 不做
- Agent/MCP 能力
- 多租户
- 多向量后端适配
- K8s 部署

## 参考

- 项目文档: `mvp.md`
- 原项目: WeKnora (Go 版本)

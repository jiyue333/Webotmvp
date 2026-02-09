# WeKnora MVP

Python 复现版 WeKnora 知识库 Chatbot MVP

## 技术栈

- **后端**: Python 3.11, FastAPI, SQLAlchemy 2.x, Alembic
- **前端**: Vue 3, Vite, TypeScript, TailwindCSS, Pinia
- **数据库**: PostgreSQL 16 + pgvector + pg_search (ParadeDB)
- **缓存**: Redis
- **图数据库**: Neo4j (可选)
- **存储**: MinIO (可选)

## 快速开始

### 前置条件

- Docker & Docker Compose
- Python 3.11+
- Node.js 20+

### 开发环境

#### 1. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 修改配置（如 JWT_SECRET_KEY）
```

#### 2. 启动基础设施

```bash
# 启动 PostgreSQL + Redis
./scripts/dev.sh start

# 启动全部服务（含 Neo4j + MinIO）
./scripts/dev.sh start --full
```

#### 3. 启动后端（新终端）

```bash
./scripts/dev.sh backend
```

后端服务:
- API: http://localhost:8000
- Swagger 文档: http://localhost:8000/docs

#### 4. 启动前端（新终端）

```bash
./scripts/dev.sh frontend
```

前端服务: http://localhost:5173

### 常用命令

```bash
# 查看服务状态
./scripts/dev.sh status

# 查看服务日志
./scripts/dev.sh logs

# 停止所有服务
./scripts/dev.sh stop

# 帮助
./scripts/dev.sh help
```

## License

MIT

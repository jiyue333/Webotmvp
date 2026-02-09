# Week 1 实施计划 - 基础骨架与用户体系

> 综合 Codex 后端规划 + Gemini 前端规划

## 1. 技术选型（已确认）

### 后端
- Python 3.11 + FastAPI + Uvicorn
- SQLAlchemy 2.x AsyncSession + Alembic
- PostgreSQL (paradedb/paradedb:v0.21.4-pg17) + Redis
- 分层架构：Router -> Handler -> Service -> Repository
- JWT 双 Token 机制（Access 15min + Refresh 7days）

### 前端
- Vue 3 + Vite + TypeScript
- vue-router（公开/受保护路由）
- Pinia 状态管理
- Axios + 请求/响应拦截器 + Token 自动刷新
- TailwindCSS

---

## 2. 后端目录结构

```text
# 项目根目录
Webotmvp/
├── docker-compose.yml                   # 根目录统一编排
├── .env.example                         # 环境变量模板
├── .env                                 # 实际环境变量（不入仓库）
│
├── backend/
│   ├── app/
│   │   ├── main.py                      # 应用入口
│   │   ├── core/
│   │   │   ├── config.py                # 环境配置
│   │   │   ├── security.py              # JWT 签发/校验
│   │   │   ├── exceptions.py            # 业务异常
│   │   │   ├── response.py              # 统一响应格式
│   │   │   └── deps.py                  # 依赖注入
│   │   ├── db/
│   │   │   ├── session.py               # AsyncSession
│   │   │   └── base.py                  # Declarative Base
│   │   ├── models/
│   │   │   ├── user.py                  # users 表
│   │   │   ├── auth_token.py            # auth_tokens 表
│   │   │   └── knowledge_base.py        # knowledge_bases 表
│   │   ├── schemas/
│   │   │   ├── common.py                # 通用响应 Schema
│   │   │   ├── auth.py                  # Auth 请求/响应
│   │   │   └── knowledge_base.py        # KB 请求/响应
│   │   ├── repositories/
│   │   │   ├── user_repository.py
│   │   │   ├── auth_token_repository.py
│   │   │   └── knowledge_base_repository.py
│   │   ├── services/
│   │   │   ├── auth_service.py
│   │   │   └── knowledge_base_service.py
│   │   ├── handlers/
│   │   │   ├── auth_handler.py
│   │   │   └── knowledge_base_handler.py
│   │   └── api/v1/
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── auth.py
│   │           └── knowledge_bases.py
│   ├── alembic/
│   │   ├── env.py
│   │   └── versions/
│   ├── tests/
│   ├── Dockerfile
│   ├── alembic.ini
│   └── pyproject.toml
│
└── frontend/
    ├── ... (见前端目录结构)
    ├── Dockerfile                       # 多阶段构建 + Nginx
    └── nginx.conf                       # Nginx 配置
```

---

## 3. 前端目录结构

```text
frontend/
├── src/
│   ├── api/
│   │   ├── axios.ts                     # Axios 封装 + Token 刷新
│   │   └── auth.ts                      # Auth API
│   ├── components/
│   │   └── ui/
│   │       ├── BaseButton.vue
│   │       ├── BaseInput.vue
│   │       └── BaseCard.vue
│   ├── layouts/
│   │   ├── AuthLayout.vue               # 登录/注册布局
│   │   └── DashboardLayout.vue          # 仪表盘布局
│   ├── router/
│   │   ├── index.ts
│   │   └── guard.ts                     # 路由守卫
│   ├── stores/
│   │   └── auth.ts                      # Pinia Auth Store
│   ├── types/
│   │   ├── api.d.ts
│   │   └── user.d.ts
│   ├── views/
│   │   ├── auth/
│   │   │   ├── LoginView.vue
│   │   │   └── RegisterView.vue
│   │   └── dashboard/
│   │       └── DashboardView.vue
│   ├── App.vue
│   └── main.ts
├── public/
├── index.html
├── vite.config.ts
├── tailwind.config.js
├── tsconfig.json
├── package.json
├── Dockerfile                           # 多阶段构建 + Nginx
└── nginx.conf                           # Nginx 配置（API 代理）
```

---

## 4. 数据模型设计

### users 表
| 字段 | 类型 | 约束 |
|------|------|------|
| id | UUID | PK |
| email | VARCHAR(320) | UNIQUE, NOT NULL |
| username | VARCHAR(64) | UNIQUE, NOT NULL |
| password_hash | VARCHAR(255) | NOT NULL |
| is_active | BOOLEAN | DEFAULT TRUE |
| created_at | TIMESTAMPTZ | NOT NULL |
| updated_at | TIMESTAMPTZ | NOT NULL |

### auth_tokens 表
| 字段 | 类型 | 约束 |
|------|------|------|
| id | UUID | PK |
| user_id | UUID | FK -> users.id |
| jti | UUID | UNIQUE |
| token_hash | VARCHAR(128) | UNIQUE |
| token_type | VARCHAR(16) | CHECK (refresh) |
| family_id | UUID | NOT NULL |
| is_revoked | BOOLEAN | DEFAULT FALSE |
| expires_at | TIMESTAMPTZ | NOT NULL |
| created_at | TIMESTAMPTZ | NOT NULL |

### knowledge_bases 表
| 字段 | 类型 | 约束 |
|------|------|------|
| id | UUID | PK |
| owner_id | UUID | FK -> users.id |
| name | VARCHAR(128) | NOT NULL |
| description | TEXT | NULL |
| created_at | TIMESTAMPTZ | NOT NULL |
| updated_at | TIMESTAMPTZ | NOT NULL |

约束：`UNIQUE(owner_id, name)`

---

## 5. API 端点设计

### Auth API (5 个)
| 方法 | 路径 | 鉴权 | 说明 |
|------|------|------|------|
| POST | /api/v1/auth/register | 否 | 用户注册 |
| POST | /api/v1/auth/login | 否 | 用户登录 |
| POST | /api/v1/auth/refresh | 否 | Token 刷新 |
| POST | /api/v1/auth/logout | 是 | 用户登出 |
| GET | /api/v1/auth/me | 是 | 获取当前用户 |

### KB API (5 个)
| 方法 | 路径 | 鉴权 | 说明 |
|------|------|------|------|
| POST | /api/v1/knowledge-bases | 是 | 创建知识库 |
| GET | /api/v1/knowledge-bases | 是 | 列表查询 |
| GET | /api/v1/knowledge-bases/{id} | 是 | 获取详情 |
| PUT | /api/v1/knowledge-bases/{id} | 是 | 更新知识库 |
| DELETE | /api/v1/knowledge-bases/{id} | 是 | 删除知识库 |

---

## 6. 实施步骤（按优先级）

### Day 1: 工程基线
- [ ] 后端：初始化项目结构、依赖管理
- [ ] 后端：完成 config/security/response/exceptions 基础模块
- [ ] 后端：搭建 v1 路由与健康检查
- [ ] 前端：初始化 Vite + Vue 3 + TS 项目
- [ ] 前端：配置 TailwindCSS + Alias

### Day 2: 数据库与核心组件
- [ ] 后端：建立 AsyncSession 与依赖注入
- [ ] 后端：定义 users/auth_tokens/knowledge_bases ORM
- [ ] 后端：生成 Alembic 初始迁移
- [ ] 前端：实现 BaseInput/BaseButton 原子组件
- [ ] 前端：实现 AuthLayout/DashboardLayout 布局

### Day 3: Auth 主链路
- [ ] 后端：Repository + Service + Handler 完成 5 个 Auth API
- [ ] 后端：JWT 解析依赖 + no-auth 白名单
- [ ] 前端：创建 Pinia auth store
- [ ] 前端：实现 Axios 基础拦截器
- [ ] 前端：开发 LoginView/RegisterView

### Day 4: KB CRUD + Token 刷新
- [ ] 后端：Repository + Service + Handler 完成 5 个 KB API
- [ ] 后端：owner_id 强制过滤校验
- [ ] 前端：实现 401 Token 刷新逻辑（队列重试）
- [ ] 前端：实现路由守卫
- [ ] 前端：开发 DashboardView

### Day 5: 收口与联调
- [ ] 后端：统一错误码与响应格式
- [ ] 后端：补齐 OpenAPI 文档
- [ ] 前端后端联调验证
- [ ] Docker Compose 一键启动验证
- [ ] 基础测试覆盖

---

## 7. Docker Compose 配置（根目录）

```yaml
# docker-compose.yml (项目根目录)
services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: weknora-backend
    ports:
      - "${BACKEND_PORT:-8000}:8000"
    environment:
      - DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
      - DATABASE_URL_SYNC=postgresql+psycopg://${DB_USER}:${DB_PASSWORD}@postgres:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
      - JWT_SECRET=${JWT_SECRET}
      - JWT_ACCESS_EXPIRE_MINUTES=${JWT_ACCESS_EXPIRE_MINUTES:-15}
      - JWT_REFRESH_EXPIRE_DAYS=${JWT_REFRESH_EXPIRE_DAYS:-7}
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: weknora-frontend
    ports:
      - "${FRONTEND_PORT:-80}:80"
    depends_on:
      backend:
        condition: service_healthy
    restart: unless-stopped

  postgres:
    image: paradedb/paradedb:v0.21.4-pg17
    container_name: weknora-postgres
    environment:
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
      - POSTGRES_DB=${DB_NAME}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    container_name: weknora-redis
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
```

### 前端 Dockerfile（多阶段构建 + Nginx）

```dockerfile
# frontend/Dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### 前端 Nginx 配置（API 代理）

```nginx
# frontend/nginx.conf
server {
    listen 80;
    server_name localhost;
    root /usr/share/nginx/html;
    index index.html;

    # SPA 路由
    location / {
        try_files $uri $uri/ /index.html;
    }

    # API 代理
    location /api/ {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 环境变量模板

```bash
# .env.example (项目根目录)
# Database
DB_USER=weknora
DB_PASSWORD=your_secure_password
DB_NAME=weknora

# JWT
JWT_SECRET=your_jwt_secret_key_at_least_32_chars
JWT_ACCESS_EXPIRE_MINUTES=15
JWT_REFRESH_EXPIRE_DAYS=7

# Ports
BACKEND_PORT=8000
FRONTEND_PORT=80
```

---

## 8. 验收标准

| 里程碑 | 验收标准 |
|--------|----------|
| M1 | 前端登录 -> 获取用户信息成功 |
| M2 | Token 过期自动刷新不中断用户操作 |
| M3 | KB CRUD 全流程正常 |
| M4 | owner_id 隔离测试通过 |
| M5 | Docker Compose 一键启动 |

---

## 9. 风险与缓解

| 风险 | 影响 | 缓解措施 |
|------|------|----------|
| owner_id 过滤遗漏 | 高 | Repository 层统一封装 |
| refresh token 重放 | 高 | token 轮换 + family_id |
| 401 并发刷新竞态 | 中 | isRefreshing 锁 + 请求队列 |
| AsyncSession 误用 | 中 | 每请求独立 session |

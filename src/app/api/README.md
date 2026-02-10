# api/

## 文件职责
- 维护 API 分层的入口约定与导出边界。
- 聚合所有版本路由，固定挂载顺序与前缀。

## 边界
- 只处理协议层入参与响应转换；上游接收 HTTP 请求，下游只调用 service 或依赖注入对象，不直接操作数据库。

## 目录结构
```text
api/
├── __init__.py               # 包入口
├── router.py                 # 路由聚合（挂载全部 endpoint router）
├── deps.py                   # 依赖注入工具（ContainerDep 等）
├── README.md                 # 本文件
└── v1/
    ├── __init__.py            # v1 版本命名空间
    └── endpoints/
        ├── __init__.py        # endpoints 包入口
        ├── health.py          # 健康检查（GET /health）
        ├── auth.py            # 认证鉴权（register/login/refresh/logout/me）
        ├── models.py          # 模型管理（provider 列表、模型 CRUD）
        ├── knowledge_bases.py # 知识库管理（CRUD）
        ├── knowledge_tags.py  # 知识标签管理（CRUD，嵌套在 KB 下）
        ├── knowledges.py      # 知识条目（file/url/manual 导入、列表、详情、删除）
        ├── sessions.py        # 会话管理（CRUD、stop、continue-stream）
        ├── messages.py        # 消息管理（历史加载）
        ├── chat.py            # 知识对话（knowledge-chat SSE 流式）
        └── search.py          # 知识检索（knowledge-search）
```

## 文件说明与里程碑归属

| 文件                 | 职责                                        | 归属阶段   | 路由前缀           |
| -------------------- | ------------------------------------------- | ---------- | ------------------ |
| `router.py`          | 聚合全部 endpoint router，固定挂载顺序      | M1（骨架） | —                  |
| `deps.py`            | 提供 `ContainerDep` 等依赖注入工具          | M2         | —                  |
| `health.py`          | 健康检查探针                                | M1（骨架） | `/health`          |
| `auth.py`            | 注册/登录/刷新/登出/当前用户                | M2         | `/auth`            |
| `models.py`          | provider 列表、模型 CRUD                    | M3         | `/models`          |
| `knowledge_bases.py` | 知识库 CRUD                                 | M3         | `/knowledge-bases` |
| `knowledge_tags.py`  | 知识标签 CRUD（嵌套在 KB 下）               | M3         | 无前缀（见注①）    |
| `knowledges.py`      | 知识 file/url/manual 导入、列表、详情、删除 | M3         | 无前缀（见注②）    |
| `sessions.py`        | 会话 CRUD、stop、continue-stream            | M4         | `/sessions`        |
| `messages.py`        | 消息历史加载                                | M4         | `/messages`        |
| `chat.py`            | knowledge-chat SSE 流式对话                 | M4         | `/knowledge-chat`  |
| `search.py`          | knowledge-search 独立检索                   | M6         | 无前缀（见注③）    |

> **注①** `knowledge_tags.py` 的路由嵌套在 `/knowledge-bases/{id}/tags` 下，由路由装饰器指定完整路径。
>
> **注②** `knowledges.py` 的路由跨 `/knowledge-bases/{id}/knowledge/*` 和 `/knowledge/{id}` 两个前缀，
> 由路由装饰器指定完整路径。
>
> **注③** `search.py` 仅有 `POST /knowledge-search` 一条路由，由路由装饰器指定完整路径。

## 路由挂载设计

`router.py` 中 `api_router` 在 `main.py` 挂载时带 `/api/v1` 前缀，因此：
- `health.py` 的 `GET /health` 实际路径为 `GET /api/v1/health`
- `auth.py` 的路由实际路径为 `/api/v1/auth/*`
- 其余类推

## TODO
- TODO(M8)：补齐运行脚本与部署配置检查项，确保 `docker compose up` 后所有路由可访问。
- TODO(M8)：补齐日志、指标、追踪最小采集口径（request_id / latency / status_code）。

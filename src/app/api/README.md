# api/

## 概述

HTTP 接口层，负责路由注册与入参校验。

## 目录结构

```
api/
├── router.py       ← 路由聚合：汇总所有 v1 endpoint 并挂载到主 app
├── deps.py         ← 依赖注入工具：提供 get_db_session、get_current_user 等 FastAPI Depends
└── v1/
    └── endpoints/  ← 各域 endpoint（每个文件对应一组 REST 接口）
```

## 版本化策略

- 当前仅有 `v1/`。未来若需 breaking change，新增 `v2/` 目录并在 `router.py` 中按前缀挂载。
- 同一版本内所有 endpoint 共享 `/api/v1` 前缀。

## `deps.py` 的作用

集中管理 FastAPI 的 `Depends` 工厂函数，避免在每个 endpoint 文件中重复创建数据库 session、解析 JWT 等逻辑。

## TODO

- [api][M2] 在 `router.py` 中挂载 auth、model 路由
- [api][M3] 挂载 knowledge_base、knowledge、session 路由
- [api][M4+] 挂载 chat、search、message 路由

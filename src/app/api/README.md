# api/

## 文件职责
- 维护 HTTP 路由入口、版本管理和依赖注入契约。
- 确保 endpoint 与 schema/service 的映射关系清晰可追踪。

## 边界
- API 层只做协议转换与参数校验，不承载业务编排。
- 所有业务行为应下沉到 `services/`。

## 目录结构
```text
api/
├── router.py
├── deps.py
└── v1/endpoints/
```

## TODO
- [arch][P1][todo] 在 M1 固化 `router.py` 的路由聚合顺序与命名规则。
- [auth][P1][todo] 在 M2 接入认证相关 endpoint。
- [chat][P1][todo] 在 M4 接入 session/message/chat/search 相关 endpoint。

# api/

## 文件职责
- 维护 API 分层的入口约定与导出边界。

## 边界
- 只处理协议层入参与响应转换；上游接收 HTTP 请求，下游只调用 service 或依赖注入对象，不直接操作数据库。

## 目录结构
```text
api/
├── router.py
├── deps.py
└── v1/endpoints/
```

## TODO
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/api/README.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/api/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/api/README.md`。


## 协作矩阵
| 协作单元 | 输入依赖 | 输出产物 | 并行边界 | 主要阻塞点 |
|---|---|---|---|---|
| api | router/deps/schema | HTTP 协议与响应 | 可与 ui 并行 | service 契约未稳定 |
| services | api/worker 调用 | 业务编排结果 | 可与 repository 并行定义接口 | repository 能力缺口 |
| repositories | services 查询需求 | 持久化访问接口 | 可与 infra 并行 | 数据模型与索引未定 |
| infra | config/compose | 连接与资源实例 | 可独立推进 | 外部服务参数变化 |
| worker | queue/service | 异步任务执行结果 | 可与 api 并行 | ingest 链路未齐全 |
| ui | api 契约 | 页面与交互状态 | 可与后端并行联调 | API 字段不稳定 |

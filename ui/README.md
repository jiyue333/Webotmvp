# ui/

## 文件职责
- 维护前端目录协作说明，约束页面、状态、API 分工。

## 边界
- 只提供文档化约束与协作说明；上游供研发阅读，下游不作为运行时行为来源。

## 启动方式
```bash
cd ui
npm install
npm run dev
```

## TODO
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/README.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/README.md`。


## 协作矩阵
| 协作单元 | 输入依赖 | 输出产物 | 并行边界 | 主要阻塞点 |
|---|---|---|---|---|
| api | router/deps/schema | HTTP 协议与响应 | 可与 ui 并行 | service 契约未稳定 |
| services | api/worker 调用 | 业务编排结果 | 可与 repository 并行定义接口 | repository 能力缺口 |
| repositories | services 查询需求 | 持久化访问接口 | 可与 infra 并行 | 数据模型与索引未定 |
| infra | config/compose | 连接与资源实例 | 可独立推进 | 外部服务参数变化 |
| worker | queue/service | 异步任务执行结果 | 可与 api 并行 | ingest 链路未齐全 |
| ui | api 契约 | 页面与交互状态 | 可与后端并行联调 | API 字段不稳定 |

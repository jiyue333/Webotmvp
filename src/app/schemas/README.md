# schemas/

## 文件职责
- 定义 `README.md` 领域 DTO 与校验结构，约束接口输入输出类型。

## 边界
- 只提供文档化约束与协作说明；上游供研发阅读，下游不作为运行时行为来源。

## 命名约定
- `Create`：创建入参
- `Update`：更新入参
- `Detail`：详情响应
- `ListItem`：列表项响应
- `Query`：查询参数

## TODO
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/schemas/README.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/schemas/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/schemas/README.md`。

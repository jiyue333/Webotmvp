# middleware/

## 文件职责
- 承载 `README.md` 请求链路中间件职责，控制横切能力注入顺序。

## 边界
- 只处理横切关注点；上游由应用入口注册，下游传递给后续中间件或路由，不执行业务领域逻辑。

## 推荐顺序
1. `request_id.py`
2. `trace.py`
3. `logger.py`
4. `recovery.py`
5. `error_handler.py`
6. `auth.py`

## TODO
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/middleware/README.md`。
- [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/middleware/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/middleware/README.md`。

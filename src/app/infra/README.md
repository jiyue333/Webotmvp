# infra/

## 文件职责
- 维护外部依赖连接生命周期（初始化、获取、关闭）。
- 向上层提供统一连接访问入口。

## 边界
- 仅负责连接管理，不处理业务逻辑。
- 不直接读取散落环境变量，统一走 `common/config.py`。

## TODO
- [arch][P1][todo] 在 M1 固化 DB/Redis/Neo4j/Storage 的生命周期函数模板。
- [worker][P2][todo] 在 M5 支撑 ingest 任务的连接复用与重试策略。
- [obs][P2][todo] 在 M8 增加连接状态指标与异常日志字段。

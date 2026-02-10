"""
文件职责：定义 `base` 持久化模型结构，约束字段语义与存储映射。
边界：只负责持久化读写与查询封装；上游由 service 调用，下游连接数据库/检索引擎，不实现业务决策。
TODO：
- [model][P1][todo] 完成条件：补齐模型提供商与模型 CRUD 最小闭环；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/repositories/models/base.py`。
"""


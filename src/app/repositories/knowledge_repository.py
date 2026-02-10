"""
文件职责：提供 `knowledge_repository` 数据访问接口，屏蔽业务层对持久化细节的直接依赖。
边界：只负责持久化读写与查询封装；上游由 service 调用，下游连接数据库/检索引擎，不实现业务决策。
TODO：
- [knowledge][P1][todo] 完成条件：补齐知识条目管理与状态流转约束；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/repositories/knowledge_repository.py`。
"""


"""
文件职责：提供 `neo4j_repository` 检索存储访问能力，承接检索链路的数据查询。
边界：只负责持久化读写与查询封装；上游由 service 调用，下游连接数据库/检索引擎，不实现业务决策。
TODO：
- [retrieval][P2][todo] 完成条件：补齐混合检索查询与召回接口；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/repositories/retriever/neo4j_repository.py`。
"""


"""
文件职责：维护 `neo4j_client` 外部依赖连接能力，统一资源初始化与释放。
边界：只负责外部连接初始化与访问；上游提供给 container/repository 使用，不承载业务状态流转。
TODO：
- [graph][P2][todo] 完成条件：补齐实体抽取与图检索增强策略；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/infra/neo4j_client.py`。
"""


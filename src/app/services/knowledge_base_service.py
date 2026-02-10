"""
文件职责：承载 `knowledge_base_service` 业务域的服务编排职责，协调上层请求与下层数据访问。
边界：只负责业务编排与流程控制；上游由 api/worker 调用，下游依赖 repository/client，不直接处理 HTTP 协议。
TODO：
- [kb][P1][todo] 完成条件：补齐知识库 CRUD 与归属关系约束；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/services/knowledge_base_service.py`。
"""


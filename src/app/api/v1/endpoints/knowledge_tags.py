"""
文件职责：定义 `knowledge_tags` 领域接口的协议入口与参数边界。
边界：只处理协议层入参与响应转换；上游接收 HTTP 请求，下游只调用 service 或依赖注入对象，不直接操作数据库。
TODO：
- [knowledge][P1][todo] 完成条件：补齐知识条目管理与状态流转约束；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/api/v1/endpoints/knowledge_tags.py`。
"""


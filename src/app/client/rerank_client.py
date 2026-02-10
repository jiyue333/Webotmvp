"""
文件职责：封装 `rerank_client` 外部模型调用入口，统一请求参数与错误处理约束。
边界：只封装外部模型请求；上游由 service 调用，下游对接第三方模型服务，不保存业务数据。
TODO：
- [rerank][P2][todo] 完成条件：补齐重排调用与结果融合规则；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/client/rerank_client.py`。
"""


"""
文件职责：承载 chat pipeline 的 `rerank` 步骤职责，明确该步骤输入输出契约。
边界：只负责业务编排与流程控制；上游由 api/worker 调用，下游依赖 repository/client，不直接处理 HTTP 协议。
TODO：
- [rerank][P2][todo] 完成条件：补齐重排调用与结果融合规则；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/services/chat_pipeline/rerank.py`。
"""


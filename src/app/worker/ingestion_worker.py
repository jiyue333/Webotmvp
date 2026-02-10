"""
文件职责：承载 worker 子模块 `ingestion_worker` 的任务消费与处理职责。
边界：只处理异步任务消费与状态回写；上游来自队列，下游调用 service/repository，不提供对外 HTTP 接口。
TODO：
- [worker][P2][todo] 完成条件：补齐队列消费、重试与状态更新机制；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/worker/ingestion_worker.py`。
"""


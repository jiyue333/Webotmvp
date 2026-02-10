"""
文件职责：维护流式事件管理入口，承接 SSE/消息流推送基础能力。
边界：只处理流式推送基础设施；上游由 chat/session 调用，下游对接流存储或连接管理，不生成业务内容。
TODO：
- [sse][P1][todo] 完成条件：补齐事件流推送与续流边界；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/stream/redis_manager.py`。
"""


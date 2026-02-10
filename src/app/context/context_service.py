"""
文件职责：维护对话上下文管理入口，约束上下文读取与更新边界。
边界：只管理上下文读写接口；上游由 chat 流程调用，下游可依赖缓存存储，不承担对话生成逻辑。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/context/context_service.py`。
"""


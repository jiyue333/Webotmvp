"""
文件职责：维护 `redis` 外部依赖连接能力，统一资源初始化与释放。
边界：只负责外部连接初始化与访问；上游提供给 container/repository 使用，不承载业务状态流转。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/infra/redis.py`。
"""


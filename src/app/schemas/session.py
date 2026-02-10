"""
文件职责：定义 `session` 领域 DTO 与校验结构，约束接口输入输出类型。
边界：只描述本文件边界与上下游关系；不在此实现跨阶段业务闭环。
TODO：
- [session][P1][todo] 完成条件：补齐会话生命周期管理与停止语义；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/schemas/session.py`。
"""


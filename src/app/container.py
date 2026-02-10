"""
文件职责：维护应用容器与资源生命周期编排，统一依赖实例管理。
边界：只管理容器与资源生命周期；上游由应用入口调用，下游服务/仓储依赖该容器，不承载业务规则。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/container.py`。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AppContainer:
    """应用依赖容器（M1 最小实现）。"""

    resources: dict[str, Any] = field(default_factory=dict)
    started: bool = False

    async def startup(self) -> None:
        """初始化应用级资源。"""
        self.started = True

    async def shutdown(self) -> None:
        """释放应用级资源。"""
        self.resources.clear()
        self.started = False


_container = AppContainer()


def get_container_instance() -> AppContainer:
    """返回全局容器实例。"""
    return _container

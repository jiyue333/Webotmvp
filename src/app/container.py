"""
文件职责：维护 `src/app/container.py` 的应用容器骨架与生命周期编排入口。
边界：仅提供 M1 阶段的最小依赖容器能力，不在此实现具体业务服务注册与装配。
TODO：
- [arch][P1][todo] 在 M1 补齐 infra/client/service 的显式装配顺序与生命周期清单。
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

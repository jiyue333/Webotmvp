"""
文件职责：维护 `src/app/api/deps.py` 的 FastAPI 依赖注入入口。
边界：仅提供跨 endpoint 共享的公共依赖，不在此承担业务校验与编排逻辑。
TODO：
- [arch][P1][todo] 在 M1 固化 get_db_session/get_current_user 等依赖签名并对齐路由层约定。
"""

from __future__ import annotations

from typing import Annotated

from fastapi import Depends, Request

from app.container import AppContainer, get_container_instance


def get_container(request: Request) -> AppContainer:
    """从应用状态中读取容器实例，缺失时回退到全局容器。"""
    container = getattr(request.app.state, "container", None)
    if isinstance(container, AppContainer):
        return container
    return get_container_instance()


ContainerDep = Annotated[AppContainer, Depends(get_container)]

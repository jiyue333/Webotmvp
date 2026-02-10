"""
文件职责：提供 API 层依赖注入入口，统一容器与上下文获取方式。
边界：只处理协议层入参与响应转换；上游接收 HTTP 请求，下游只调用 service 或依赖注入对象，不直接操作数据库。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/api/deps.py`。
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

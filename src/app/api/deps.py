# 文件职责：提供 API 层依赖注入入口，统一容器与上下文获取方式。
# 边界：仅暴露依赖注入工具函数与类型别名（如 ContainerDep），不定义路由、不处理请求参数、不包含业务逻辑。

from __future__ import annotations

import os
from typing import Annotated

from fastapi import Depends, Request

from app.container import AppContainer, get_container_instance


def get_container(request: Request) -> AppContainer:
    """从应用状态中读取容器实例。
    生产环境下容器必须由 lifespan 注入到 app.state，缺失时直接抛异常以暴露初始化问题。
    仅当环境变量 TESTING=1 时允许回退到全局单例（用于单元测试绕过 lifespan）。
    """
    container = getattr(request.app.state, "container", None)
    if isinstance(container, AppContainer):
        return container
    if os.getenv("TESTING") == "1":
        return get_container_instance()
    raise RuntimeError(
        "AppContainer 未在 app.state 中找到，请检查 lifespan 是否正确初始化容器。"
    )


ContainerDep = Annotated[AppContainer, Depends(get_container)]

# TODO(M2)：新增 get_current_user 依赖函数。解析请求 Authorization header 中的 JWT，提取 user_id，查询并返回用户对象。
# TODO(M2)：新增 CurrentUserDep 类型别名。方便 endpoint 通过 user: CurrentUserDep 一行代码获取当前登录用户。
# TODO(M2)：新增 get_db_session 依赖函数。创建请求级 SQLAlchemy AsyncSession，请求结束后自动关闭连接。

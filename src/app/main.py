"""
文件职责：装配 FastAPI 应用生命周期与路由入口，提供服务启动主入口。
边界：只负责应用装配与生命周期管理；上游由进程启动调用，下游注入 router/container，不承载领域实现。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/main.py`。
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.container import get_container_instance


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期：初始化容器并在退出时释放资源。"""
    container = get_container_instance()
    await container.startup()
    app.state.container = container
    try:
        yield
    finally:
        await container.shutdown()


app = FastAPI(title="Webot MVP API", version="0.1.0", lifespan=lifespan)
app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    """根路径健康检查（运维探针）。"""
    return {"status": "ok"}

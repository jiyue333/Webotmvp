"""
文件职责：维护 `src/app/main.py` 的 FastAPI 应用入口与生命周期编排。
边界：仅负责应用装配与启动入口，不承载领域业务逻辑实现。
TODO：
- [arch][P1][todo] 在 M1 固化中间件注册顺序与全局异常处理策略。
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

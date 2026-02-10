"""
文件职责：FastAPI 应用入口。
TODO：后续在此注册中间件、路由版本和全局异常处理。
"""

from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(title="Webot MVP API", version="0.1.0")
app.include_router(api_router, prefix="/api/v1")


@app.get("/health")
def health() -> dict[str, str]:
    """健康检查接口。"""
    return {"status": "ok"}

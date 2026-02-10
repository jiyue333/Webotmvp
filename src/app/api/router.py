"""
文件职责：维护 `src/app/api/router.py` 的 API 路由聚合与挂载顺序。
边界：仅负责路由编排，不承担具体 endpoint 的业务处理逻辑。
TODO：
- [arch][P1][todo] 在 M1 按域拆分并接入 auth/model/kb/session/chat 路由。
"""

from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)

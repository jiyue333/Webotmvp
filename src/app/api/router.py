"""
文件职责：聚合 API 路由并固定挂载顺序，作为 HTTP 入口编排点。
边界：只处理协议层入参与响应转换；上游接收 HTTP 请求，下游只调用 service 或依赖注入对象，不直接操作数据库。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/api/router.py`。
"""

from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router

api_router = APIRouter()
api_router.include_router(health_router)

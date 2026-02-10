"""
文件职责：维护 `src/app/api/v1/endpoints/health.py` 的版本化健康检查端点。
边界：仅暴露服务可用性探针，不承载业务域逻辑与外部依赖连通性检测。
TODO：
- [arch][P1][todo] 在 M1 完成 `/api/v1/health` 与根 `/health` 的一致性验收。
"""

from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict[str, str]:
    """API 版本前缀下的健康检查。"""
    return {"status": "ok"}

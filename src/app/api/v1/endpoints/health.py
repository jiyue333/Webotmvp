# 文件职责：定义健康检查路由，提供服务可用性探针。
# 边界：不依赖业务 Service 或数据库，仅返回固定状态，用于 Docker 探活与 CI 冒烟测试。

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    """API 版本前缀下的健康检查。"""
    return {"status": "ok"}

# TODO(M8)：扩展健康检查，增加 PostgreSQL、Redis、Neo4j 连通性探测。各组件不可用时返回降级状态而非 500。

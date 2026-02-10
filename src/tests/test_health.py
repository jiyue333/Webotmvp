"""
文件职责：维护 `src/tests/test_health.py` 的健康检查回归用例。
边界：仅验证 M1 最小可运行健康接口，不覆盖业务域 API 行为。
TODO：
- [test][P2][todo] 在 M8 将 smoke 覆盖扩展到 auth/ingest/retrieval/chat 主链路。
"""


def test_health_root(client) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_api_v1(client) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

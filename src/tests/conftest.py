"""
文件职责：维护 `src/tests/conftest.py` 的测试夹具与全局测试配置。
边界：仅提供测试运行期公共依赖，不在此定义具体业务断言。
TODO：
- [test][P2][todo] 在 M8 补齐集成测试环境夹具（数据库/Redis/Neo4j）。
"""

from __future__ import annotations

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client() -> Generator[TestClient, None, None]:
    """提供 FastAPI TestClient。"""
    with TestClient(app) as test_client:
        yield test_client

"""
文件职责：维护测试夹具与回归用例，验证最小运行链路稳定性。
边界：只描述测试行为与断言；上游由测试命令触发，下游调用应用接口，不承载生产业务逻辑。
TODO：
- [test][P2][todo] 完成条件：补齐模块级测试覆盖并固定回归路径；验证方式：执行 `cd src && python -m pytest -q` 并通过；归属模块：`src/tests/conftest.py`。
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

"""
文件职责：维护测试夹具与回归用例，验证最小运行链路稳定性。
边界：只描述测试行为与断言；上游由测试命令触发，下游调用应用接口，不承载生产业务逻辑。
TODO：
- [test][P2][todo] 完成条件：补齐模块级测试覆盖并固定回归路径；验证方式：执行 `cd src && python -m pytest -q` 并通过；归属模块：`src/tests/test_health.py`。
"""

def test_health_root(client) -> None:
    """执行 `test_health_root` 逻辑。

    输入：按函数签名参数接收。
    输出：返回当前函数声明对应的数据结果。
    副作用：可能读取或更新进程内状态与外部依赖。
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_api_v1(client) -> None:
    """执行 `test_health_api_v1` 逻辑。

    输入：按函数签名参数接收。
    输出：返回当前函数声明对应的数据结果。
    副作用：可能读取或更新进程内状态与外部依赖。
    """
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

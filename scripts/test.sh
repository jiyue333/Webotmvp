#!/usr/bin/env bash
# 文件职责：维护 `scripts/test.sh` 的后端测试执行入口。
# 边界：仅执行 pytest，不负责任务编排、数据准备和测试报告聚合。
# TODO：
# - [test][P2][todo] 在 M8 增加 smoke/regression 分层测试执行选项。

set -euo pipefail

cd src
pytest -q

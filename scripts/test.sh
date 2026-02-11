#!/usr/bin/env bash
# 文件职责：执行后端单元测试，自动切换到 src/ 目录运行 pytest，供本地开发和 CI 调用。
# 边界：仅执行测试；不做 lint 或构建（由 lint.sh 和 Dockerfile 负责）。

# TODO(M1)：实现测试执行。`set -euo pipefail && cd src && pytest -q`。

#!/usr/bin/env bash
# 文件职责：执行后端代码质量检查，包括 Python 编译检查（compileall）和 ruff lint，供本地开发和 CI 调用。
# 边界：仅执行静态检查；不修改代码（ruff 不加 --fix）；不运行测试（由 test.sh 负责）。

# TODO(M1)：实现编译检查。`python -m compileall -q src/app`，验证所有 .py 文件无语法错误。
# TODO(M1)：实现 ruff check。`cd src && ruff check app tests`，若 ruff 未安装则跳过并打印提示。

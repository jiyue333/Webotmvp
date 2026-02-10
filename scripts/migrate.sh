#!/usr/bin/env bash
# 文件职责：封装 `migrate.sh` 对应的开发运维命令，减少重复操作与误用风险。
# 边界：只封装命令入口与流程控制；上游由开发者执行，下游调用系统工具，不定义业务规则。
# TODO：
# - [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：执行 `bash -n scripts/*.sh` 并通过脚本分支自检；归属模块：`scripts/migrate.sh`。

set -euo pipefail

cd src
alembic "$@"

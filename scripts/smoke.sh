#!/usr/bin/env bash
# 文件职责：执行最小化冒烟测试，验证应用健康检查端点可正常响应，作为部署后快速验证手段。对齐 mvp.md §5.3 健康检查。
# 边界：仅验证 /health 端点可达且响应含 status 字段；不执行业务链路测试（完整 smoke test 由 M8 补充）。

# TODO(M1)：实现健康检查验证。curl GET /health，检查响应体包含 "status" 字段，失败则 exit 1。
# TODO(M8)：扩展为完整 API smoke test。覆盖登录→导入→检索→对话链路。

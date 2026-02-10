# 文件职责：定义消息管理相关的 HTTP 路由（消息历史加载）。
# 边界：仅处理请求参数校验与响应封装，消息持久化与查询委托给 MessageService，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M4)：实现 GET /{session_id}/load 消息历史加载端点。接收 before_id（可选，用于向上翻页）和 limit（默认 20），调用 MessageService.load()，返回按时间倒序排列的消息列表。

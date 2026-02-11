# 文件职责：定义会话管理相关的 HTTP 路由（CRUD、stop、continue-stream）。
# 边界：仅处理请求参数校验与响应封装，会话生命周期与流控逻辑委托给 SessionService 和 StreamManager，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M4)：实现 POST / 创建会话端点。接收 kb_id 和可选 title，调用 SessionService.create()，返回新会话信息。
# TODO(M4)：实现 GET / 会话列表端点。返回当前用户的所有会话，按最后活跃时间倒序排列。
# TODO(M4)：实现 GET /{id} 会话详情端点。返回会话信息及关联的知识库摘要。
# TODO(M4)：实现 PUT /{id} 更新会话端点。接收可选的 title，调用 SessionService.update()。
# TODO(M4)：实现 DELETE /{id} 删除会话端点。调用 SessionService.delete()，级联删除关联消息。
# TODO(M4)：实现 POST /{session_id}/stop 停止会话端点。向 StreamManager 发送 stop 事件，中断正在进行的流式生成。
# TODO(M4)：实现 GET /continue-stream/{session_id} 续流端点。从请求 Header 读取 Last-Event-ID（SSE 标准，浏览器断线重连自动携带），调用 StreamManager.get_events_after(after_event_id) 回放断点之后的事件并继续推送增量。对齐 mvp.md §4.2.4 API 定义。

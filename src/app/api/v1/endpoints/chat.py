# 文件职责：定义知识对话相关的 HTTP 路由（knowledge-chat SSE 流式接口）。
# 边界：仅接收对话请求并转发给 ChatPipeline/SessionService，流式响应由 StreamManager 驱动，本模块不含检索或 LLM 调用逻辑。

from fastapi import APIRouter

router = APIRouter()

# TODO(M4)：实现 POST /{session_id} SSE 流式端点。接收 query 文本和可选参数（temperature 等），触发 ChatPipeline，通过 StreamingResponse 推送 answer/references 事件流。

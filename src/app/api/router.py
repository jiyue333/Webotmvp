# 文件职责：聚合所有 v1 endpoint 路由并固定挂载顺序，作为 HTTP 入口编排点。
# 边界：只做路由注册与前缀/标签配置，不包含请求处理逻辑或业务编排。

from fastapi import APIRouter

from app.api.v1.endpoints.auth import router as auth_router
from app.api.v1.endpoints.chat import router as chat_router
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.knowledge_bases import router as kb_router
from app.api.v1.endpoints.knowledge_tags import router as tags_router
from app.api.v1.endpoints.knowledges import router as knowledges_router
from app.api.v1.endpoints.messages import router as messages_router
from app.api.v1.endpoints.models import router as models_router
from app.api.v1.endpoints.search import router as search_router
from app.api.v1.endpoints.sessions import router as sessions_router

api_router = APIRouter()

# ---------- 基础设施 ----------
api_router.include_router(health_router, tags=["health"])

# ---------- 认证鉴权（M2） ----------
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])

# ---------- 模型管理（M3） ----------
api_router.include_router(models_router, prefix="/models", tags=["models"])

# ---------- 知识库管理（M3） ----------
api_router.include_router(kb_router, prefix="/knowledge-bases", tags=["knowledge-bases"])

# ---------- 知识标签管理（M3） ----------
# 路由嵌套在 /knowledge-bases/{id}/tags 下，不设统一 prefix，由路由装饰器指定完整路径。
api_router.include_router(tags_router, tags=["knowledge-tags"])

# ---------- 知识条目管理（M3） ----------
# 路由跨两个路径前缀（/knowledge-bases/{id}/knowledge/* 和 /knowledge/{id}），
# 不设统一 prefix，由路由装饰器指定完整路径。
api_router.include_router(knowledges_router, tags=["knowledges"])

# ---------- 会话管理（M4） ----------
api_router.include_router(sessions_router, prefix="/sessions", tags=["sessions"])

# ---------- 消息管理（M4） ----------
api_router.include_router(messages_router, prefix="/messages", tags=["messages"])

# ---------- 知识对话（M4） ----------
api_router.include_router(chat_router, prefix="/knowledge-chat", tags=["chat"])

# ---------- 知识检索（M6） ----------
api_router.include_router(search_router, tags=["search"])

# TODO(M2)：验证所有 endpoint router 的挂载前缀和标签与 mvp.md 4.2 API 设计表一致。启动后访问 /docs 确认路由列表完整。

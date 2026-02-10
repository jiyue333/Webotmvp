# 文件职责：定义知识检索相关的 HTTP 路由（POST /knowledge-search 独立检索接口）。
# 边界：仅处理请求参数校验与响应封装，检索与重排逻辑委托给 RetrieverService，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M6)：实现 POST /knowledge-search 独立检索端点。接收 query/kb_id/top_k（默认 5），执行 pgvector 向量检索 + pg_search 关键词检索，经 Rerank 模型重排后返回带相似度分数的文档片段列表。

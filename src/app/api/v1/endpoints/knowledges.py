# 文件职责：定义知识条目管理相关的 HTTP 路由（file/url/manual 导入、列表、详情、删除）。
# 边界：仅处理请求参数校验与响应封装，知识入库与状态流转委托给 KnowledgeService 和 Worker，不直接操作数据库。
# 注意：本模块路由跨两个路径前缀（/knowledge-bases/{id}/knowledge/* 和 /knowledge/{id}），
#       因此在 router.py 中不设统一 prefix，由各路由装饰器指定完整路径。

from fastapi import APIRouter

router = APIRouter()

# TODO(M3)：实现 POST /knowledge-bases/{id}/knowledge/file 文件导入端点。接收上传文件（UploadFile），创建 knowledge 记录（状态 pending），存储文件到 MinIO/本地，投递 Redis 解析任务。
# TODO(M3)：实现 POST /knowledge-bases/{id}/knowledge/url URL 导入端点。接收 URL 字符串，创建 knowledge 记录（状态 pending），投递 Redis 抓取任务。
# TODO(M3)：实现 POST /knowledge-bases/{id}/knowledge/manual 手工录入端点。接收 title + Markdown 内容，创建 knowledge 记录并直接进入分块流程。
# TODO(M3)：实现 GET /knowledge-bases/{id}/knowledge 知识列表端点。支持分页和 tag_id 筛选，返回该知识库下的知识条目及 parse_status。
# TODO(M3)：实现 GET /knowledge/{id} 知识详情端点。返回单条知识的完整信息、解析状态和分块统计。
# TODO(M3)：实现 DELETE /knowledge/{id} 删除知识端点。软删除 knowledge 记录，异步清理关联的 chunks/embeddings。

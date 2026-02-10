# 文件职责：定义知识库管理相关的 HTTP 路由（CRUD：创建、列表、详情、更新、删除）。
# 边界：仅处理请求参数校验与响应封装，知识库业务逻辑委托给 KBService，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M3)：实现 POST / 创建知识库端点。接收 name/description/embedding_model_id 等配置，调用 KBService.create()，返回新建知识库信息。
# TODO(M3)：实现 GET / 知识库列表端点。支持分页参数 page/page_size，调用 KBService.list()，返回知识库列表与总数。
# TODO(M3)：实现 GET /{id} 知识库详情端点。调用 KBService.get_by_id()，返回单个知识库的完整信息。
# TODO(M3)：实现 PUT /{id} 更新知识库端点。接收可选的 name/description 等字段，调用 KBService.update()。
# TODO(M3)：实现 DELETE /{id} 删除知识库端点。调用 KBService.delete()，级联处理关联的知识条目和标签。

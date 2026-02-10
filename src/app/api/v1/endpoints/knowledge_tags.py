# 文件职责：定义知识标签管理相关的 HTTP 路由（CRUD：列表、创建、更新、删除）。
# 边界：仅处理请求参数校验与响应封装，标签挂载在知识库下（/knowledge-bases/{id}/tags），业务逻辑委托给 TagService，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M3)：实现 GET /knowledge-bases/{id}/tags 标签列表端点。返回指定知识库下的所有标签，含每个标签关联的知识数量。
# TODO(M3)：实现 POST /knowledge-bases/{id}/tags 创建标签端点。接收 name/color/sort_order，调用 TagService.create()，同一知识库下 name 唯一。
# TODO(M3)：实现 PUT /knowledge-bases/{id}/tags/{tag_id} 更新标签端点。接收可选的 name/color/sort_order，调用 TagService.update()。
# TODO(M3)：实现 DELETE /knowledge-bases/{id}/tags/{tag_id} 删除标签端点。调用 TagService.delete()，将关联知识的 tag_id 置空。

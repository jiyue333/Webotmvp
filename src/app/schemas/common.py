# 文件职责：定义通用/共享 schema，包括分页查询参数 PaginationQuery、排序参数等跨域 DTO。
# 边界：只定义跨模块复用的 schema；模块专属 schema 在各模块文件中定义。统一响应壳已由 common/response.py 负责，此处不重复定义。

# TODO(M2)：定义 PaginationQuery(BaseModel)，包含 page: int = 1, page_size: int = 20 字段，添加取值范围校验（1 <= page, 1 <= page_size <= 100）。
# TODO(M3)：定义 IDPath(BaseModel)，用于路径参数 {id} 的 UUID 格式校验。

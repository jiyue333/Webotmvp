# 文件职责：定义统一 API 响应壳，供 api 层包装 service 返回值。对齐 mvp.md §4.3.1。
# 边界：只定义响应数据结构（Pydantic 模型）和辅助工厂函数；不处理 HTTP 异常、不依赖 service 层。

# TODO(M2)：定义 ApiResponse[T] 泛型模型，包含 success: bool, data: T, request_id: str 字段。提供 success_response() 工厂函数。
# TODO(M2)：定义 PaginatedData[T] 泛型模型，包含 items: list[T], total: int, page: int, page_size: int 字段。
# TODO(M2)：定义 ErrorDetail 模型，包含 code: int, message: str, details: dict 字段。提供 error_response() 工厂函数。

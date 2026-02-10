# 文件职责：API 包入口，控制包级导出边界。
# 边界：仅作为包声明，不包含路由定义或业务逻辑。

# TODO(M2)：在各 endpoint 中使用 common.response 中的 ApiResponse 和 PaginatedData 包装 service 返回值。

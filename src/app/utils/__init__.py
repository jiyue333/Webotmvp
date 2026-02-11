# 文件职责：utils 包入口；统一导出通用工具函数，供各层模块按需 import。
# 边界：仅控制包级导出边界；不实现业务逻辑，不依赖 service / repository 层对象。

# TODO(M2)：按需导出 json / sanitize / file_size 等工具模块的核心函数。

# 文件职责：splitter 子包入口；统一导出分块器和标题追踪器，供 parser 层调用。
# 边界：仅做符号导出，不包含分块逻辑。

# TODO(M5)：在分块器实现完成后，导出 TextSplitter, HeaderHook。

# 文件职责：context 包入口；导出 ContextManager 协议与工厂函数，供 chat_pipeline / session service 使用。
# 边界：仅做 re-export，不包含实现逻辑。

# TODO(M4)：导出 ContextManager 协议、ContextStats 数据类、create_context_manager() 工厂函数。

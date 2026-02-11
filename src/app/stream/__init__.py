# 文件职责：stream 包入口；统一导出 StreamManager 协议、StreamEvent 和工厂函数，供 chat_pipeline / handler 层使用。
# 边界：仅控制包级导出边界；不实现具体的流管理逻辑，不直接依赖 Redis 客户端。

# TODO(M4)：导出 StreamManager / StreamEvent / create_stream_manager 等核心符号。

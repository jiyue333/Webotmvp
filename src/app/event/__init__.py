# 文件职责：event 包入口；统一导出事件类型、事件数据结构与 EventBus，供 chat_pipeline / service / worker 层使用。
# 边界：仅控制包级导出边界；不实现任何事件处理逻辑，不直接依赖 infra 层。

# TODO(M4)：导出 EventBus / EventType / Event 等核心符号，供 chat 和 session 模块 import 使用。

# 文件职责：标题层级追踪器 HeaderHook，在分块过程中维护当前标题栈，使每个 chunk 保留所属章节上下文。
# 边界：仅负责标题识别与栈管理；由 TextSplitter 在分块时调用，不直接参与分块逻辑。

# TODO(M5)：定义 HeaderHook 类。__init__ 初始化 _header_stack: list[str] 空列表。
# TODO(M5)：实现 update(text: str) 方法，匹配 Markdown 标题语法（# ~ ######），按层级弹栈再压栈更新标题栈。
# TODO(M5)：实现 get_context() -> str 方法，将 _header_stack 用 " > " 拼接返回，如 "第一章 > 1.1 概述"。

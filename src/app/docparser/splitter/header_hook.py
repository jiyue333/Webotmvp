"""
文件职责：标题层级追踪钩子，在分块过程中为每个 chunk 记录其所属的标题上下文。
边界：仅追踪 Markdown 标题层级（# / ## / ###），不负责分块逻辑本身。
来源对齐：WeKnora docreader/splitter/header_hook.py
TODO [docparser][M5] 实现标题层级解析与上下文追踪。
"""
import re
from typing import Dict, List, Optional


class HeaderHook:
    """
    标题层级追踪器。

    在文本分块过程中被调用，维护当前的标题栈，
    使每个 chunk 都能知道自己属于哪个章节/小节。

    示例标题栈：["# 第一章", "## 1.1 概述"]
    """

    def __init__(self):
        self._header_stack: List[str] = []

    def update(self, text: str) -> None:
        """
        扫描文本中的标题行，更新标题栈。

        Args:
            text: 当前正在处理的文本片段。
        """
        # TODO [docparser][M5] 实现标题层级识别与栈更新
        pass

    def get_context(self) -> str:
        """
        返回当前标题上下文字符串（用于注入到 chunk 的 metadata 中）。

        Returns:
            标题上下文，如 "第一章 > 1.1 概述"。
        """
        # TODO [docparser][M5] 拼接标题栈为上下文字符串
        return " > ".join(self._header_stack) if self._header_stack else ""

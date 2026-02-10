"""
文件职责：文本分块器，将长文本切分为可检索的 chunk。
边界：负责分块算法（chunk_size、overlap、保护模式）；不负责文件解析。
来源对齐：WeKnora docreader/splitter/splitter.py（TextSplitter 类）
TODO [docparser][M5] 实现完整的 split_text 方法，支持受保护模式（表格、代码块、公式不被切断）。
"""
import logging
from typing import Callable, List, Optional, Tuple

logger = logging.getLogger(__name__)

# 默认分块参数
DEFAULT_CHUNK_SIZE = 512
DEFAULT_CHUNK_OVERLAP = 100


class TextSplitter:
    """
    文本分块器。

    支持：
    - 可配置的 chunk_size 和 overlap
    - 受保护的正则模式（表格、代码块、数学公式不会被切断）
    - 标题层级追踪（通过 HeaderHook 为每个 chunk 保留上下文标题）
    - 多级分隔符优先级（\\n\\n → \\n → 。→ ，→ 空格）
    """

    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
        separators: Optional[List[str]] = None,
        protected_patterns: Optional[List[str]] = None,
        length_function: Callable[[str], int] = len,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", "。", "？", "！", "，", " "]
        self.protected_patterns = protected_patterns or []
        self.length_function = length_function

    def split_text(self, text: str) -> List[Tuple[int, int, str]]:
        """
        将文本分块。

        Args:
            text: 输入文本。

        Returns:
            分块列表，每项为 (start_pos, end_pos, chunk_text)。
        """
        # TODO [docparser][M5] 实现完整分块逻辑
        raise NotImplementedError

    @staticmethod
    def restore_text(chunks: List[Tuple[int, int, str]]) -> str:
        """
        从分块结果还原原始文本（用于验证分块正确性）。

        Args:
            chunks: split_text 返回的分块列表。

        Returns:
            还原后的文本。
        """
        # TODO [docparser][M5] 实现文本还原（对齐 WeKnora TextSplitter.restore_text）
        raise NotImplementedError

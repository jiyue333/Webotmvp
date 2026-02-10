"""
文件职责：Markdown 文件解析器。
边界：负责 Markdown 文本 → 标准化 Markdown 的清洗与预处理；保留标题层级结构供 splitter 使用。
来源对齐：WeKnora docreader/parser/markdown_parser.py
TODO [docparser][M5] 实现 Markdown 解析（标题层级追踪、图片链接提取）。
"""
from app.docparser.parsers.base_parser import BaseParser


class MarkdownParser(BaseParser):
    """Markdown 文件解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现 Markdown 解析
        raise NotImplementedError

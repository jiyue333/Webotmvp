"""
文件职责：纯文本文件解析器。
边界：负责纯文本（.txt）的编码检测与内容读取；最简单的解析器。
来源对齐：WeKnora docreader/parser/text_parser.py
TODO [docparser][M5] 实现文本编码检测（chardet）和内容读取。
"""
from app.docparser.parsers.base_parser import BaseParser


class TextParser(BaseParser):
    """纯文本文件解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现纯文本解析（编码检测 + 读取）
        raise NotImplementedError

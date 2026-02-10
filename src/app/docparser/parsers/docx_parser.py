"""
文件职责：Word 文档（.docx）解析器。
边界：负责 DOCX 二进制内容 → Markdown 文本的转换；表格、图片等富内容需特殊处理。
来源对齐：WeKnora docreader/parser/docx_parser.py
TODO [docparser][M5] 使用 python-docx 实现文本提取；处理表格、图片、标题层级。
"""
from app.docparser.parsers.base_parser import BaseParser


class DocxParser(BaseParser):
    """Word 文档（.docx）解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现 DOCX 文本提取
        raise NotImplementedError

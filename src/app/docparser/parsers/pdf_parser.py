"""
文件职责：PDF 文档解析器。
边界：负责 PDF 二进制内容 → Markdown 文本的转换；图片提取走 OCR 流程。
来源对齐：WeKnora docreader/parser/pdf_parser.py
TODO [docparser][M5] 使用 PyMuPDF 或 pdfplumber 实现文本提取；支持扫描件走 OCR 路径。
"""
from app.docparser.parsers.base_parser import BaseParser


class PDFParser(BaseParser):
    """PDF 文档解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现 PDF 文本提取
        raise NotImplementedError

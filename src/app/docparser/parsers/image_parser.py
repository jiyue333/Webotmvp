"""
文件职责：图片文件解析器（纯图片 → OCR 文本）。
边界：负责图片文件的文本提取；核心依赖 OCR 引擎。
来源对齐：WeKnora docreader/parser/image_parser.py
TODO [docparser][M5] 调用 OCR engine 实现图片文字提取。
"""
from app.docparser.parsers.base_parser import BaseParser


class ImageParser(BaseParser):
    """图片文件解析器（OCR）。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现图片 OCR 文本提取
        raise NotImplementedError

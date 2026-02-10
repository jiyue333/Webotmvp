"""
文件职责：CSV 文件解析器。
边界：负责 CSV → Markdown 表格的转换。
来源对齐：WeKnora docreader/parser/csv_parser.py
TODO [docparser][M5] 使用 csv 模块实现解析，输出 Markdown 表格格式。
"""
from app.docparser.parsers.base_parser import BaseParser


class CSVParser(BaseParser):
    """CSV 文件解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现 CSV 解析
        raise NotImplementedError

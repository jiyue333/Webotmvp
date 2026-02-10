"""
文件职责：Excel 文件（.xlsx）解析器。
边界：负责 Excel → Markdown 表格的转换；多 Sheet 需拼接或分别处理。
来源对齐：WeKnora docreader/parser/excel_parser.py
TODO [docparser][M5] 使用 openpyxl 实现解析，输出 Markdown 表格格式。
"""
from app.docparser.parsers.base_parser import BaseParser


class ExcelParser(BaseParser):
    """Excel 文件（.xlsx）解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现 Excel 解析
        raise NotImplementedError

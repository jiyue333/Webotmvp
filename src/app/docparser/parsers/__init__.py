"""
文件职责：维护 docparser 子模块 `__init__` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/__init__.py`。
"""

# from app.docparser.parsers.parser_factory import get_parser
# from app.docparser.parsers.pdf_parser import PDFParser
# from app.docparser.parsers.docx_parser import DocxParser
# from app.docparser.parsers.markdown_parser import MarkdownParser
# from app.docparser.parsers.text_parser import TextParser
# from app.docparser.parsers.csv_parser import CSVParser
# from app.docparser.parsers.excel_parser import ExcelParser
# from app.docparser.parsers.web_parser import WebParser
# from app.docparser.parsers.image_parser import ImageParser

# 文件职责：parsers 子包入口；统一导出各格式解析器、工厂函数和内容抓取器，供 docparser 包和 ingest 链路使用。
# 边界：仅做符号导出，不包含解析逻辑。

# TODO(M5)：在各解析器实现完成后，导出 get_parser, fetch_url, PDFParser, DocxParser, MarkdownParser, TextParser, CSVParser, ExcelParser, WebParser, ImageParser。

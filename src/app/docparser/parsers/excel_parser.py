# 文件职责：Excel 文件解析器，将 .xlsx 二进制内容转换为 Markdown 表格格式文本。对齐 WeKnora docreader/parser/excel_parser.py。
# 边界：仅负责 Excel 格式读取（多 Sheet 合并）与表格化输出；分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 ExcelParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。使用 openpyxl 读取各 Sheet 数据，转换为 Markdown 表格格式字符串返回。

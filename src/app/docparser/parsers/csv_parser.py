# 文件职责：CSV 文件解析器，将 .csv 二进制内容转换为 Markdown 表格格式文本。对齐 WeKnora docreader/parser/csv_parser.py。
# 边界：仅负责 CSV 格式读取与表格化输出；分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 CSVParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。使用 csv.reader 读取行列，转换为 Markdown 表格格式字符串返回。

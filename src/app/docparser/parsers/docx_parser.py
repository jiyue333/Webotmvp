# 文件职责：Word（.docx）文档解析器，将 DOCX 二进制内容提取为 Markdown 格式文本。对齐 WeKnora docreader/parser/docx_parser.py。
# 边界：仅负责 DOCX 格式的文本和内嵌图片提取；OCR 和分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 DocxParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。使用 python-docx 读取段落和表格，提取内嵌图片，返回 (text, images) 元组。

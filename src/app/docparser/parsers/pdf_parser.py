# 文件职责：PDF 文档解析器，将 PDF 二进制内容提取为 Markdown 格式文本。对齐 WeKnora docreader/parser/pdf_parser.py。
# 边界：仅负责 PDF 格式的文本提取；OCR 补全和分块由 BaseParser.parse() 编排调用，本类不直接处理。

# TODO(M5)：定义 PDFParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。使用 pdfplumber 或 PyMuPDF 读取页面文本，提取图片占位符，返回 (text, images) 元组。

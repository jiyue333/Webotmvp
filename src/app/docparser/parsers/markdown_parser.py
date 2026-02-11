# 文件职责：Markdown 文件解析器，将 .md 二进制内容解码为文本。对齐 WeKnora docreader/parser/markdown_parser.py。
# 边界：仅负责编码检测与文本读取；Markdown 本身即目标格式，无需格式转换。分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 MarkdownParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。检测编码后 decode 为字符串返回，提取内嵌图片引用。

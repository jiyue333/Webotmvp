# 文件职责：纯文本文件解析器，将 .txt 二进制内容解码为字符串。对齐 WeKnora docreader/parser/text_parser.py。
# 边界：仅负责编码检测与文本读取；不做格式转换。分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 TextParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。使用 chardet 或 charset-normalizer 检测编码，decode 后返回字符串。

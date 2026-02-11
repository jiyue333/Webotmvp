# 文件职责：图片文件解析器，通过 OCR 将图片二进制内容提取为文本。对齐 WeKnora docreader/parser/image_parser.py。
# 边界：仅负责将图片内容委托给 OCREngine 提取文字；不处理图片格式转换。分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 ImageParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。调用 OCREngine.get_instance() 获取后端，执行 predict(content) 返回提取文本。

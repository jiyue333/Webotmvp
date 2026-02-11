# 文件职责：网页内容解析器，将已抓取的 HTML bytes 提取为 Markdown 格式正文。对齐 WeKnora docreader/parser/web_parser.py 的解析部分。
# 边界：仅负责 HTML → Markdown 正文提取（使用 trafilatura 或 readability）；不负责网络请求，URL 抓取由 content_fetcher 完成。分块由 BaseParser.parse() 编排。

# TODO(M5)：定义 WebParser(BaseParser) 类，实现 parse_into_text(content: bytes) 方法。将 HTML bytes decode 后，使用 trafilatura.extract() 提取正文并转为 Markdown 返回。

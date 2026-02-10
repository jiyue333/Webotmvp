"""
文件职责：网页内容解析器（URL → 文本）。
边界：负责从 URL 抓取网页内容并转换为 Markdown 文本；需防范 SSRF。
来源对齐：WeKnora docreader/parser/web_parser.py
TODO [docparser][M5] 使用 httpx 抓取网页，用 BeautifulSoup/readability 提取正文。
"""
from app.docparser.parsers.base_parser import BaseParser


class WebParser(BaseParser):
    """网页内容解析器。"""

    def parse_into_text(self, content: bytes):
        # TODO [docparser][M5] 实现 URL 网页抓取与正文提取
        raise NotImplementedError

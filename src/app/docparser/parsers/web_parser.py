"""
文件职责：维护 docparser 子模块 `web_parser` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/web_parser.py`。
"""

from app.docparser.parsers.base_parser import BaseParser


class WebParser(BaseParser):
    """网页内容解析器。"""

    def parse_into_text(self, content: bytes):
        # [ingest][P2][todo] 完成条件：实现 URL 网页抓取与正文提取；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/web_parser.py`。
        """执行 `parse_into_text` 逻辑。

        输入：按函数签名参数接收。
        输出：返回当前函数声明对应的数据结果。
        副作用：可能读取或更新进程内状态与外部依赖。
        """
        raise NotImplementedError

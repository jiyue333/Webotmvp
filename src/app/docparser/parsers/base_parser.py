"""
文件职责：维护 docparser 子模块 `base_parser` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/base_parser.py`。
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple, Union

from app.docparser.document import Chunk, Document


class BaseParser(ABC):
    """
    解析器基类。

    所有格式解析器（PDF、Word、Markdown 等）必须继承此类并实现 parse_into_text 方法。
    基类提供统一的 parse() 入口，编排"文本提取→OCR→分块"流程。
    """

    def __init__(
        self,
        file_name: str = "",
        file_type: Optional[str] = None,
        chunk_size: int = 512,
        chunk_overlap: int = 100,
        enable_ocr: bool = True,
    ):
        """执行 `__init__` 逻辑。

        输入：按函数签名参数接收。
        输出：返回当前函数声明对应的数据结果。
        副作用：可能读取或更新进程内状态与外部依赖。
        """
        self.file_name = file_name
        self.file_type = file_type or self._infer_type(file_name)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.enable_ocr = enable_ocr

    @abstractmethod
    def parse_into_text(
        self, content: bytes
    ) -> Union[str, Tuple[str, Dict[str, str]]]:
        """
        将文件二进制内容解析为文本（Markdown 格式优先）。

        Args:
            content: 文件二进制内容。

        Returns:
            纯文本字符串，或 (文本, 图片映射) 元组。
        """
        ...

    def parse(self, content: bytes) -> Document:
        """
        完整解析流程：文本提取 → OCR（可选）→ 分块 → 返回 Document。

        Args:
            content: 文件二进制内容。

        Returns:
            解析后的 Document 对象。
        """
        # [ingest][P2][todo] 完成条件：实现完整流程；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/base_parser.py`。
        raise NotImplementedError

    @staticmethod
    def _infer_type(file_name: str) -> str:
        """根据文件名推断文件类型。"""
        if not file_name:
            return ""
        ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
        return ext

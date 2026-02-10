"""
文件职责：解析器抽象基类，定义所有格式解析器的统一接口。
边界：只定义接口契约，不包含具体格式解析实现。
来源对齐：WeKnora docreader/parser/base_parser.py（简化版，移除 gRPC/存储耦合）。
TODO [docparser][M5] 实现 parse_into_text 和 parse 的完整流程：解析→OCR→分块。
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
        # TODO [docparser][M5] 实现完整流程
        raise NotImplementedError

    @staticmethod
    def _infer_type(file_name: str) -> str:
        """根据文件名推断文件类型。"""
        if not file_name:
            return ""
        ext = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
        return ext

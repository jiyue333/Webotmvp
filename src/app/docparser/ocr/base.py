"""
文件职责：OCR 后端抽象基类，定义所有 OCR 引擎的统一接口。
边界：只定义 predict 接口，不包含具体 OCR 实现。
来源对齐：WeKnora docreader/ocr/base.py
TODO [docparser][M5] 确认 predict 接口是否需要 async 版本。
"""
from abc import ABC, abstractmethod
from typing import Union


class OCRBackend(ABC):
    """OCR 后端抽象基类。"""

    @abstractmethod
    def predict(self, image: Union[str, bytes]) -> str:
        """
        从图片中提取文字。

        Args:
            image: 图片文件路径或二进制内容。

        Returns:
            提取的文本。
        """
        ...


class DummyOCRBackend(OCRBackend):
    """空实现，用于 OCR 不可用时的降级。"""

    def predict(self, image: Union[str, bytes]) -> str:
        return ""

"""
文件职责：维护 docparser 子模块 `base` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/ocr/base.py`。
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
        """执行 `predict` 逻辑。

        输入：按函数签名参数接收。
        输出：返回当前函数声明对应的数据结果。
        副作用：可能读取或更新进程内状态与外部依赖。
        """
        return ""

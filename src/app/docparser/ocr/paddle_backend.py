"""
文件职责：PaddleOCR 后端实现。
边界：封装 PaddleOCR SDK 调用，对外暴露统一的 predict 接口。
来源对齐：WeKnora docreader/ocr/paddle.py
TODO [docparser][M5] 安装 paddleocr 依赖，实现 predict 方法。
"""
from typing import Union

from app.docparser.ocr.base import OCRBackend


class PaddleOCRBackend(OCRBackend):
    """PaddleOCR 后端。"""

    def __init__(self):
        # TODO [docparser][M5] 初始化 PaddleOCR 模型
        pass

    def predict(self, image: Union[str, bytes]) -> str:
        # TODO [docparser][M5] 调用 PaddleOCR 执行文字识别
        raise NotImplementedError

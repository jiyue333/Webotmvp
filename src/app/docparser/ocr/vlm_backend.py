"""
文件职责：VLM（视觉语言模型）OCR 后端实现。
边界：通过调用外部 VLM 接口（如 GPT-4V、Qwen-VL）从图片中提取文字。
来源对齐：WeKnora docreader/ocr/vlm.py
TODO [docparser][M5] 对接 LLM client 实现 VLM OCR。
"""
from typing import Union

from app.docparser.ocr.base import OCRBackend


class VLMOCRBackend(OCRBackend):
    """VLM（视觉语言模型）OCR 后端。"""

    def __init__(self):
        # TODO [docparser][M5] 初始化 VLM 客户端（使用 app.client.llm_client）
        pass

    def predict(self, image: Union[str, bytes]) -> str:
        # TODO [docparser][M5] 调用 VLM 接口执行图片文字提取
        raise NotImplementedError

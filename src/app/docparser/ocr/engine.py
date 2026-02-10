"""
文件职责：OCR 引擎工厂，管理各 OCR 后端实例（单例 + 线程安全）。
边界：负责 OCR 后端的创建与缓存，不包含具体 OCR 算法。
来源对齐：WeKnora docreader/ocr/__init__.py（OCREngine 类）
TODO [docparser][M5] 注册 PaddleOCR 和 VLM 后端。
"""
import logging
import threading
from typing import Dict

from app.docparser.ocr.base import DummyOCRBackend, OCRBackend

logger = logging.getLogger(__name__)


class OCREngine:
    """OCR 引擎工厂（单例模式，线程安全）。"""

    _instances: Dict[str, OCRBackend] = {}
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls, backend_type: str = "dummy") -> OCRBackend:
        """
        获取 OCR 后端实例。

        Args:
            backend_type: 后端类型（"paddle" / "vlm" / "dummy"）。

        Returns:
            OCR 后端实例。
        """
        backend_type = (backend_type or "dummy").lower()

        with cls._lock:
            inst = cls._instances.get(backend_type)
            if inst is not None:
                return inst

            logger.info("创建 OCR 引擎实例: %s", backend_type)

            # TODO [docparser][M5] 注册 PaddleOCR 和 VLM 后端
            if backend_type == "paddle":
                from app.docparser.ocr.paddle_backend import PaddleOCRBackend
                inst = PaddleOCRBackend()
            elif backend_type == "vlm":
                from app.docparser.ocr.vlm_backend import VLMOCRBackend
                inst = VLMOCRBackend()
            else:
                inst = DummyOCRBackend()

            cls._instances[backend_type] = inst
            return inst

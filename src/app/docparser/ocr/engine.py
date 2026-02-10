"""
文件职责：维护 docparser 子模块 `engine` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/ocr/engine.py`。
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

            # [ingest][P2][todo] 完成条件：注册 PaddleOCR 和 VLM 后端；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/ocr/engine.py`。
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

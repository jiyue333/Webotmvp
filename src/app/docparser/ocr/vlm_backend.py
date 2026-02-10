"""
文件职责：维护 docparser 子模块 `vlm_backend` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/ocr/vlm_backend.py`。
"""

from typing import Union

from app.docparser.ocr.base import OCRBackend


class VLMOCRBackend(OCRBackend):
    """VLM（视觉语言模型）OCR 后端。"""

    def __init__(self):
        # [ingest][P2][todo] 完成条件：初始化 VLM 客户端（使用 app.client.llm_client）；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/ocr/vlm_backend.py`。
        """执行 `__init__` 逻辑。

        输入：按函数签名参数接收。
        输出：返回当前函数声明对应的数据结果。
        副作用：可能读取或更新进程内状态与外部依赖。
        """
        pass

    def predict(self, image: Union[str, bytes]) -> str:
        # [ingest][P2][todo] 完成条件：调用 VLM 接口执行图片文字提取；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/ocr/vlm_backend.py`。
        """执行 `predict` 逻辑。

        输入：按函数签名参数接收。
        输出：返回当前函数声明对应的数据结果。
        副作用：可能读取或更新进程内状态与外部依赖。
        """
        raise NotImplementedError

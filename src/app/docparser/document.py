"""
文件职责：维护 docparser 子模块 `document` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/document.py`。
"""

from typing import Any, Dict, List

from pydantic import BaseModel, Field


class Chunk(BaseModel):
    """文档分块，包含分块内容、位置信息和元数据。"""

    content: str = Field(default="", description="分块文本内容")
    seq: int = Field(default=0, description="分块序号")
    start: int = Field(default=0, description="在原文中的起始位置")
    end: int = Field(default=0, description="在原文中的结束位置")
    images: List[Dict[str, Any]] = Field(
        default_factory=list, description="分块中包含的图片信息"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="附加元数据"
    )


class Document(BaseModel):
    """解析后的文档，包含文本内容、图片映射和分块结果。"""

    content: str = Field(default="", description="文档全文（Markdown 格式）")
    images: Dict[str, str] = Field(
        default_factory=dict, description="图片映射 {占位符: 存储路径}"
    )
    chunks: List[Chunk] = Field(
        default_factory=list, description="分块结果列表"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="文档级元数据（文件名、类型、大小等）"
    )

    def is_valid(self) -> bool:
        """文档是否有效（内容非空）。"""
        return self.content != ""

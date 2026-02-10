"""
文件职责：文档解析模块的数据模型定义（Document 和 Chunk）。
边界：仅定义数据结构，不含解析逻辑。所有 parser、splitter、ocr 模块的输入/输出均基于此文件的类型。
来源对齐：WeKnora docreader/models/document.py
TODO [docparser][M5] 根据实际需求扩展 metadata 字段。
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

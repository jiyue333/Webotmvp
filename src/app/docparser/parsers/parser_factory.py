"""
文件职责：解析器工厂，根据文件类型（扩展名）自动选择合适的解析器实例。
边界：只做路由分发，不包含具体解析逻辑。
来源对齐：WeKnora docreader/parser/parser.py
TODO [docparser][M5] 注册所有格式解析器，实现 get_parser 工厂方法。
"""
from typing import Optional

from app.docparser.parsers.base_parser import BaseParser


# 文件扩展名 → 解析器类的映射（M5 阶段逐步注册）
_PARSER_REGISTRY: dict[str, type[BaseParser]] = {
    # TODO [docparser][M5] 注册各格式解析器
    # "pdf": PDFParser,
    # "docx": DocxParser,
    # "md": MarkdownParser,
    # "txt": TextParser,
    # "csv": CSVParser,
    # "xlsx": ExcelParser,
}


def get_parser(
    file_name: str,
    file_type: Optional[str] = None,
    chunk_size: int = 512,
    chunk_overlap: int = 100,
    enable_ocr: bool = True,
) -> BaseParser:
    """
    根据文件类型获取对应的解析器实例。

    Args:
        file_name: 文件名（用于推断类型）。
        file_type: 显式指定文件类型（优先于文件名推断）。
        chunk_size: 分块大小。
        chunk_overlap: 分块重叠。
        enable_ocr: 是否启用 OCR。

    Returns:
        对应格式的解析器实例。

    Raises:
        ValueError: 不支持的文件类型。
    """
    ext = file_type or (file_name.rsplit(".", 1)[-1].lower() if "." in file_name else "")
    parser_cls = _PARSER_REGISTRY.get(ext)
    if parser_cls is None:
        raise ValueError(f"不支持的文件类型: {ext}")
    return parser_cls(
        file_name=file_name,
        file_type=ext,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        enable_ocr=enable_ocr,
    )

"""
文件职责：维护 docparser 子模块 `parser_factory` 的解析/OCR/分块职责边界。
边界：只处理文档解析、OCR 与分块相关能力；上游接收 ingest 输入，下游输出结构化结果，不直接写数据库。
TODO：
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/parser_factory.py`。
"""

from typing import Optional

from app.docparser.parsers.base_parser import BaseParser


# 文件扩展名 → 解析器类的映射（M5 阶段逐步注册）
_PARSER_REGISTRY: dict[str, type[BaseParser]] = {
    # [ingest][P2][todo] 完成条件：注册各格式解析器；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/parsers/parser_factory.py`。
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

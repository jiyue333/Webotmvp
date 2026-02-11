# 文件职责：docparser 包入口；统一导出文档解析模块的公共符号，供上层模块 `from app.docparser import ...` 使用。
# 边界：仅做符号导出，不包含任何业务逻辑。

# TODO(M5)：导出 Document, Chunk, get_parser, fetch_url, TextSplitter 等核心符号，以及 DocParserError 异常基类，供 worker/ingest 链路 import。

# 文件职责：文本分块器 TextSplitter，将长文本按可配置参数切分为带位置信息的 chunk 列表。对齐 WeKnora docreader TextSplitter。
# 边界：仅负责文本切分算法；不感知文件格式、OCR、数据库。由 BaseParser.parse() 调用。

# TODO(M5)：定义 TextSplitter 类。__init__ 接收 chunk_size(512), chunk_overlap(100), separators, protected_patterns, length_function 参数。
# TODO(M5)：实现 split_text(text: str) -> list[tuple[int,int,str]]，按分隔符优先级递归切分，支持受保护模式（表格/代码块/公式不切断），返回 (start, end, chunk_text) 列表。
# TODO(M5)：实现 restore_text(chunks) -> str 静态方法，按 start_pos 拼接非重叠部分，用于验证分块正确性。

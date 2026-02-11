# 文件职责：定义解析器抽象基类 BaseParser，规定所有格式解析器必须实现的接口契约，并提供统一的 parse() 编排入口。
# 边界：仅定义抽象接口与编排骨架；具体格式解析由子类实现，OCR 和分块能力由外部注入，不直接依赖具体后端。

# TODO(M5)：定义 BaseParser(ABC) 类。__init__ 接收 file_name, file_type, chunk_size, chunk_overlap, enable_ocr 参数。
# TODO(M5)：定义抽象方法 parse_into_text(content: bytes) -> Union[str, Tuple[str, Dict[str,str]]]，子类实现格式文本提取。子类解析失败应抛 ParseError 子类（CorruptedFileError / ParseTimeoutError）。
# TODO(M5)：定义 parse(content: bytes) -> Document 编排方法，流程为 parse_into_text → OCREngine（可选）→ TextSplitter 分块 → 组装 Document 返回。内部捕获 OCRError 降级为空文本，SplitError 上抛。
# TODO(M5)：定义 _infer_type(file_name) 静态方法，根据文件扩展名推断类型。

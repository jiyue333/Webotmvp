# 文件职责：解析器工厂函数 get_parser()，根据文件类型返回对应的解析器实例。对齐 WeKnora docreader/parser/parser.py 的注册逻辑。
# 边界：仅负责类型映射与实例化，不包含解析逻辑；解析器注册表在 M5 阶段补齐。URL 场景由上层先调用 content_fetcher.fetch_url() 获取 HTML bytes，再以 "html" 类型查表获取 WebParser。

# TODO(M5)：定义 _PARSER_REGISTRY: dict[str, type[BaseParser]] 映射表，注册 pdf/docx/md/txt/csv/xlsx/html 对应的解析器类。其中 html 映射到 WebParser。
# TODO(M5)：实现 get_parser(file_name, file_type?, chunk_size?, chunk_overlap?, enable_ocr?) -> BaseParser。按 file_type 或文件扩展名查表，返回解析器实例，不支持的类型抛 UnsupportedFormatError(2011)。

# docparser/

## 文件职责
文档解析模块，负责将各种格式的文件/URL 内容转换为结构化文本并分块，为下游 ingest 链路提供统一输出。

## 边界
- 仅处理"内容理解"相关能力：格式解析、OCR 文字补全、文本分块。
- **不直接落库**或更新业务状态，产物交给 worker/ingest 层处理。
- 上游由 `knowledge/worker` 传入文件或 URL，下游输出 `Document(chunks, metadata)` 结构。

## 设计要点
- **fetch 与 parse 分离**：所有 Parser 的 `parse_into_text(content: bytes)` 接口统一接收已获取的内容 bytes。URL 场景的网络抓取由独立的 `content_fetcher` 负责，不混入 Parser。
- 调用链路：
  - **文件类型**：`file_bytes → get_parser(file_type).parse(file_bytes) → Document`
  - **URL 类型**：`url → content_fetcher.fetch_url(url) → html_bytes → get_parser("html").parse(html_bytes) → Document`
- **统一异常模型**：定义 `DocParserError` 异常层次（继承 `common.AppError`），按职责域分为 ParseError / OCRError / FetchError / SplitError，每个异常携带 `error_code`（2000-2099 号段）和 `retryable` 标记，让上层 worker 精准映射 parse_status 和制定重试策略。

## 数据流
```text
文件上传
  -> parser_factory.get_parser(file_type) 选择解析器
  -> BaseParser.parse_into_text(content_bytes) 提取文本
  -> OCREngine（可选）补全图片中的文字
  -> TextSplitter.split_text() 分块
  -> 输出 Document(chunks, metadata)

URL 导入
  -> content_fetcher.fetch_url(url) 抓取 HTML
  -> parser_factory.get_parser("html") 获取 WebParser
  -> WebParser.parse_into_text(html_bytes) 提取正文
  -> TextSplitter.split_text() 分块
  -> 输出 Document(chunks, metadata)
```

## 目录结构
| 文件                         | 职责                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| `__init__.py`                | 包入口，统一导出公共符号                                   |
| `document.py`                | `Document`/`Chunk` 数据模型定义                            |
| `parsers/__init__.py`        | parsers 子包入口                                           |
| `parsers/base_parser.py`     | 解析器抽象基类 `BaseParser`，定义接口契约和 parse 编排骨架 |
| `parsers/parser_factory.py`  | 工厂函数 `get_parser()`，按文件类型返回解析器实例          |
| `parsers/content_fetcher.py` | URL 内容抓取器 `fetch_url()`，将 fetch 与 parse 解耦       |
| `parsers/pdf_parser.py`      | PDF 解析器                                                 |
| `parsers/docx_parser.py`     | Word（.docx）解析器                                        |
| `parsers/markdown_parser.py` | Markdown 解析器                                            |
| `parsers/text_parser.py`     | 纯文本解析器                                               |
| `parsers/csv_parser.py`      | CSV 解析器                                                 |
| `parsers/excel_parser.py`    | Excel（.xlsx）解析器                                       |
| `parsers/web_parser.py`      | 网页正文解析器（接收已抓取的 HTML bytes）                  |
| `parsers/image_parser.py`    | 图片解析器（OCR）                                          |
| `ocr/__init__.py`            | OCR 子包入口                                               |
| `ocr/base.py`                | OCR 后端抽象基类 `OCRBackend` + 降级实现 `DummyOCRBackend` |
| `ocr/engine.py`              | OCR 引擎工厂 `OCREngine`（单例模式）                       |
| `ocr/paddle_backend.py`      | PaddleOCR 后端实现                                         |
| `splitter/__init__.py`       | splitter 子包入口                                          |
| `splitter/text_splitter.py`  | 文本分块器 `TextSplitter`                                  |
| `splitter/header_hook.py`    | 标题层级追踪器 `HeaderHook`                                |

## 协作关系
| 协作单元              | 输入依赖           | 输出产物      | 并行边界             |
| --------------------- | ------------------ | ------------- | -------------------- |
| content_fetcher       | URL 字符串         | HTML bytes    | 可独立演进           |
| parsers               | 文件/HTML bytes    | 结构化文本    | 可与 ocr 并行演进    |
| ocr                   | 图片路径/二进制    | OCR 文本结果  | 可独立替换后端       |
| splitter              | 原始文本、分块参数 | chunk 列表    | 可与 parser 并行调优 |
| worker/ingest（上游） | —                  | Document 输出 | 与 API 并行          |

## TODO
- TODO(M5)：在 common/exceptions.py 中实现 DocParserError 异常层次（依赖 M2 的 AppError 基类）。
- TODO(M5)：实现 content_fetcher.fetch_url()，包含 SSRF 防护和代理支持。失败抛 FetchError 子类。
- TODO(M5)：补齐各格式解析器的 parse_into_text 实现。解析失败抛 ParseError 子类。
- TODO(M5)：实现 BaseParser.parse() 完整编排流程（文本提取 → OCR → 分块）。OCRError 降级为空文本。
- TODO(M5)：实现 TextSplitter.split_text() 分块算法。分块失败抛 SplitError。
- TODO(M5)：实现 PaddleOCR 后端调用。初始化/识别失败抛 OCRInitError / OCRPredictError。
- TODO(M5)：在 parser_factory 注册表中注册各解析器（含 html → WebParser）。不支持的类型抛 UnsupportedFormatError。

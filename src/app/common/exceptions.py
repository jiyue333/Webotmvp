# 文件职责：定义全局业务异常基类 AppError 和各模块异常子类，供 service/worker 层抛出、api 层（exception_handler）捕获并转换为统一响应。
# 边界：只定义异常类层次结构；不包含错误码定义（由 error_codes.py 负责），不处理 HTTP 响应封装（由 api 层中间件负责）。

# ── 通用异常 ──────────────────────────────────────────────

# TODO(M2)：定义 AppError(Exception) 基类，包含 error_code: int, message: str, details: dict 字段。
# TODO(M2)：定义常用子类 NotFoundError(AppError) / ValidationError(AppError) / AuthenticationError(AppError) / PermissionError(AppError) / ConflictError(AppError)，各自设置默认 error_code 和 HTTP status_code。
# TODO(M2)：在 main.py 中调用 common/error_handler.register_exception_handlers(app)，将 AppError 子类自动映射为 HTTP 状态码 + 统一响应壳 {success: false, error: {code, message, details}}。

# ── DocParser 异常（2000-2099）────────────────────────────
#
# 设计要点（改进 WeKnora 的裸 Exception 做法）：
#   - WeKnora 问题：docreader 全部用 except Exception as e: + logger.error()，上层无法区分失败原因，重试和状态回写无法标准化。
#   - 改进方案：按职责域分层异常（Parser / OCR / Fetcher / Splitter），每个异常携带 error_code + retryable 标记。
#   - 上层 worker 只需 catch DocParserError，即可从 e.error_code 映射 parse_status，从 e.retryable 决定是否重试。
#
# 异常层次：
#   AppError
#     └── DocParserError (docparser 异常基类, error_code 2000-2099)
#           ├── ParseError                  # 文件解析失败 (2010-2019)
#           │     ├── UnsupportedFormatError   # 不支持的格式 (2011, retryable=False)
#           │     ├── CorruptedFileError       # 文件损坏/无法读取 (2012, retryable=False)
#           │     └── ParseTimeoutError        # 解析超时 (2013, retryable=True)
#           ├── OCRError                    # OCR 识别失败 (2020-2029)
#           │     ├── OCRInitError             # OCR 引擎初始化失败 (2021, retryable=False)
#           │     └── OCRPredictError          # OCR 识别执行失败/超时 (2022, retryable=True)
#           ├── FetchError                  # URL 抓取失败 (2030-2039)
#           │     ├── FetchTimeoutError        # 抓取超时 (2031, retryable=True)
#           │     ├── FetchBlockedError        # SSRF 安全拦截 (2032, retryable=False)
#           │     └── FetchHTTPError           # HTTP 状态码异常 (2033, retryable=按状态码)
#           └── SplitError                  # 分块失败 (2040, retryable=False)

# TODO(M5)：定义 DocParserError(AppError) 基类，包含 error_code: int, message: str, retryable: bool = False 字段。
# TODO(M5)：定义 ParseError(DocParserError) 及子类 UnsupportedFormatError(2011) / CorruptedFileError(2012) / ParseTimeoutError(2013, retryable=True)。
# TODO(M5)：定义 OCRError(DocParserError) 及子类 OCRInitError(2021) / OCRPredictError(2022, retryable=True)。
# TODO(M5)：定义 FetchError(DocParserError) 及子类 FetchTimeoutError(2031, retryable=True) / FetchBlockedError(2032) / FetchHTTPError(2033, retryable 根据 status_code 判断)。
# TODO(M5)：定义 SplitError(DocParserError)，error_code=2040。

# 文件职责：URL 内容抓取器，负责从 URL 获取网页 HTML 内容，返回 bytes 给 WebParser 解析。将 fetch 与 parse 职责解耦。
# 边界：仅负责 HTTP(S) 请求与内容获取；不做正文提取或分块。包含 SSRF 防护（校验 URL 安全性）和代理配置支持。

# TODO(M5)：实现 fetch_url(url: str, timeout: int = 30) -> bytes 函数。使用 requests 或 httpx 发起 GET 请求，返回响应 body bytes。超时抛 FetchTimeoutError(2031)，HTTP 错误抛 FetchHTTPError(2033)。
# TODO(M5)：实现 _is_safe_url(url: str) -> bool 内部函数。校验 URL scheme 仅限 http/https，拒绝 private/loopback/link-local IP 和 localhost 等内部地址。校验失败抛 FetchBlockedError(2032)。
# TODO(M5)：支持从配置读取 HTTP/HTTPS 代理设置（对齐 WeKnora CONFIG.external_https_proxy）。

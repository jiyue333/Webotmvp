# 文件职责：提供输入清理与安全校验工具函数，防止 SSRF 攻击、XSS 注入和恶意输入。供 KnowledgeService URL 导入、用户输入清理等场景调用。对齐 WeKnora internal/utils/security.go（IsSSRFSafeURL / SanitizeHTML / ValidateInput）。
# 边界：只提供安全校验/清理的纯函数；不处理认证逻辑（JWT / 密码哈希由 common/security.py 负责），不处理 HTTP 请求（由 docparser/web_parser 负责），不依赖数据库。

# TODO(M5)：实现 is_ssrf_safe_url(url: str) -> tuple[bool, str] 函数。校验 URL 协议（仅允许 http/https）、解析主机名、检查私有 IP / 回环地址 / 云元数据端点。返回 (is_safe, reason)。
# TODO(M5)：实现 sanitize_html(input: str) -> str 函数。清理 HTML 标签，防止 XSS 攻击。
# TODO(M5)：实现 validate_input(input: str, max_length: int = 10000) -> tuple[str, bool] 函数。校验用户输入长度和 UTF-8 合法性。

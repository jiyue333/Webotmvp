# 文件职责：封装外部 OCR 服务的调用客户端，提供图片文字识别能力。
# 边界：仅负责 HTTP 请求发送与响应解析；不编排业务流程，不读写数据库。OCR 服务配置由调用方传入。
# 对齐来源：WeKnora docreader/parser/*.py 中的 OCR 调用路径；mvp.md §3.1 架构图 External_Left 中的 OCR Service。

# TODO(M5)：定义 OCRConfig dataclass（frozen=True），字段包括 backend(vlm/paddle/third_party), base_url, api_key, extra。
# TODO(M5)：定义 OCRResult dataclass（text, confidence, page）。
# TODO(M5)：定义 OCRClient Protocol，包含：
#   - async recognize(image_data: bytes, *, language: str) -> list[OCRResult]
#   - async recognize_from_url(image_url: str, *, language: str) -> list[OCRResult]
# TODO(M5)：实现 VLMOCRClient 类，使用 LLMClient 对接 VLM 模型进行 OCR。对齐 docreader ocr/vlm_backend.py 思路。
# TODO(M5)：评估是否需要 PaddleOCR 本地方案作为备选（离线场景）。

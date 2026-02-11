# 文件职责：ocr 子包入口；统一导出 OCR 引擎和后端类，供 parser 层调用。
# 边界：仅做符号导出，不包含 OCR 逻辑。

# TODO(M5)：在 OCR 后端实现完成后，导出 OCREngine。

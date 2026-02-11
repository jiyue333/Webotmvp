# 文件职责：定义 OCR 后端抽象基类 OCRBackend 和降级空实现 DummyOCRBackend，作为 OCR 能力的接口契约。
# 边界：仅定义抽象接口和降级实现；具体 OCR 后端（PaddleOCR 等）由子类实现。不依赖任何外部模型。

# TODO(M5)：定义 OCRBackend(ABC) 抽象类，包含抽象方法 predict(image: Union[str, bytes, Image.Image]) -> str，从图片提取文字。
# TODO(M5)：定义 DummyOCRBackend(OCRBackend) 降级实现，predict 直接返回空字符串，用于 OCR 不可用时的 fallback。

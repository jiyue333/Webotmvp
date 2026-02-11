# 文件职责：PaddleOCR 后端实现，封装 PaddleOCR 模型调用，从图片中提取文字。对齐 WeKnora docreader/ocr/paddle.py。
# 边界：仅封装 PaddleOCR SDK 调用；由 OCREngine 统一管理实例生命周期，不对外直接暴露。
#
# 设计要点：
#   - __init__ 接收 **kwargs 配置（lang, use_gpu, det_model_name, rec_model_name, 阈值等），不再写死。
#   - 与 OCREngine 的配置指纹机制配合：不同 kwargs → 不同实例，避免配置串用。

# TODO(M5)：定义 PaddleOCRBackend(OCRBackend) 类。__init__(**kwargs) 根据传入参数初始化 PaddleOCR 模型，默认 lang="ch", use_gpu=False。初始化失败抛 OCRInitError(2021)。
# TODO(M5)：实现 predict(image: Union[str, bytes, Image.Image]) -> str 方法。统一将输入转为 PIL.Image → numpy array，调用 self.ocr.ocr() 执行识别，拼接结果文本返回。识别失败抛 OCRPredictError(2022, retryable=True)。

# 文件职责：OCR 引擎工厂，根据 backend_type + 配置参数返回对应的 OCR 后端实例。通过配置指纹实现"同配置复用、异配置隔离"。
# 边界：仅负责后端实例的创建与缓存管理；不执行 OCR 识别逻辑。线程安全。
#
# 设计要点（改进 WeKnora 的纯 backend_type 单例）：
#   - WeKnora 问题：_instances 仅按 backend_type 缓存，同类型不同配置（lang、model_path、use_gpu）会误共享实例。
#   - 改进方案：缓存 key = backend_type + config_fingerprint（对 **kwargs 排序后 hash），确保：
#     • 同 backend_type + 同配置 → 复用实例（避免重复加载模型）
#     • 同 backend_type + 不同配置 → 各自独立实例
#     • 配置热更新时可通过 reset() 清除缓存
#   - 内存控制：可选设置 max_instances 上限，超出时 LRU 淘汰最久未使用的实例。

# TODO(M5)：定义 OCREngine 类。使用类变量 _instances: dict[str, OCRBackend] + threading.Lock 实现线程安全缓存。
# TODO(M5)：实现 _config_fingerprint(backend_type: str, **kwargs) -> str 静态方法。对 backend_type + sorted kwargs 做 hashlib.md5 生成唯一指纹作为缓存 key。
# TODO(M5)：实现 get_instance(backend_type="dummy", **kwargs) -> OCRBackend 类方法。计算指纹查缓存，命中则返回；未命中则按 backend_type 分支创建 PaddleOCRBackend(**kwargs) 或 DummyOCRBackend()，存入缓存后返回。创建失败抛 OCRInitError(2021)。
# TODO(M5)：实现 reset(backend_type?: str) 类方法。无参数时清空全部缓存；指定 backend_type 时仅清除该类型的所有实例。用于配置热更新场景。

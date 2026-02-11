# 文件职责：worker 包入口；统一导出 IngestionWorker、TaskQueue 等核心符号，供 main.py 启动 worker 进程使用。
# 边界：仅控制包级导出边界；不实现任务处理逻辑，不直接依赖 infra 层（由 ingestion_worker 内部注入）。

# TODO(M5)：导出 IngestionWorker / TaskQueue 等核心符号，供 main.py 或独立入口脚本 import 使用。

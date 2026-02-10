# worker/

## 文件职责
- 维护异步任务队列消费器与文档入库任务执行骨架。
- 承接 ingest 状态机与失败重试策略。

## 边界
- worker 不对外暴露 HTTP 接口。
- worker 不定义业务域对象，仅消费任务并调用 service。

## TODO
- [worker][P2][todo] 在 M5 完成队列消费、任务状态更新与重试机制。
- [ingest][P2][todo] 在 M5 打通解析/OCR/分块/向量化入库链路。
- [obs][P2][todo] 在 M8 增加任务级日志与指标埋点。

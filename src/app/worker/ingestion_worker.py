# 文件职责：定义 IngestionWorker 类，作为后台任务消费主循环；通过 TaskQueue（Redis Stream）拉取文档处理任务，调度到对应的 task handler 执行，并维护任务生命周期（确认、回收、状态回写）。
# 边界：只负责任务消费调度与生命周期管理；不包含具体解析/向量化/图谱抽取逻辑（由 services 层和 docparser 模块承担）；不对外暴露 HTTP 接口。

# TODO(M5)：实现 IngestionWorker 类。初始化接收 TaskQueue 实例和 KnowledgeService 依赖；提供 start() / stop() / run_forever() 方法。
# TODO(M5)：实现任务消费主循环。调用 TaskQueue.dequeue() 获取 ReceivedMessage 列表，从 received.envelope 中读取 task_type 路由到对应处理函数（如 "document:process" 路由到 KnowledgeService.process_document）。
# TODO(M5)：处理成功后调用 TaskQueue.ack(received.stream_message_id) 确认消息；处理失败时更新 knowledge.parse_status 为 failed 并写入 error_message，同样 ack（业务失败不需要重试队列，状态已落库）。
# TODO(M5)：在主循环中定期调用 TaskQueue.reclaim_stale() 回收超时未确认的消息（其他 Worker 崩溃遗留），重新执行处理。
# TODO(M5)：实现优雅关闭。收到 SIGTERM/SIGINT 信号后完成当前任务再退出，避免消息停留在 pending 状态。
# TODO(M8)：补齐结构化日志与 OTel span。每个任务消费记录 envelope.task_id / envelope.task_type / knowledge_id / duration / status。

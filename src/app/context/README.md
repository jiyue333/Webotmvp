# context/

## 模块职责
管理 LLM 对话上下文窗口：维护每个 session 的对话历史在 LLM 上下文中的读写、压缩与淘汰。  
对齐 WeKnora `internal/application/service/llmcontext/` 模块。  
在架构图中对应 `CTX["ContextManager(Redis)"]` 节点（核心引擎层）。

## 边界
- **不做**：不负责消息持久化（由 repository 负责）、不处理 HTTP 请求、不执行 RAG 检索。
- **上游**：由 `chat_pipeline` 和 `session service` 调用，获取/写入当前 session 的 LLM 上下文。
- **下游**：依赖 `infra/redis` 作为上下文存储后端；依赖 `client/llm_client` 实现智能压缩（可选）。

## 核心概念（对齐 WeKnora）
- **ContextManager**：核心接口，提供 `add_message` / `get_context` / `clear_context` / `set_system_prompt`。
- **ContextStorage**：存储抽象（Redis 或 Memory），负责上下文的序列化/反序列化。
- **CompressionStrategy**：上下文超出 max_tokens 时的压缩策略（滑动窗口 / LLM 摘要）。

## 文件清单

| 文件                 | 职责                                                          | 主要阶段 |
| -------------------- | ------------------------------------------------------------- | -------- |
| `__init__.py`        | 包入口；导出 ContextManager 协议与工厂函数                    | M1       |
| `context_manager.py` | ContextManager 协议定义与默认实现，编排 storage + compression | M4       |
| `storage.py`         | ContextStorage 协议定义（Save/Load/Delete）                   | M4       |
| `compression.py`     | CompressionStrategy 协议与滑动窗口实现                        | M4       |

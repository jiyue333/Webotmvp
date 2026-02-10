# client/

## 文件职责
- 封装外部 AI 模型服务（LLM / Embedding / Rerank / OCR）的调用入口。
- 统一请求参数组装、超时控制、错误处理与重试策略。
- 对上游 service 层屏蔽第三方 API 差异（基于 `source` 字段路由到不同实现）。

## 边界
- 只负责"发请求 + 解析响应"；不包含业务编排逻辑（由 service 层控制）。
- 不直接读写数据库或 Redis；需要模型配置时由调用方传入。
- 不处理 HTTP 路由层协议（不依赖 FastAPI 相关组件）。
- 异常统一使用 `common/exceptions.py` 中定义的 `ClientError`（`AppError` 子类），供 service 层映射到业务错误码。

## 对齐来源（WeKnora）
- `internal/models/chat/chat.go`：Chat 接口与多 provider 工厂。
- `internal/models/embedding/embedder.go`：Embedder 接口与多 provider 工厂。
- `internal/models/rerank/reranker.go`：Reranker 接口与多 provider 工厂。
- `docreader/parser/*.py` 中的 OCR 调用路径。

## 文件说明
| 文件                  | 职责                                                    | 首次需要阶段 |
| --------------------- | ------------------------------------------------------- | ------------ |
| `__init__.py`         | 包入口；统一导出协议与工厂                              | M1（骨架）   |
| `base.py`             | 定义 BaseModelClient 协议（Protocol）与公共数据结构     | M4           |
| `factory.py`          | 统一工厂入口 `create_client(capability, config)`        | M4           |
| `llm_client.py`       | LLM（Chat）客户端协议与实现，支持流式与非流式           | M4           |
| `embedding_client.py` | Embedding 客户端协议与实现，支持单条与批量向量化        | M5           |
| `rerank_client.py`    | Rerank 客户端协议与实现，支持文档重排打分               | M6           |
| `ocr_client.py`       | OCR 客户端协议与实现，封装外部 OCR 服务的请求与结果解析 | M5           |



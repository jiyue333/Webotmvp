# services/chat_pipeline/

## 目录职责

实现 RAG 对话流水线（Chat Pipeline），采用事件驱动 + 插件模式编排对话的完整生命周期：从历史加载到流式输出。

对标 WeKnora `internal/application/service/chat_pipline/`。

## 边界

- 只负责对话流程编排与步骤调度，不直接处理 HTTP 协议（由 Handler 层负责）。
- 上游调用方：ChatService（同步对话）、Handler（SSE 推送）。
- 下游依赖：Repository 层（数据读写）、ModelService（LLM/Rerank 调用）、EventBus/StreamManager（事件推送）。

## 编排流程

```
LoadHistory → Rewrite → ExtractEntity → SearchParallel → Rerank → Merge → FilterTopK → IntoChatMessage → ChatCompletionStream
```

Pipeline 采用洋葱模型（Middleware/Onion Model），每个步骤为一个 Plugin，由 EventManager 构建调用链。

## 文件结构

| 文件                        | 职责                                              | 实现阶段 | 对标 WeKnora                |
| --------------------------- | ------------------------------------------------- | -------- | --------------------------- |
| `__init__.py`               | 包入口，导出公共符号                              | M4       | —                           |
| `pipeline.py`               | 核心编排引擎：Plugin 协议 + EventManager + 错误体 | M4       | `chat_pipline.go`           |
| `common.py`                 | 公共工具：日志封装、模型准备、消息组装            | M4       | `common.go`                 |
| `load_history.py`           | 加载会话历史对话记录                              | M4       | `load_history.go`           |
| `rewrite.py`                | LLM 查询重写                                      | M6       | `rewrite.go`                |
| `extract_entity.py`         | LLM 实体抽取（Graph RAG 前置）                    | M7       | `extract_entity.go`         |
| `search.py`                 | Chunk 级混合检索（向量 + BM25）                   | M6       | `search.go`                 |
| `search_entity.py`          | 图谱实体检索（Neo4j）                             | M7       | `search_entity.go`          |
| `search_parallel.py`        | 并行编排 Chunk 检索与图谱检索                     | M6/M7    | `search_parallel.go`        |
| `rerank.py`                 | Rerank Model 语义重排序                           | M6       | `rerank.go`                 |
| `merge.py`                  | 多路结果 RRF 合并去重                             | M6       | `merge.go`                  |
| `filter_top_k.py`           | Top-K 截取                                        | M6       | `filter_top_k.go`           |
| `into_chat_message.py`      | Prompt 组装（system + context + history + query） | M4/M6    | `into_chat_message.go`      |
| `chat_completion_stream.py` | LLM 流式生成 + SSE 推送                           | M4       | `chat_completion_stream.go` |

## 与 WeKnora 的裁剪说明

| 裁剪项                 | 原因                                              |
| ---------------------- | ------------------------------------------------- |
| `chat_completion.go`   | MVP 仅保留流式模式，非流式不纳入                  |
| `data_analysis.go`     | 数据分析能力属于 Agent 模式，MVP non-goal         |
| `tracing.go`           | 追踪能力推迟到 M8，且采用 Python OTel 方案        |
| `stream_filter.go`     | 拒答检测能力 mvp.md 主链路未纳入，按需在 M4+ 引入 |
| `chat_pipline_test.go` | 测试文件在 M8 阶段补齐                            |

## TODO

- TODO(M4): 完成 pipeline.py / common.py / load_history.py / into_chat_message.py / chat_completion_stream.py 的实现，打通基础对话链路。
- TODO(M6): 完成 search.py / search_parallel.py / rerank.py / merge.py / filter_top_k.py / rewrite.py 的实现，接入检索增强。
- TODO(M7): 完成 extract_entity.py / search_entity.py 的实现，接入图谱增强。
- TODO(M8): 补齐 Pipeline 级别的 OpenTelemetry 追踪与结构化日志。

# docparser/

## 文件职责
- 维护文档解析、OCR 与分块模块的协作约束。
- 为 `worker -> docparser -> repositories` 链路提供统一输入输出定义。

## 边界
- 仅处理“内容理解”相关能力，不直接落库或更新业务状态。
- 上游由 `knowledge/worker` 传入文件或 URL，下游输出 `Document/Chunk` 结构给 ingest 流程。

## 数据流
```text
上传文件/URL
  -> parser_factory 选择解析器
  -> parse_into_text 提取文本
  -> OCREngine（可选）补全文字
  -> TextSplitter 分块
  -> 输出 Document(chunks, metadata)
```

## 目录结构
- `document.py`：`Document/Chunk` 数据模型。
- `parsers/`：按格式拆分解析器实现与工厂。
- `ocr/`：OCR 后端抽象与工厂。
- `splitter/`：分块算法与标题上下文处理。

## 协作矩阵
| 协作单元 | 输入依赖 | 输出产物 | 并行边界 | 主要阻塞点 |
|---|---|---|---|---|
| parsers | 文件二进制、URL 内容 | 结构化文本 | 可与 OCR 并行演进 | 文件格式兼容性 |
| ocr | 图片路径/二进制 | OCR 文本结果 | 可独立替换后端 | 模型可用性与耗时 |
| splitter | 原始文本、分块参数 | chunk 列表 | 可与 parser 并行调优 | 长文档性能与精度 |
| ingest/worker | Document 输出 | 入库任务数据 | 与 API 并行 | 状态回写约束 |

## TODO
- [ingest][P2][todo] 完成条件：补齐解析/OCR/分块链路并定义失败回写；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/README.md`。
- [retrieval][P2][todo] 完成条件：补齐混合检索查询与召回接口；验证方式：执行 `cd src && python -m pytest -q` 并通过相关模块用例；归属模块：`src/app/docparser/README.md`。
- [obs][P2][todo] 完成条件：补齐日志、指标、追踪最小采集口径；验证方式：完成文档评审并与目录结构、接口现状对齐；归属模块：`src/app/docparser/README.md`。

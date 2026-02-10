# services/chat_pipeline/

## 文件职责
- 维护对话流水线各步骤的拆分模块与执行顺序。
- 支撑 query rewrite、检索、重排、融合与流式输出。

## 边界
- pipeline 只负责编排步骤，不直接处理 HTTP 层细节。
- pipeline 每个步骤应可独立测试与替换。

## 目标步骤
1. `load_history`
2. `rewrite`
3. `extract_entity`
4. `search_parallel`
5. `rerank`
6. `merge`
7. `filter_top_k`
8. `into_chat_message`
9. `chat_completion_stream`

## TODO
- [chat][P1][todo] 在 M4 先打通无检索的流式对话占位流程。
- [retrieval][P2][todo] 在 M6 接入混合检索与重排主链路。
- [graph][P2][todo] 在 M7 接入图谱增强检索并支持降级路径。

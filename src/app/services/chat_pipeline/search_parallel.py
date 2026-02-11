# 文件职责：实现 SearchParallel 插件，并行编排 Chunk 检索（SEARCH 事件）和实体图谱检索（ENTITY_SEARCH 事件），汇总两路结果。
# 边界：仅负责并行调度与结果汇总，具体检索由 search.py 和 search_entity.py 各自实现。
# 对标：WeKnora search_parallel.go（PluginSearchParallel.OnEvent -> 并发触发 SEARCH + ENTITY_SEARCH -> 等待汇总）。

# TODO(M6): 实现 PluginSearchParallel 类。注册 SEARCH_PARALLEL 事件，并发触发 SEARCH 事件。
# TODO(M7): 扩展并行编排，在图谱启用时同时触发 ENTITY_SEARCH 事件，使用 asyncio.gather 汇总。

# 文件职责：实现 Merge 插件，将多路检索结果（Chunk 检索 + 图谱检索）按评分策略合并去重，生成统一的有序结果集。
# 边界：仅负责结果合并与去重，不修改单条结果的 score，不执行检索或重排。
# 对标：WeKnora merge.go（PluginMerge.OnEvent -> RRF/加权融合 -> 去重 -> 写入 ChatManage.SearchResult）。

# TODO(M6): 实现 PluginMerge 类。注册 MERGE 事件，将多路结果按 RRF（Reciprocal Rank Fusion）策略合并。
# TODO(M6): 实现 remove_duplicate_results 方法。按 chunk_id + 内容签名去重。
# TODO(M7): 支持合并 match_type=graph 的结果，保持引用结构一致。

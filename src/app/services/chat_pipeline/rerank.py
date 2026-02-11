# 文件职责：实现 Rerank 插件，调用 Rerank Model 对检索结果进行语义重排序，提升 Top-K 结果的相关性。
# 边界：仅负责重排序，不修改检索结果的内容。当无 rerank model 配置或结果为空时跳过。
# 对标：WeKnora rerank.go（PluginRerank.OnEvent -> 获取 RerankModel -> 调用重排 -> 按 score 降序排列 -> 更新 ChatManage.SearchResult）。

# TODO(M6): 实现 PluginRerank 类。注册 RERANK 事件，通过 ModelService 获取 rerank model。
# TODO(M6): 调用 rerank model 对 search_result 按 query 重打分，更新 score 并按降序排列。
# TODO(M6): 当 rerank model 未配置时，保留原排序直接 next()。

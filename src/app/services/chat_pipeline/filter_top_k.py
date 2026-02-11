# 文件职责：实现 FilterTopK 插件，按 top_k 配置截取合并后的检索结果，控制送入 Prompt 的上下文量。
# 边界：仅负责截取，不修改结果的顺序或内容。top_k 值从 session/KB 配置中继承。
# 对标：WeKnora filter_top_k.go（PluginFilterTopK.OnEvent -> 按 ChatManage.TopK 截断 -> 更新 ChatManage.SearchResult）。

# TODO(M6): 实现 PluginFilterTopK 类。注册 FILTER_TOP_K 事件，按 top_k 截取 search_result。
# TODO(M6): 当 search_result 长度 <= top_k 时直接跳过截取。

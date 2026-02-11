# 文件职责：实现 Rewrite 插件，利用 LLM 对用户查询进行重写/补全，结合历史上下文生成更适合检索的查询。
# 边界：仅负责查询重写，不执行检索。重写结果写入 ChatManage.rewritten_query，原始 query 保持不变。
# 对标：WeKnora rewrite.go（PluginReWrite.OnEvent -> 调用 LLM 重写 -> 写入 ChatManage.RewriteQuery）。

# TODO(M6): 实现 PluginRewrite 类。注册 REWRITE 事件，调用 LLM 进行 query 重写。
# TODO(M6): 当历史为空或 query 足够明确时跳过重写（short-circuit），直接 next()。

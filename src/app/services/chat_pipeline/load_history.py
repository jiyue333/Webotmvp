# 文件职责：实现 LoadHistory 插件，从数据库加载当前会话的历史对话记录，写入 ChatManage.history。
# 边界：仅负责历史消息的读取与截断（max_rounds），不修改消息内容，不感知检索或生成逻辑。
# 对标：WeKnora load_history.go（PluginHistory.OnEvent -> 按 maxRounds 截取历史 -> 写入 ChatManage.History）。

# TODO(M4): 实现 PluginLoadHistory 类。注册 LOAD_HISTORY 事件，通过 MessageRepository 加载历史。
# TODO(M4): 按 session 配置的 max_rounds 截断历史，防止上下文超限。

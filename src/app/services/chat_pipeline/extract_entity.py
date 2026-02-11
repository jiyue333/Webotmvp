# 文件职责：实现 ExtractEntity 插件，调用 LLM 从用户查询中抽取命名实体，供图谱检索使用。
# 边界：仅负责实体抽取，不执行图谱检索。抽取结果写入 ChatManage.entity。若图谱未启用则跳过。
# 对标：WeKnora extract_entity.go（PluginExtractEntity.OnEvent -> LLM 提取实体 -> 写入 ChatManage.Entity）。

# TODO(M7): 实现 PluginExtractEntity 类。注册 EXTRACT_ENTITY 事件，通过 LLM 抽取实体列表。
# TODO(M7): 检查 NEO4J_ENABLE 和 KB 级别的 extract_config 开关，未启用时直接 next()。

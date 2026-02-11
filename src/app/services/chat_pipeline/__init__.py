# 文件职责：chat_pipeline 包入口，导出 Pipeline 编排器与各步骤插件的公共符号。
# 边界：仅做符号导出与包级初始化，不包含业务逻辑。

# TODO(M4): 导出 ChatPipeline 编排器，供 ChatService 调用。
# TODO(M6): 导出检索相关插件（search/rerank/merge/filter_top_k）。
# TODO(M7): 导出图谱相关插件（extract_entity/search_entity）。

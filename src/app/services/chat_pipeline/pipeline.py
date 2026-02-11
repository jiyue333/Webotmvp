# 文件职责：定义 Chat Pipeline 的核心编排引擎，包含 Plugin 接口、EventManager 事件管理器和 PipelineError 错误体系。
# 边界：仅负责插件注册与洋葱模型调用链构建，不实现任何具体步骤逻辑。各步骤以 Plugin 方式注册。
# 对标：WeKnora chat_pipline.go（Plugin 接口 + EventManager + PluginError）。

# TODO(M4): 定义 Plugin 协议（Protocol），包含 on_event(ctx, event_type, chat_manage, next) 和 activation_events() 方法。
# TODO(M4): 实现 EventManager 类。维护 event_type -> [Plugin] 映射，build_handler 构建洋葱调用链，trigger 触发事件执行。
# TODO(M4): 定义 PipelineError 数据类。包含 err/description/error_type 字段，提供 with_error() 克隆方法。
# TODO(M4): 定义预定义错误常量。ErrSearchNothing/ErrSearch/ErrRerank/ErrModelCall/ErrGetHistory 等。
# TODO(M4): 实现 ChatPipeline 门面类。接收所有依赖，按步骤顺序注册插件并触发执行。

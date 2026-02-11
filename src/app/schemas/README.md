# schemas/

## 目录职责
定义各 API 端点的 Pydantic DTO（请求/响应数据结构），约束接口输入输出类型，是前后端 API 契约的唯一数据源。

## 边界
- 只定义数据结构与 Pydantic 校验规则。
- 不包含业务逻辑（由 Service 层负责）。
- 不处理 HTTP 响应封装（统一响应壳由 `common/response.py` 负责）。

## 命名约定
| 后缀       | 用途                     | 示例                |
| ---------- | ------------------------ | ------------------- |
| `Create`   | 创建请求入参             | `KBCreate`          |
| `Update`   | 更新请求入参（字段可选） | `ModelUpdate`       |
| `Detail`   | 详情响应                 | `UserDetail`        |
| `ListItem` | 列表项响应               | `KnowledgeListItem` |
| `Query`    | 查询/筛选参数            | `KnowledgeQuery`    |
| `Request`  | 动作请求入参             | `ChatRequest`       |
| `Response` | 动作响应                 | `TokenResponse`     |

## 文件清单
| 文件                | 对应 API                                 | 实现阶段 |
| ------------------- | ---------------------------------------- | -------- |
| `__init__.py`       | 包入口，重导出常用 schema                | —        |
| `common.py`         | 通用分页/路径参数                        | M2       |
| `auth.py`           | `/auth/*` 鉴权端点                       | M2       |
| `model.py`          | `/models/*` 模型管理                     | M3       |
| `knowledge_base.py` | `/knowledge-bases/*` 知识库              | M3       |
| `knowledge_tag.py`  | `/knowledge-bases/{id}/tags/*` 标签      | M3       |
| `knowledge.py`      | `/knowledge-bases/{id}/knowledge/*` 知识 | M3       |
| `session.py`        | `/sessions/*` 会话                       | M4       |
| `message.py`        | `/messages/*` 消息                       | M4       |
| `chat.py`           | `/knowledge-chat/*` 对话 + SSE 事件      | M4       |
| `search.py`         | `/knowledge-search` 独立检索             | M6       |

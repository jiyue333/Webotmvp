# schemas/

## 概述

Pydantic DTO（Data Transfer Object）层。定义 API 请求/响应的数据结构与校验规则。

## 命名规范

每个文件对应一个业务域，文件内按用途使用以下后缀：

| 后缀       | 用途         | 示例                    |
| ---------- | ------------ | ----------------------- |
| `Create`   | 创建请求体   | `KnowledgeBaseCreate`   |
| `Update`   | 更新请求体   | `KnowledgeBaseUpdate`   |
| `Detail`   | 详情响应体   | `KnowledgeBaseDetail`   |
| `ListItem` | 列表项响应体 | `KnowledgeBaseListItem` |
| `Query`    | 查询参数     | `KnowledgeBaseQuery`    |

## 文件与 Endpoint 对应关系

| Schema 文件         | 对应 Endpoint 文件                    |
| ------------------- | ------------------------------------- |
| `auth.py`           | `api/v1/endpoints/auth.py`            |
| `model.py`          | `api/v1/endpoints/models.py`          |
| `knowledge_base.py` | `api/v1/endpoints/knowledge_bases.py` |
| `knowledge.py`      | `api/v1/endpoints/knowledges.py`      |
| `knowledge_tag.py`  | `api/v1/endpoints/knowledge_tags.py`  |
| `session.py`        | `api/v1/endpoints/sessions.py`        |
| `message.py`        | `api/v1/endpoints/messages.py`        |
| `chat.py`           | `api/v1/endpoints/chat.py`            |
| `common.py`         | 通用响应包装（所有接口共用）          |

## TODO

- [schemas][M2] 实现 auth.py 的登录/注册 schema
- [schemas][M3] 实现 model、knowledge_base、knowledge 的 CRUD schema

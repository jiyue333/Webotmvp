# repositories/

## 文件职责
- 提供数据库与检索存储的访问抽象。
- 维护实体模型与仓储接口的对应关系。

## 边界
- Repository 不处理业务策略与跨领域编排。
- 所有查询/写入语义由 service 层组织。

## 子模块
- `models/`：ORM 模型定义。
- `retriever/`：检索相关存储访问（Postgres/Neo4j）。
- `*_repository.py`：按聚合根拆分的仓储接口实现。

## TODO
- [arch][P1][todo] 在 M1 统一仓储方法命名与返回类型约定。
- [knowledge][P1][todo] 在 M3 完成知识库与知识实体仓储实现。
- [retrieval][P2][todo] 在 M6 完成混合检索与重排所需仓储查询接口。

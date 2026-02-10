# schemas/

## 文件职责
- 维护 API 请求/响应 DTO 与参数校验规则。
- 保证接口输入输出结构的演进可控。

## 边界
- 仅负责数据结构和校验，不含业务逻辑。
- 与数据库模型解耦，不直接暴露 ORM 实体。

## 命名约定
- `Create`：创建入参
- `Update`：更新入参
- `Detail`：详情响应
- `ListItem`：列表项响应
- `Query`：查询参数

## TODO
- [arch][P1][todo] 在 M1 固化 DTO 命名规范与分页字段约定。
- [auth][P1][todo] 在 M2 完成认证相关 schema。
- [knowledge][P1][todo] 在 M3 完成知识管理与模型管理 schema。

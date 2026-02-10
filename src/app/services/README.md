# services/

## 文件职责
- 编排业务用例，协调 repository/client/infra。
- 承接状态流转、事务边界和跨模块调用。

## 边界
- Service 不直接暴露 HTTP 协议细节。
- Service 不直接管理连接生命周期（由 infra/container 负责）。

## TODO
- [arch][P1][todo] 在 M1 统一 service 接口粒度与命名约定。
- [auth][P1][todo] 在 M2 完成用户与鉴权服务闭环。
- [graph][P2][todo] 在 M7 完成图谱增强相关服务编排。

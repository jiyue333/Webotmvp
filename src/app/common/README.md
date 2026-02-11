# common/

## 模块职责
提供全局共享的基础设施类与工具类，供 service/api/worker 等上层模块统一引用。  
本模块不含任何业务逻辑，仅提供：配置加载、常量定义、错误码、异常体系、统一响应壳、日志配置、安全工具。

## 边界
- **不做**：不处理 HTTP 路由、不管理数据库连接、不持有业务状态。
- **上游**：被 api/service/worker/middleware 等几乎所有模块引用。
- **下游**：除 Python 标准库和 pydantic/FastAPI 类型外，不依赖项目内其他模块。

## 文件清单

| 文件               | 职责                                                                    | 主要阶段 |
| ------------------ | ----------------------------------------------------------------------- | -------- |
| `__init__.py`      | 包入口；统一导出公共符号                                                | M2       |
| `config.py`        | 应用配置（Pydantic Settings），从环境变量 / .env 加载                   | M2       |
| `constants.py`     | 全局常量（分页默认值、文件大小限制、parse_status 枚举字符串等）         | M2       |
| `error_codes.py`   | 业务错误码枚举，按域划分号段（auth/model/kb/knowledge/session/…）       | M2       |
| `error_handler.py` | 全局异常处理器注册（app.add_exception_handler），异常到 HTTP 响应的映射 | M2       |
| `exceptions.py`    | 业务异常基类 `AppError` 及常用子类，由 service 层抛出、api 层捕获       | M2       |
| `response.py`      | 统一响应壳 `ApiResponse[T]` 与分页壳 `PaginatedResponse[T]`             | M2       |
| `logger.py`        | 日志配置与 logger 实例工厂（对齐 WeKnora internal/logger/logger.go）    | M2       |
| `security.py`      | 安全工具：密码哈希（bcrypt）、JWT 生成/验证、敏感字段脱敏               | M2       |

# common/

## 概述

全局配置与通用工具层。存放被所有业务模块共享的基础设施代码，**不含任何网络 I/O 或外部连接**。

## 文件说明

| 文件             | 职责                                    |
| ---------------- | --------------------------------------- |
| `config.py`      | Pydantic Settings，集中管理环境变量配置 |
| `constants.py`   | 全局常量定义                            |
| `security.py`    | JWT 签发/验证、密码哈希工具（纯函数）   |
| `exceptions.py`  | 统一业务异常基类（AppException 等）     |
| `error_codes.py` | 错误码枚举定义                          |
| `logging.py`     | 日志格式化与 logger 配置                |

## 设计原则

- **无 I/O 副作用**：所有文件只做配置读取、工具函数、类型定义，不建立网络连接。
- **被所有层依赖**：api、services、repositories、middleware 都可直接 import common 下的模块。
- 与 `infra/` 的区别：`infra/` 管理有状态连接（DB/Redis），`common/` 只提供纯配置与工具。

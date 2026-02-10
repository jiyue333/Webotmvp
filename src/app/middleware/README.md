# middleware/

## 概述

FastAPI 中间件层。所有 HTTP 请求/响应都会经过这些中间件，**注册顺序影响执行行为**。

## 中间件注册顺序（推荐）

```
请求进入 →
  1. request_id.py    — 生成 X-Request-ID，注入上下文（最外层，确保所有日志都有 request_id）
  2. trace.py         — OpenTelemetry 链路追踪（需要 request_id 已就绪）
  3. logger.py        — 请求/响应日志记录（需要 request_id + trace_id）
  4. recovery.py      — 未捕获异常兜底（防止 500 直接暴露堆栈）
  5. error_handler.py — 业务异常转 HTTP 响应（转换 AppException → JSON 错误体）
  6. auth.py          — JWT 鉴权（最内层，最接近 handler）
→ 到达 Handler
```

> **注意**：FastAPI 中间件的执行顺序是 **后注册的先执行**（LIFO）。所以在 `main.py` 中注册时，`request_id` 应最后注册，`auth` 应最先注册。

## 文件说明

| 文件               | 职责         | 关键行为                      |
| ------------------ | ------------ | ----------------------------- |
| `request_id.py`    | 请求 ID 注入 | 读取或生成 X-Request-ID       |
| `trace.py`         | 链路追踪     | 创建 OpenTelemetry span       |
| `logger.py`        | 请求日志     | 记录请求方法、路径、耗时      |
| `recovery.py`      | 异常兜底     | 捕获未处理异常，返回 500      |
| `error_handler.py` | 业务异常处理 | 将 AppException 转为 JSON     |
| `auth.py`          | JWT 鉴权     | 校验 Token，注入 current_user |

## TODO

- [middleware][M2] 实现 auth.py 的 JWT 校验逻辑
- [middleware][M1] 实现 request_id.py 和 error_handler.py
- [middleware][M6+] 接入 OpenTelemetry trace

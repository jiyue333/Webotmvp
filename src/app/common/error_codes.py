# 文件职责：定义业务错误码枚举，供 service 层和 api 层统一引用。
# 边界：只定义错误码常量；不包含异常类（由 exceptions.py 负责），不处理 HTTP 响应（由 response.py 负责）。

# TODO(M2)：定义 ErrorCode 整型枚举类。按 mvp.md §4.3.3 划分号段：1000-1099 通用, 1100-1199 Auth, 1200-1299 Model, 1300-1399 KB, 1400-1499 Knowledge, 1500-1599 Tag, 1600-1699 Session, 1700-1799 Message, 1800-1899 Chat, 1900-1999 Search。

# 文件职责：用户信息管理服务，负责用户 CRUD 与密码修改（不含鉴权逻辑）。
# 边界：仅操作 users 表的读写，鉴权流程（JWT/token）由 AuthService 负责；不处理 HTTP 请求上下文（当前用户提取由 api/deps.py 的 Depends 注入完成）。
# 对标：WeKnora internal/application/service/user.go（GetUserByID/GetUserByEmail/UpdateUser/DeleteUser/ChangePassword）。

# TODO(M2): 实现 UserService 类骨架。注入 UserRepository。
# TODO(M2): 实现 get_user_by_id()。按 user_id 查询用户（api/deps.py 解析 JWT 后传入 user_id 调用此方法）。
# TODO(M2): 实现 update_user()。更新用户名/邮箱等基本信息。
# TODO(M2): 实现 change_password()。校验旧密码，bcrypt 哈希新密码后更新。

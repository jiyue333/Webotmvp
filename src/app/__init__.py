# 文件职责：app 包入口，标记 src/app 为 Python 包，按需重导出关键对象供外部引用。
# 边界：只做重导出；不包含逻辑实现，各子模块由 main.py 和 container.py 按需导入。

# TODO(M1)：从 app.main 重导出 app 实例，使 uvicorn app:app 或 from app import app 可用。

# 文件职责：定义后端应用的 Docker 镜像构建步骤，包括基础镜像选择、依赖安装、代码复制和启动命令。
# 边界：仅定义构建与运行入口；不包含业务逻辑；依赖列表由 pyproject.toml 管理，运行时配置通过环境变量注入。

# TODO(M1)：补充 Dockerfile 内容。基础镜像 python:3.11-slim，WORKDIR /app，设置 PYTHONDONTWRITEBYTECODE=1 和 PYTHONUNBUFFERED=1。
# TODO(M1)：补充依赖安装步骤。COPY src/pyproject.toml → pip install，利用 Docker layer cache 加速。
# TODO(M1)：补充代码复制步骤。COPY src /app/src，WORKDIR /app/src。
# TODO(M1)：补充启动命令。EXPOSE 8000，CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]。

FROM python:3.11-slim

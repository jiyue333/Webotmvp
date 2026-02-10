# 文件职责：维护镜像构建入口，约束运行时依赖与启动命令。
# 边界：只定义镜像构建步骤；上游由构建工具执行，下游产出运行镜像，不包含业务流程。
# TODO：
# - [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：执行对应模块回归检查并通过；归属模块：`Dockerfile`。

FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY src /app/src
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir fastapi "uvicorn[standard]" sqlalchemy alembic pydantic pytest

WORKDIR /app/src
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

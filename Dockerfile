# 文件职责：维护 `Dockerfile` 的后端镜像构建流程。
# 边界：仅构建 MVP 后端运行镜像，不处理多阶段发布优化与生产级安全加固。
# TODO：
# - [ops][P2][todo] 在 M8 增加非 root 用户、依赖锁定与镜像体积优化。

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

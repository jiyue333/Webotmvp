# 文件职责：定义应用全局配置类（基于 Pydantic Settings），从环境变量或 .env 文件加载配置项。
# 边界：只负责配置声明与校验；不处理连接池初始化（由 infra/ 负责），不包含业务常量（由 constants.py 负责）。

# TODO(M2)：定义 AppSettings(BaseSettings) 配置类。包含 DATABASE_URL / REDIS_URL / NEO4J_URI / SECRET_KEY / DEBUG 等字段，使用 pydantic-settings 的 model_config 指定 env_file=".env"。
# TODO(M2)：提供 get_settings() 工厂函数（使用 lru_cache 缓存），供 container.py 和其他模块获取配置单例。
# TODO(M2)：补充 JWT 相关配置字段（ACCESS_TOKEN_EXPIRE_MINUTES / REFRESH_TOKEN_EXPIRE_DAYS / JWT_ALGORITHM 等）。
# TODO(M5)：补充 MINIO_ENDPOINT / MINIO_ACCESS_KEY / MINIO_SECRET_KEY 等对象存储配置。
# TODO(M7)：补充 NEO4J_ENABLE / NEO4J_USER / NEO4J_PASSWORD 等图谱开关与连接配置。

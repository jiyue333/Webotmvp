# 文件职责：repositories 包入口，按需重导出仓储基类和各具体仓储类，方便外部 from app.repositories import UserRepository 式引用。
# 边界：只负责包级导出；不包含业务逻辑，不直接实例化仓储类（实例化由依赖注入或 service 层负责）。

# TODO(M2)：导出 CrudRepository, SoftDeleteRepository（基类）。
# TODO(M2)：导出 UserRepository, AuthTokenRepository（CrudRepository 子类），供 AuthService 使用。
# TODO(M3)：导出 ModelRepository, KnowledgeBaseRepository, KnowledgeRepository, KnowledgeTagRepository。
# TODO(M4)：导出 SessionRepository, MessageRepository。
# TODO(M5)：导出 ChunkRepository, EmbeddingRepository（CrudRepository 子类）。

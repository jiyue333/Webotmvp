# 文件职责：retriever 包入口，导出检索相关仓储类（PostgresRetrieverRepository、Neo4jRetrieverRepository）。
# 边界：retriever 包专注于检索链路的数据查询（向量相似度/BM25/图检索），与普通 CRUD 仓储（如 EmbeddingRepository）的区别在于：后者负责写入，本包负责查询。

# TODO(M6)：导出 PostgresRetrieverRepository。
# TODO(M7)：导出 Neo4jRetrieverRepository。

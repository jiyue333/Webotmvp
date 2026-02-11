# 文件职责：创建并管理对象存储客户端（MinIO 或本地文件系统），提供文件上传/下载/删除的统一接口。对齐 WeKnora 的文件存储能力。
# 边界：仅负责存储客户端创建与基础文件操作抽象；不处理文件解析（由 docparser/ 负责），不感知业务元数据（由 knowledge service 维护）。

# TODO(M5)：定义 StorageBackend Protocol。声明 upload(path, data) / download(path) / delete(path) / exists(path) 方法签名。
# TODO(M5)：实现 LocalStorageBackend 类。将文件存储到本地磁盘指定目录，作为开发环境默认方案。
# TODO(M5)：实现 MinIOStorageBackend 类。使用 miniopy-async 异步客户端上传/下载/删除 MinIO 对象。
# TODO(M5)：定义 create_storage_client(config) 工厂函数。根据 STORAGE_TYPE 配置选择本地或 MinIO 后端。

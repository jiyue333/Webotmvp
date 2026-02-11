# 文件职责：创建并管理 Redis 异步客户端连接，提供缓存/队列/流式事件存储的 Redis 访问入口。对齐 WeKnora 的 Redis 连接初始化。
# 边界：仅负责 Redis 客户端创建与连接验证；不实现业务级缓存策略（由 service/stream/worker 层使用），不感知具体 key 结构。

# TODO(M2)：定义 create_redis_client(redis_url) 函数。使用 redis.asyncio.from_url 创建异步 Redis 客户端，配置 decode_responses / max_connections 等参数。
# TODO(M2)：定义 init_redis(client) 协程。应用启动时 ping 验证 Redis 连接是否正常。
# TODO(M2)：定义 close_redis(client) 协程。应用关闭时调用 client.aclose() 释放连接。

# 文件职责：定义分层仓储基类。CrudRepository 封装通用 CRUD 操作（get_by_id/create/update/hard_delete/list），不假设任何删除策略；SoftDeleteRepository 继承 CrudRepository 并加入软删除过滤与 soft_delete 方法。对齐 WeKnora internal/application/repository 的通用仓储模式。
# 边界：只封装通用持久化操作与 SQLAlchemy session 管理；不包含业务判断、不感知具体表结构。主键类型不限定 UUID，get_by_id/update/hard_delete 的 id 参数接受任意主键类型（str/int），由 SQLAlchemy 自动适配。AuthToken/Embedding 等无 deleted_at 的模型继承 CrudRepository，其他模型继承 SoftDeleteRepository。

# TODO(M2)：定义 CrudRepository 类，接收 AsyncSession 和 model class 作为构造参数。
# TODO(M2)：实现 CrudRepository.get_by_id(id) 方法。纯主键查询，不附加任何过滤条件。
# TODO(M2)：实现 CrudRepository.create(data) 方法。接收 dict 或 schema，创建记录并 flush 返回实例。
# TODO(M2)：实现 CrudRepository.update(id, data) 方法。部分更新，自动设置 updated_at（若模型包含该列）。
# TODO(M2)：实现 CrudRepository.hard_delete(id) 方法。物理删除记录。
# TODO(M3)：实现 CrudRepository.list_with_pagination(page, page_size, filters) 方法。支持过滤条件、分页和总数返回。

# TODO(M2)：定义 SoftDeleteRepository(CrudRepository) 类。
# TODO(M2)：重写 get_by_id(id) 方法。在父类基础上追加 deleted_at IS NULL 过滤。
# TODO(M2)：重写 list_with_pagination 方法。在父类基础上追加 deleted_at IS NULL 过滤。
# TODO(M2)：实现 soft_delete(id) 方法。设置 deleted_at = now()，不物理删除。

# 文件职责：Alembic 迁移脚本模板（Mako），定义 `alembic revision --autogenerate` 自动生成的迁移版本文件的代码骨架。
# 边界：仅作为模板被 Alembic 内部引擎渲染；不直接执行，不包含业务逻辑；修改此模板会影响所有后续自动生成的迁移脚本格式。

# TODO(M1)：补充标准 Mako 模板内容。包含 revision/down_revision 变量、imports、upgrade()/downgrade() 函数骨架。参考 Alembic 官方默认模板。

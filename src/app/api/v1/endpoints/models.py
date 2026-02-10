# 文件职责：定义模型管理相关的 HTTP 路由（provider 列表、模型 CRUD）。
# 边界：仅处理请求参数校验与响应封装，模型配置逻辑委托给 ModelService，不直接操作数据库。

from fastapi import APIRouter

router = APIRouter()

# TODO(M3)：实现 GET /providers 模型厂商列表端点。返回系统支持的 provider 类型列表（如 openai/anthropic/ollama 等），包含各厂商的默认 base_url。
# TODO(M3)：实现 POST / 创建模型端点。接收 provider/model_name/model_type/api_key/base_url 等配置，调用 ModelService.create()。
# TODO(M3)：实现 GET / 模型列表端点。支持按 provider 和 model_type（chat/embedding/rerank）筛选，返回已配置的模型列表。
# TODO(M3)：实现 GET /{id} 模型详情端点。返回单个模型配置信息（api_key 需脱敏）。
# TODO(M3)：实现 PUT /{id} 更新模型端点。接收可选的配置字段，调用 ModelService.update()。
# TODO(M3)：实现 DELETE /{id} 删除模型端点。调用 ModelService.delete()，检查是否有知识库依赖该模型。

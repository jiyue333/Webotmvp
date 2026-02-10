# 文件职责：common 包入口；统一导出公共符号，供上层模块 `from app.common import ...` 使用。
# 边界：仅做 re-export，不包含实现逻辑；不依赖项目内其他模块。

# TODO(M2)：当 config.py / constants.py / response.py 完成后，在此补充对应的 re-export。

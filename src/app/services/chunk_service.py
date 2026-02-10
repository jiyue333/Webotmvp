"""
文件职责：维护 `src/app/services/chunk_service.py` 的 M1 骨架与结构约束。
边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
TODO：
- [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。
"""

# services/chunk_service.py
"""
文件职责：文本分块管理服务（ChunkService）。
边界：负责 chunk 的存储、查询、删除等管理操作；分块算法本身由 docparser/splitter 负责。
TODO [chunk][M5] 实现 create_chunks、get_chunks_by_knowledge_id、delete_chunks 等方法。
"""

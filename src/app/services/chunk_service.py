# services/chunk_service.py
"""
文件职责：文本分块管理服务（ChunkService）。
边界：负责 chunk 的存储、查询、删除等管理操作；分块算法本身由 docparser/splitter 负责。
TODO [chunk][M5] 实现 create_chunks、get_chunks_by_knowledge_id、delete_chunks 等方法。
"""

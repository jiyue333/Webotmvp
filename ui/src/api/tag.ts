// 文件职责：封装 Knowledge Tag 相关 HTTP 接口（CRUD）。
// 边界：处理 /api/v1/knowledge-bases/{id}/tags 路径下的增删改查；不包含知识库本身的管理。

export interface TagItem {
  id: string
  knowledge_base_id: string
  name: string
  color?: string
  sort_order?: number
  created_at?: string
  updated_at?: string
}

export const tagApi = {
  list: (_kbId: string): Promise<TagItem[]> => {
    throw new Error('Not implemented')
  },
  create: (_kbId: string, _data: { name: string; color?: string; sort_order?: number }): Promise<TagItem> => {
    throw new Error('Not implemented')
  },
  update: (_kbId: string, _tagId: string, _data: Partial<TagItem>): Promise<TagItem> => {
    throw new Error('Not implemented')
  },
  delete: (_kbId: string, _tagId: string): Promise<void> => {
    throw new Error('Not implemented')
  }
}

// TODO(M3)：实现 list，GET /api/v1/knowledge-bases/{id}/tags，含关联知识数量。
// TODO(M3)：实现 create，POST /api/v1/knowledge-bases/{id}/tags，同 KB 下 name 唯一。
// TODO(M3)：实现 update，PUT /api/v1/knowledge-bases/{id}/tags/{tag_id}，可选字段更新。
// TODO(M3)：实现 delete，DELETE /api/v1/knowledge-bases/{id}/tags/{tag_id}，关联知识的 tag_id 置空。

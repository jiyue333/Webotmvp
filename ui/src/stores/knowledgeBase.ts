// 文件职责：维护 knowledgeBase 状态仓库（列表、当前选中），统一知识库相关状态读写。
// 边界：只维护前端状态与动作；上游由视图触发，下游调用 api/knowledgeBase 模块。

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useKnowledgeBaseStore = defineStore('knowledgeBase', () => {
  const list = ref<any[]>([])
  const currentId = ref<string | null>(null)

  async function fetchList() {
    throw new Error('Not implemented')
  }

  return { list, currentId, fetchList }
})

// TODO(M3)：实现 fetchList Action，调用 api/knowledgeBase.listKnowledgeBases()，更新 list state。
// TODO(M3)：实现 create/update/delete Action，分别调用对应 API 并刷新列表。

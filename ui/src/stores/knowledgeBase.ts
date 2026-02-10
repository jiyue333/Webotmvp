/**
 * 文件职责：知识库状态管理（Pinia Store）。
 * TODO [kb][M3] 实现知识库列表、当前选中知识库等状态。
 */
import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useKnowledgeBaseStore = defineStore('knowledgeBase', () => {
    const list = ref<{ id: string; name: string }[]>([])
    const currentId = ref<string | null>(null)

    // TODO [kb][M3] 实现 fetchList、selectKB 等 action

    return { list, currentId }
})

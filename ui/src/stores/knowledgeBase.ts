/**
 * 文件职责：维护 `ui/src/stores/knowledgeBase.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [knowledge][P1][todo] 在 M3 完成本模块能力实现与回归验证。
 */

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useKnowledgeBaseStore = defineStore('knowledgeBase', () => {
    const list = ref<{ id: string; name: string }[]>([])
    const currentId = ref<string | null>(null)

    // TODO [kb][M3] 实现 fetchList、selectKB 等 action

    return { list, currentId }
})

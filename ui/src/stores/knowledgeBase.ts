/**
 * 文件职责：维护 `knowledgeBase` 状态仓库，统一页面状态读写与派发入口。
 * 边界：只维护前端状态与动作；上游由视图触发，下游调用 api 模块，不直接拼装网络协议。
 * TODO：
 * - [knowledge][P1][todo] 完成条件：补齐知识条目管理与状态流转约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/knowledgeBase.ts`。
 */

import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useKnowledgeBaseStore = defineStore('knowledgeBase', () => {
    const list = ref<{ id: string; name: string }[]>([])
    const currentId = ref<string | null>(null)

    // [kb][P1][todo] 完成条件：实现 fetchList、selectKB 等 action；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/stores/knowledgeBase.ts`。

    return { list, currentId }
})

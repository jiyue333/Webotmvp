<!--
文件职责：承载 `KnowledgeBaseView` 页面交互逻辑与展示职责，编排用户动作与状态反馈。
边界：只负责页面渲染与交互编排；上游接收路由进入，下游调用 store/api，不沉淀底层请求实现。
TODO：
- [knowledge][P1][todo] 完成条件：补齐知识条目管理与状态流转约束；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/views/KnowledgeBaseView.vue`。
-->

<template>
  <section class="page">
    <h1>知识库</h1>
    <p class="muted">M1 骨架阶段展示基础列表，M2/M3 补充创建与编辑操作。</p>

    <div class="toolbar">
      <button class="btn btn-ghost" @click="refresh">刷新</button>
    </div>

    <ul v-if="items.length" class="list">
      <li v-for="item in items" :key="item.id" class="list-item">
        <div>
          <strong>{{ item.name }}</strong>
          <p class="muted">{{ item.description || '暂无描述' }}</p>
        </div>
        <code>{{ item.id }}</code>
      </li>
    </ul>

    <p v-else class="muted">暂无知识库数据。</p>
    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
/**
 * 文件职责：知识库列表页，承接知识库管理主入口。
 * [knowledge][P1][todo] 完成条件：补充创建/更新/删除、分页与筛选。；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/views/KnowledgeBaseView.vue`。
 */
import { onMounted, ref } from 'vue'
import { listKnowledgeBases } from '../api/knowledgeBase'
import type { KnowledgeBaseItem } from '../types/api'

const items = ref<KnowledgeBaseItem[]>([])
const error = ref('')

async function refresh() {
  // 刷新知识库列表，失败时在页面保留可读错误提示。
  error.value = ''
  try {
    items.value = await listKnowledgeBases()
  } catch (err) {
    error.value = err instanceof Error ? err.message : '加载知识库失败'
  }
}

// 首次进入页面自动拉取列表。
onMounted(refresh)
</script>

<style scoped>
.toolbar {
  margin: 14px 0;
}

.list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: 10px;
}

.list-item {
  display: flex;
  justify-content: space-between;
  align-items: start;
  padding: 12px;
  border: 1px solid var(--border);
  border-radius: 10px;
}

.error {
  color: var(--danger);
}
</style>

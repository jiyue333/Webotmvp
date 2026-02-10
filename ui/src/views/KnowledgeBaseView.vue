<!--
文件职责：维护 `ui/src/views/KnowledgeBaseView.vue` 的 M1 骨架与结构约束。
边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
TODO：
- [knowledge][P1][todo] 在 M3 完成本模块能力实现与回归验证。
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
 * TODO：补充创建/更新/删除、分页与筛选。
 */
import { onMounted, ref } from 'vue'
import { listKnowledgeBases } from '../api/knowledgeBase'
import type { KnowledgeBaseItem } from '../types/api'

const items = ref<KnowledgeBaseItem[]>([])
const error = ref('')

async function refresh() {
  error.value = ''
  try {
    items.value = await listKnowledgeBases()
  } catch (err) {
    error.value = err instanceof Error ? err.message : '加载知识库失败'
  }
}

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

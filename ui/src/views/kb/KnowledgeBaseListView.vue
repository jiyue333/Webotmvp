<!--
文件职责：知识库列表管理页面，包含创建、删除、查看入口。
边界：负责列表展示与操作交互；不处理具体的知识入库逻辑。
-->
<template>
  <div class="kb-list-view">
    <h1>Knowledge Bases</h1>
    <!-- List Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'KnowledgeBaseListView' })
</script>

<!-- TODO(M3)：对接 KnowledgeBase Store 实现列表加载。 -->
<!-- TODO(M3)：实现新建知识库按钮（弹出 KbCreateModal）。 -->
<!-- TODO(M3)：实现知识库卡片/列表项（点击进入详情页）。 -->
<!-- TODO(M3)：实现知识库删除操作。 -->

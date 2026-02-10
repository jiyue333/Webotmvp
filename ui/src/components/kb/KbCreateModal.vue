<!--
文件职责：新建知识库弹窗组件。
边界：负责表单收集与校验（名称、描述、Embedding 模型）；提交动作委托给父组件或 Store。
-->
<template>
  <div class="kb-create-modal">
    <!-- Create KB Form Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'KbCreateModal' })
</script>

<!-- TODO(M3)：实现表单字段：名称（必填）、描述、Embedding 模型选择（下拉加载 modelApi.list）。 -->
<!-- TODO(M3)：实现表单校验与提交，调用 knowledgeBase.createKnowledgeBase()。 -->

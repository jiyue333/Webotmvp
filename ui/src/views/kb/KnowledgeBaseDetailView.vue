<!--
文件职责：知识库详情页，管理知识文档的导入、列表展示与状态查看。
边界：负责知识文档的上传/导入入口；不处理具体解析逻辑（由后端 Worker 异步完成）。
-->
<template>
  <div class="kb-detail-view">
    <h1>Knowledge Base Detail</h1>
    <!-- Knowledge List Placeholder -->
    <!-- Upload/Settings Buttons Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'KnowledgeBaseDetailView' })
</script>

<!-- TODO(M3)：引入 KbUploadModal 和 KbSettingsModal 组件。 -->
<!-- TODO(M3)：实现文件/URL/文本导入入口按钮。 -->
<!-- TODO(M3)：实现知识文档列表加载（含 parse_status 状态标签）。 -->
<!-- TODO(M3)：实现知识文档删除操作。 -->

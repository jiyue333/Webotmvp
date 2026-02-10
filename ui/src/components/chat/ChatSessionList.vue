<!--
文件职责：展示和管理历史会话列表（侧边栏）。
边界：仅处理会话列表的渲染与选中状态切换；数据获取依赖 stores/session。
-->
<template>
  <div class="chat-session-list">
    <!-- Session List Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'ChatSessionList' })
</script>

<!-- TODO(M4)：对接 Session Store 实现列表加载与选中态切换。 -->
<!-- TODO(M4)：实现新建会话按钮。 -->
<!-- TODO(M4)：实现会话删除与重命名交互。 -->

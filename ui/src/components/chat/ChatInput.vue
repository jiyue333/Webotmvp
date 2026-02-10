<!--
文件职责：处理用户消息输入与发送操作。
边界：仅负责输入框状态与快捷键监听；发送动作通过 emit 委托给父组件（ChatView）。
-->
<template>
  <div class="chat-input">
    <!-- Input Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'ChatInput' })
</script>

<!-- TODO(M4)：实现文本输入框，支持 Enter 发送、Shift+Enter 换行。 -->
<!-- TODO(M4)：实现发送按钮与加载中状态锁定。 -->

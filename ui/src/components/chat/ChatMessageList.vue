<!--
文件职责：渲染当前会话的消息流（用户消息 + AI 回复）。
边界：仅展示消息内容（Markdown 渲染、流式打字机效果）；不处理消息发送逻辑。
-->
<template>
  <div class="chat-message-list">
    <!-- Message List Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'ChatMessageList' })
</script>

<!-- TODO(M4)：实现消息列表渲染，区分 user/assistant 角色样式。 -->
<!-- TODO(M4)：实现 Markdown 渲染（可选 markdown-it 或 marked）。 -->
<!-- TODO(M4)：实现流式打字机效果（逐 token 追加）。 -->
<!-- TODO(M4)：实现知识引用展示（references 折叠面板）。 -->

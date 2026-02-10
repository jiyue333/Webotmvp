<!--
文件职责：RAG 对话交互界面，编排会话列表、消息流展示与输入组件。
边界：负责用户与 AI 的对话交互页面布局；不处理 RAG 检索的具体流程，仅展示结果。
-->
<template>
  <div class="chat-view">
    <!-- ChatSessionList Placeholder -->
    <!-- ChatMessageList Placeholder -->
    <!-- ChatInput Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'ChatView' })
</script>

<!-- TODO(M4)：引入 ChatSessionList、ChatMessageList、ChatInput 组件并编排布局。 -->
<!-- TODO(M4)：对接 Session/Chat Store，处理会话切换与消息加载。 -->
<!-- TODO(M4)：对接 SSE 流式响应，实现打字机效果。 -->

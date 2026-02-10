<!--
文件职责：知识库配置与管理弹窗（修改元数据、分块参数、模型参数）。
边界：修改知识库元数据与配置参数；提交修改调用 api/knowledgeBase。
-->
<template>
  <div class="kb-settings-modal">
    <!-- Settings Modal Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'KbSettingsModal' })
</script>

<!-- TODO(M3)：实现知识库设置表单（名称、描述、chunking_config）。 -->
<!-- TODO(M3)：实现 Embedding 模型切换（需提示重新向量化风险）。 -->

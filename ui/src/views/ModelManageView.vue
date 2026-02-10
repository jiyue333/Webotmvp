<!--
文件职责：模型管理页面，展示 Provider 列表与模型 CRUD 操作。
边界：负责模型的增删改查界面交互；不处理模型调用与推理逻辑。
-->
<template>
  <div class="model-manage-view">
    <h1>Model Management</h1>
    <!-- Provider List Placeholder -->
    <!-- Model List Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'ModelManageView' })
</script>

<!-- TODO(M3)：实现 Provider 列表展示（调用 modelApi.listProviders()）。 -->
<!-- TODO(M3)：实现模型列表（按 type 分组：llm/embedding/rerank）。 -->
<!-- TODO(M3)：实现模型创建弹窗（name/type/source/parameters）。 -->
<!-- TODO(M3)：实现模型编辑与删除操作。 -->

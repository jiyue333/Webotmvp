<!--
文件职责：提供文档上传与导入交互界面（文件上传、URL 导入、手工录入）。
边界：处理文件选择、拖拽与参数配置；上传动作调用 api/knowledge。
-->
<template>
  <div class="kb-upload-modal">
    <!-- Upload Modal Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'KbUploadModal' })
</script>

<!-- TODO(M3)：实现文件选择/拖拽上传，支持 PDF/DOCX/MD/TXT/CSV/XLSX。 -->
<!-- TODO(M3)：实现 URL 导入表单。 -->
<!-- TODO(M3)：实现手工 Markdown 录入表单。 -->

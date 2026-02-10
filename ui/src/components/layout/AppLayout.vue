<!--
文件职责：应用核心布局组件，包含侧边栏导航和主内容区域。
边界：负责整体布局框架渲染（侧边栏 + 顶栏 + 内容区）；不处理具体页面业务逻辑。
-->
<template>
  <div class="app-layout">
    <!-- Sidebar Placeholder -->
    <!-- TopBar Placeholder -->
    <router-view />
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'AppLayout' })
</script>

<!-- TODO(M1)：实现侧边栏导航（知识库、对话、模型管理入口）。 -->
<!-- TODO(M1)：实现响应式布局（移动端侧边栏折叠）。 -->

<template>
  <AppShell>
    <router-view />
  </AppShell>
</template>

<script setup lang="ts">
/**
 * 文件职责：应用根组件，承载全局布局与路由视图。
 * TODO：按设计稿补充全局通知、全局 loading、错误边界。
 */
import AppShell from './components/layout/AppShell.vue'
</script>

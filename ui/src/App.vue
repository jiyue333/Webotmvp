<!--
文件职责：维护 `ui/src/App.vue` 的 M1 骨架与结构约束。
边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
TODO：
- [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。
-->

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

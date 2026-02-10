<!--
文件职责：维护前端组件职责边界，承接渲染与交互逻辑。
边界：只描述本文件边界与上下游关系；不在此实现跨阶段业务闭环。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/App.vue`。
-->

<template>
  <AppShell>
    <router-view />
  </AppShell>
</template>

<script setup lang="ts">
/**
 * 文件职责：应用根组件，承载全局布局与路由视图。
 * [arch][P1][todo] 完成条件：按设计稿补充全局通知、全局 loading、错误边界。；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/App.vue`。
 */
import AppShell from './components/layout/AppShell.vue'
</script>

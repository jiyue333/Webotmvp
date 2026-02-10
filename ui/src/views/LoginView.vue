<!--
文件职责：用户登录页面，承载登录表单交互与跳转逻辑。
边界：只负责页面渲染与交互编排；上游接收路由进入，下游调用 stores/auth，不沉淀底层请求实现。
-->
<template>
  <div class="login-view">
    <h1>WeKnora Login</h1>
    <!-- Login Form Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'LoginView' })
</script>

<!-- TODO(M2)：实现登录表单（email/password），调用 authStore.login()。 -->
<!-- TODO(M2)：实现登录成功后跳转至 Dashboard 或知识库列表。 -->
<!-- TODO(M2)：添加"前往注册"链接。 -->

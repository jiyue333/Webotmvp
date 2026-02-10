<!--
文件职责：用户注册页面，承载注册表单交互与跳转逻辑。
边界：只负责页面渲染与交互编排；上游接收路由进入，下游调用 stores/auth，不沉淀底层请求实现。
-->
<template>
  <div class="register-view">
    <h1>WeKnora Register</h1>
    <!-- Register Form Placeholder -->
  </div>
</template>

<script setup lang="ts">
defineOptions({ name: 'RegisterView' })
</script>

<!-- TODO(M2)：实现注册表单（username/email/password/确认密码），调用 authStore 或 api/auth.register()。 -->
<!-- TODO(M2)：实现注册成功后跳转至登录页。 -->
<!-- TODO(M2)：添加"前往登录"链接。 -->

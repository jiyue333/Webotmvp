<!--
文件职责：维护可复用前端组件，承接布局与通用交互渲染。
边界：只负责组件渲染与复用交互；上游由页面组合，下游依赖 store/api 的公开能力，不持久化业务数据。
TODO：
- [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/components/layout/AppShell.vue`。
-->

<template>
  <div class="shell">
    <header class="shell-header">
      <div class="brand">WeKnora MVP</div>
      <nav class="nav">
        <router-link to="/knowledge-bases">知识库</router-link>
        <router-link to="/chat">对话</router-link>
      </nav>
      <div class="actions">
        <span v-if="auth.user" class="muted">{{ auth.user.username }}</span>
        <button v-if="auth.isAuthenticated" class="btn btn-ghost" @click="onLogout">退出</button>
      </div>
    </header>

    <main class="shell-main">
      <slot />
    </main>
  </div>
</template>

<script setup lang="ts">
/**
 * 文件职责：应用公共布局，统一导航和登录态操作入口。
 * [arch][P1][todo] 完成条件：补充面包屑、租户切换占位（若未来恢复多租户）。；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/components/layout/AppShell.vue`。
 */
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

const auth = useAuthStore()
const router = useRouter()

async function onLogout() {
  // 退出后统一返回登录页，避免保留受保护页面状态。
  await auth.logout()
  await router.push({ name: 'login' })
}
</script>

<style scoped>
.shell {
  min-height: 100vh;
}

.shell-header {
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
}

.brand {
  font-weight: 700;
}

.nav {
  display: flex;
  gap: 20px;
}

.nav a.router-link-active {
  color: var(--brand);
  font-weight: 600;
}

.actions {
  display: flex;
  gap: 10px;
  align-items: center;
}

.shell-main {
  max-width: 1080px;
  margin: 20px auto;
  padding: 0 16px 24px;
}
</style>

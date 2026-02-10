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
 * TODO：补充面包屑、租户切换占位（若未来恢复多租户）。
 */
import { useRouter } from 'vue-router'
import { useAuthStore } from '../../stores/auth'

const auth = useAuthStore()
const router = useRouter()

async function onLogout() {
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

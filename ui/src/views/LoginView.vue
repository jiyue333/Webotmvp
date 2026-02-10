<!--
文件职责：维护 `ui/src/views/LoginView.vue` 的 M1 骨架与结构约束。
边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
TODO：
- [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。
-->

<template>
  <section class="page login-page">
    <h1>登录</h1>
    <p class="muted">使用已注册账号进入 WeKnora MVP。</p>

    <form class="form" @submit.prevent="onSubmit">
      <label>
        <span>邮箱</span>
        <input v-model="form.email" class="input" type="email" required />
      </label>

      <label>
        <span>密码</span>
        <input v-model="form.password" class="input" type="password" required />
      </label>

      <button class="btn btn-primary" :disabled="loading" type="submit">
        {{ loading ? '登录中...' : '登录' }}
      </button>
    </form>

    <p v-if="error" class="error">{{ error }}</p>
  </section>
</template>

<script setup lang="ts">
/**
 * 文件职责：登录页面，完成用户认证入口。
 * TODO：补充注册入口、忘记密码和更细致错误码提示。
 */
import { reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '../stores/auth'

const router = useRouter()
const route = useRoute()
const auth = useAuthStore()

const form = reactive({
  email: '',
  password: ''
})
const loading = ref(false)
const error = ref('')

async function onSubmit() {
  loading.value = true
  error.value = ''

  try {
    await auth.login({ email: form.email, password: form.password })
    const redirect = (route.query.redirect as string | undefined) ?? '/knowledge-bases'
    await router.push(redirect)
  } catch (err) {
    error.value = err instanceof Error ? err.message : '登录失败，请检查账号信息'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.login-page {
  max-width: 420px;
  margin: 40px auto;
}

.form {
  display: grid;
  gap: 14px;
  margin-top: 18px;
}

label {
  display: grid;
  gap: 6px;
}

.error {
  margin-top: 12px;
  color: var(--danger);
}
</style>

/**
 * 文件职责：维护 `ui/src/router/index.ts` 的 M1 骨架与结构约束。
 * 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
 * TODO：
 * - [arch][P1][todo] 在 M1 完成本模块能力实现与回归验证。
 */

import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '../stores/auth'
import LoginView from '../views/LoginView.vue'
import KnowledgeBaseView from '../views/KnowledgeBaseView.vue'
import ChatView from '../views/ChatView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      redirect: '/knowledge-bases'
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/knowledge-bases',
      name: 'knowledge-bases',
      component: KnowledgeBaseView,
      meta: { requiresAuth: true }
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView,
      meta: { requiresAuth: true }
    }
  ]
})

router.beforeEach(async (to) => {
  const auth = useAuthStore()

  if (auth.isAuthenticated && !auth.user) {
    try {
      await auth.loadProfile()
    } catch {
      await auth.logout()
    }
  }

  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    return { name: 'login', query: { redirect: to.fullPath } }
  }

  if (to.name === 'login' && auth.isAuthenticated) {
    return { name: 'knowledge-bases' }
  }

  return true
})

export default router

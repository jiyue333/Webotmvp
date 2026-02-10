/**
 * 文件职责：维护前端路由表与守卫策略，控制页面访问路径与登录态校验。
 * 边界：只负责路由表与守卫编排；上游由应用入口装载，下游驱动页面切换，不承载业务状态存储。
 * TODO：
 * - [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/router/index.ts`。
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

/**
 * 统一路由守卫：
 * 1) 已登录但缺少用户信息时先拉取 profile；
 * 2) 未登录访问受保护路由时跳转登录页并带回跳参数；
 * 3) 已登录访问登录页时重定向到知识库首页。
 */
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

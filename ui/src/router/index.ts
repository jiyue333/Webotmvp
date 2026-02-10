// 文件职责：维护前端路由表与导航守卫策略，控制页面访问路径与登录态校验。
// 边界：只负责路由声明与守卫编排；不承载业务状态存储。

import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/RegisterView.vue')
    },
    {
      path: '/',
      component: () => import('../components/layout/AppLayout.vue'),
      meta: { requiresAuth: true },
      children: [
        {
          path: '',
          redirect: 'knowledge-bases'
        },
        {
          path: 'dashboard',
          name: 'dashboard',
          component: () => import('../views/DashboardView.vue')
        },
        {
          path: 'knowledge-bases',
          name: 'kb-list',
          component: () => import('../views/kb/KnowledgeBaseListView.vue')
        },
        {
          path: 'knowledge-bases/:id',
          name: 'kb-detail',
          component: () => import('../views/kb/KnowledgeBaseDetailView.vue')
        },
        {
          path: 'models',
          name: 'model-manage',
          component: () => import('../views/ModelManageView.vue')
        },
        {
          path: 'chat',
          name: 'chat',
          component: () => import('../views/ChatView.vue')
        },
        {
          path: 'chat/:sessionId',
          name: 'chat-session',
          component: () => import('../views/ChatView.vue')
        }
      ]
    }
  ]
})

export default router

// TODO(M2)：实现 beforeEach 导航守卫，检查 requiresAuth 并验证 token 有效性。
// TODO(M2)：未登录用户重定向至 /login，已登录用户访问 /login 重定向至首页。

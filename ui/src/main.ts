/**
 * 文件职责：维护前端 TypeScript 模块职责边界，承接状态与调用编排。
 * 边界：只描述本文件边界与上下游关系；不在此实现跨阶段业务闭环。
 * TODO：
 * - [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/src/main.ts`。
 */

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './style.css'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')

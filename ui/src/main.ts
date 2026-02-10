// 文件职责：应用入口，挂载 Vue 实例、Pinia 状态管理、Vue Router。
// 边界：仅负责应用初始化与插件注册；不包含业务逻辑。

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import './style.css'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')

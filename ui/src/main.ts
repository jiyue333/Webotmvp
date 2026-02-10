/**
 * 文件职责：前端应用入口，挂载 Router/Pinia 并启动 Vue App。
 * TODO：后续在这里接入全局异常上报与埋点初始化。
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

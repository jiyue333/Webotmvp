/**
 * 文件职责：维护前端构建与开发服务器配置，约束代理与打包入口。
 * 边界：只描述本文件边界与上下游关系；不在此实现跨阶段业务闭环。
 * TODO：
 * - [arch][P1][todo] 完成条件：形成可执行的分层契约并消除职责重叠；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/vite.config.ts`。
 */

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})

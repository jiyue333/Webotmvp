/**
 * 文件职责：Vite 构建配置，统一前端开发与打包行为。
 * TODO：按部署环境补充更细粒度 proxy 与构建优化策略。
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

// 文件职责：全局 HTTP 请求客户端封装（Axios 实例）。
// 边界：仅处理 Axios 实例配置、拦截器挂载；不包含具体业务 API。

import axios from 'axios'

const http = axios.create({})

export default http

// TODO(M1)：配置 baseURL（读取 VITE_API_BASE_URL）和 timeout。
// TODO(M2)：实现请求拦截器（注入 Authorization Token）。
// TODO(M2)：实现响应拦截器（统一错误处理、401 跳转登录）。

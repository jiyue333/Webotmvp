# 文件职责：维护 `ui/Dockerfile` 的 M1 骨架与结构约束。
# 边界：仅定义职责边界与调用契约，不在本文件实现 M2-M8 的完整业务闭环。
# TODO：
# - [ops][P2][todo] 在 M8 完成本模块能力实现与回归验证。

# 阶段一：构建
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

# 阶段二：Nginx 托管
FROM nginx:1.27-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

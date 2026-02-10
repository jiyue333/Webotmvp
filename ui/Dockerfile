# 文件职责：维护前端镜像构建流程，约束构建与静态托管步骤。
# 边界：只定义镜像构建步骤；上游由构建工具执行，下游产出运行镜像，不包含业务流程。
# TODO：
# - [ops][P2][todo] 完成条件：补齐运行脚本与部署配置检查项；验证方式：执行 `cd ui && npm run build` 并通过页面基础联调；归属模块：`ui/Dockerfile`。

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

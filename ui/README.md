# ui/

## 文件职责
- 维护 Vue3 前端骨架、路由、状态管理与 API 访问层。
- 承接 MVP 阶段页面与后端接口联调入口。

## 边界
- 仅覆盖 MVP 所需页面，不复现原项目完整前端能力。
- UI 层不实现后端业务规则，仅做展示与交互编排。

## 启动方式
```bash
cd ui
npm install
npm run dev
```

## TODO
- [auth][P1][todo] 在 M2 完成登录态 refresh 续期与异常映射。
- [knowledge][P1][todo] 在 M3 完成模型与知识库 CRUD 页面联调。
- [chat][P1][todo] 在 M4 打通 SSE 对话与 stop/continue-stream 交互。
- [graph][P2][todo] 在 M7 增加图谱增强引用展示与可视化占位。

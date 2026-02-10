/// <reference types="vite/client" />
// 文件职责：声明 Vite 环境变量的 TypeScript 类型，供全局引用。
// 边界：仅包含环境变量类型声明；不包含运行时逻辑。

interface ImportMetaEnv {
  readonly VITE_API_BASE_URL?: string
}

interface ImportMeta {
  readonly env: ImportMetaEnv
}

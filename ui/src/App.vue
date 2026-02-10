<!--
文件职责：应用根组件，提供全局配置（Element Plus 国际化、主题）和路由出口。
边界：仅负责全局 Provider 包裹与 RouterView 渲染；不包含页面业务逻辑。
-->
<template>
  <el-config-provider :locale="zhCn">
    <router-view />
  </el-config-provider>
</template>

<script setup lang="ts">
import { ElConfigProvider } from 'element-plus'
import zhCn from 'element-plus/es/locale/lang/zh-cn'

// TODO(M1)：根据设计稿补充全局主题配置（暗色模式、品牌色变量）。
</script>

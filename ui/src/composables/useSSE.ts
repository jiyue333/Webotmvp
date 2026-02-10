// 文件职责：封装 SSE（Server-Sent Events）流式接收逻辑为 Vue Composable。
// 边界：仅处理 SSE 连接建立、事件解析与状态管理；不包含具体业务逻辑（由调用方处理事件数据）。

export function useSSE() {
    throw new Error('Not implemented')
}

// TODO(M4)：实现 useSSE composable，接收 URL 和 options，返回 { data, error, isConnected, close }。
// TODO(M4)：解析 SSE 事件流，对齐 mvp.md §4.3.4 格式（id/response_type/content/done/knowledge_references）。
// TODO(M4)：实现 Last-Event-ID 自动回传，支持断线重连（对接 continue-stream API）。
// TODO(M4)：实现 close 方法，用于停止接收（配合 session stop API）。

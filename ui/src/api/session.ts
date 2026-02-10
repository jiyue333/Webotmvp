// 文件职责：定义会话管理相关的 HTTP 接口（CRUD + stop + continue-stream）。
// 边界：仅定义接口签名与类型；不包含状态管理逻辑。

export interface SessionItem {
    id: string
    knowledge_base_id: string
    title: string
    created_at?: string
    updated_at?: string
}

export const sessionApi = {
    list: (): Promise<SessionItem[]> => {
        throw new Error('Not implemented')
    },
    getById: (_id: string): Promise<SessionItem> => {
        throw new Error('Not implemented')
    },
    create: (_data: { knowledge_base_id: string; title?: string }): Promise<SessionItem> => {
        throw new Error('Not implemented')
    },
    update: (_id: string, _title: string): Promise<SessionItem> => {
        throw new Error('Not implemented')
    },
    delete: (_id: string): Promise<void> => {
        throw new Error('Not implemented')
    },
    stop: (_sessionId: string): Promise<void> => {
        throw new Error('Not implemented')
    }
}

// TODO(M4)：实现 list，GET /api/v1/sessions，按最后活跃时间倒序。
// TODO(M4)：实现 getById，GET /api/v1/sessions/{id}。
// TODO(M4)：实现 create，POST /api/v1/sessions，接收 knowledge_base_id 和可选 title。
// TODO(M4)：实现 update，PUT /api/v1/sessions/{id}，更新会话标题。
// TODO(M4)：实现 delete，DELETE /api/v1/sessions/{id}，级联删除消息。
// TODO(M4)：实现 stop，POST /api/v1/sessions/{session_id}/stop，停止流式生成。
// TODO(M4)：实现 continueStream，GET /api/v1/sessions/continue-stream/{session_id}，SSE 回放。

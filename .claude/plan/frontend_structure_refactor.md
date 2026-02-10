# Frontend Structure Refactoring Plan

Based on the design analysis of `design.pen` and the current `ui/src` structure.

## 1. Cleanup
- [ ] Delete `ui/src/views/ModelView.vue` (Not in design scope)

## 2. Create New Components
### Chat Components
- [ ] Create `ui/src/components/chat/` directory
- [ ] Create `ui/src/components/chat/ChatSessionList.vue` (Sidebar session list)
- [ ] Create `ui/src/components/chat/ChatMessageList.vue` (Message area)
- [ ] Create `ui/src/components/chat/ChatInput.vue` (Input area)

### Knowledge Base Modals
- [ ] Create `ui/src/components/kb/KbUploadModal.vue` (Missing in implementation)
- [ ] Create `ui/src/components/kb/KbSettingsModal.vue` (Missing in implementation)

## 3. Refactor Views
### ChatView.vue
- [ ] Update `ui/src/views/ChatView.vue` to import and use:
    - `ChatSessionList`
    - `ChatMessageList`
    - `ChatInput`
- [ ] Remove inline implementation of these features from `ChatView.vue`.

## 4. Verification
- [ ] Ensure all new files exist.
- [ ] Ensure `ModelView.vue` is removed.
- [ ] Verify `ChatView.vue` builds/runs (basic check).

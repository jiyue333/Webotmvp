# docparser/

## 概述

文档解析与分块模块。将用户上传的各种格式文件转换为可检索的文本块（Chunk）。

**来源**：对齐 WeKnora `docreader/` 微服务，但在 Webotmvp 中作为单体模块集成（非独立 gRPC 服务）。

## 数据流

```
用户上传文件
    ↓
parser_factory.get_parser(file_name)   # 根据扩展名选择解析器
    ↓
XxxParser.parse_into_text(bytes)       # 格式解析 → Markdown 文本
    ↓
OCREngine（可选）                       # 图片/扫描件 → 文字
    ↓
TextSplitter.split_text(text)          # 文本分块（chunk_size + overlap）
    ↓
[Chunk, Chunk, ...]                    # 输出 → 存入 chunks 表 → 向量化
```

## 目录结构

```
docparser/
├── __init__.py           ← 模块入口
├── document.py           ← 数据模型（Document / Chunk）
├── README.md
├── parsers/              ← 各格式解析器
│   ├── base_parser.py    ← 解析器抽象基类
│   ├── parser_factory.py ← 工厂函数（文件类型 → 解析器）
│   ├── pdf_parser.py
│   ├── docx_parser.py
│   ├── markdown_parser.py
│   ├── text_parser.py
│   ├── csv_parser.py
│   ├── excel_parser.py
│   ├── web_parser.py     ← URL 网页抓取
│   └── image_parser.py   ← 纯图片 OCR
├── ocr/                  ← OCR 引擎
│   ├── base.py           ← OCR 后端抽象基类
│   ├── engine.py         ← OCR 工厂（单例管理）
│   ├── paddle_backend.py ← PaddleOCR 实现
│   └── vlm_backend.py    ← VLM（视觉语言模型）实现
└── splitter/             ← 文本分块
    ├── text_splitter.py  ← 分块器（chunk_size / overlap / 保护模式）
    └── header_hook.py    ← 标题层级追踪（为 chunk 保留章节上下文）
```

## 与 WeKnora docreader 的差异

| 维度     | WeKnora docreader  | Webotmvp docparser        |
| -------- | ------------------ | ------------------------- |
| 部署方式 | 独立 gRPC 微服务   | 单体模块                  |
| 通信协议 | gRPC（proto 定义） | 直接函数调用              |
| 存储     | 自带 storage.py    | 使用 app.infra 的 storage |
| 配置     | 独立 config.py     | 使用 app.common.config    |
| OCR 支持 | PaddleOCR + VLM    | 同（M5 实现）             |

## TODO

- [docparser][M5] 优先实现 PDF、DOCX、Markdown、Text 四种格式
- [docparser][M5] 实现 TextSplitter 的完整分块算法
- [docparser][M5] 对接 OCR 引擎（PaddleOCR 优先）
- [docparser][M6] 补充 CSV、Excel、Web、Image 解析器

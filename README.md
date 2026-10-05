# ai-agent-journey

从 Python 基础到大模型应用开发的六个月学习历程 —— 每周一个主题，产出一份可运行的代码。

## 关于这个仓库

这是一条**项目驱动**的学习路线，不是教程笔记的搬运。目标岗位：**AI 应用开发 / LLM 应用开发 实习**。

每个目录（`W1` ~ `W8`）对应一周的学习内容，里面是该周实际写出的代码。

## 学习进度

### 阶段一：Python 基础 → 大模型 API → 界面应用 ✅ 已完成（v1.0.0）

| 周 | 主题 | 产物 |
|----|------|------|
| W1 | Python 基础语法 | 猜数字、密码校验、成绩判断等 5 个练习脚本 |
| W2 | 列表 / 字典 / 文件读写 | 通讯录 CLI、文本分析器等 5 个练习脚本 |
| W3 | 函数 / 模块 / 包 | 通讯录（函数版 + 多文件包结构） |
| W4 | 面向对象编程 | 图书管理系统、学生管理系统 |
| W5 | 继承 / 多态 / 异常处理 | 图书管理系统（终版）、员工系统 |
| W6 | 调用大模型 API | AI 翻译助手 CLI（DeepSeek API） |
| W7 | Streamlit Web 界面 | **AI 伴侣 Web 应用** |
| W8 | 阶段收官项目 | AI 伴侣 Web 应用打磨与发布 |

### 阶段二：RAG / Agent 应用开发 🚧 进行中

Prompt 工程 → 向量检索 → RAG 知识库 → Function Calling → Agent → 部署。

## 项目导航

| 项目 | 目录 | 技术点 | 说明 |
|------|------|--------|------|
| **AI 伴侣 Web 应用** ⭐ | [`W7/`](W7/) | Streamlit · OpenAI SDK · 会话持久化 | 流式输出 + 人格定制 + 历史会话管理，详见 [W7/README.md](W7/README.md) |
| AI 翻译助手 CLI | [`W6/`](W6/) | OpenAI SDK · python-dotenv | 中英互译，支持语气切换，API Key 走 `.env` |
| 图书管理系统 | [`W5/`](W5/) | OOP · 继承 · 异常处理 | 面向对象综合练习终版 |
| 学生管理系统 | [`W4/`](W4/) | OOP · 文件持久化 | 增删改查 + JSON 存储 |
| 通讯录 | [`W3/`](W3/) | 函数 · 模块 · 包 | 从单文件重构为多文件包结构 |

## 技术栈

- **语言**：Python
- **大模型**：DeepSeek API（OpenAI 兼容接口）
- **界面**：Streamlit
- **配置管理**：python-dotenv（API Key 存于 `.env`，不入库）
- **版本控制**：Git / GitHub

## 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置 API Key：复制 .env.example 为 .env，填入自己的 Key
#    DEEPSEEK_API_KEY=sk-xxxxxxxx

# 3. 运行 AI 伴侣 Web 应用
streamlit run W7/chat_ui.py
```

## 说明

- `.env` 存放 API Key，已被 `.gitignore` 忽略，不会上传
- `sessions/` 存放本地聊天记录，同样不会上传
# AI 伴侣 Web 应用

基于 Streamlit + DeepSeek 大模型的 AI 伴侣聊天应用，支持流式输出、会话持久化与人格定制。

## 功能

- **流式输出**：AI 回复逐字显示，接近真实聊天体验
- **会话持久化**：聊天记录以 JSON 保存到本地，重启应用不丢失
- **会话管理**：侧边栏列出历史会话（按时间倒序），支持一键加载与删除
- **人格定制**：可自定义伴侣昵称与性格，性格描述直接注入 system prompt
- **新建会话**：自动保存当前会话并开启新对话

## 技术栈

| 技术 | 用途 |
|------|------|
| Python | 主语言 |
| Streamlit | Web 界面 |
| OpenAI SDK | 调用 DeepSeek API（OpenAI 兼容接口） |
| python-dotenv | 从 `.env` 读取 API Key |
| JSON | 会话数据的持久化 |

## 运行步骤

1. 安装依赖

   ```bash
   pip install -r requirements.txt
   ```

2. 配置 API Key：复制根目录的 `.env.example` 为 `.env`，填入你的 DeepSeek Key

   ```
   DEEPSEEK_API_KEY=sk-xxxxxxxx
   ```

3. 启动应用

   ```bash
   streamlit run W7/chat_ui.py
   ```

## 项目结构

```
W7/
├── chat_ui.py          # AI 伴侣主程序
└── streamlit_hello.py  # Streamlit 入门练习
```

## 说明

- 会话文件保存在 `sessions/`，该目录已加入 `.gitignore`，不会上传到仓库
- 默认模型：`deepseek-v4-pro`
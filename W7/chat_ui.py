import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from datetime import datetime
import json

load_dotenv()

# 创建OpenAI客户端
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

# 设置页面配置
st.set_page_config(
    page_title="我的AI助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)
st.title("我的AI助手")
st.subheader("一个基于DeepSeek的AI聊天应用")

# 保存会话函数 
# 格式为 JSON 文件，文件名为当前会话的时间戳
def save_session():
    if st.session_state.current_session:
        # 构建新的会话对象
        session_data = {
            "nick": st.session_state.nick,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
                
        # 创建sessions目录
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
    
        # 保存会话到文件 
        # json操作：
        # dump() 方法将 Python 对象转换为 JSON 格式并写入文件,
        # load() 方法从文件中读取 JSON 数据并转换为 Python 对象
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f: 
            json.dump(session_data, f, ensure_ascii=False, indent=2)  

# 加载所有会话列表name信息
def load_sessions():
    sessions_list = []
    if os.path.exists("sessions") :
        file_sessions = os.listdir("sessions")
        for file_name in file_sessions:
            if file_name.endswith(".json"):
                sessions_list.append(file_name[:-5])
    sessions_list.sort(reverse=True)  # 按时间倒序排列
    return sessions_list

# 加载指定会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json") :
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as r: 
                session_data = json.load(r)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick = session_data["nick"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception:
        st.error("加载会话失败")

# 删除指定会话信息
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json") :
            os.remove(f"sessions/{session_name}.json")
            if st.session_state.current_session == session_name:
                st.session_state.messages = []
                st.session_state.current_session = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    except Exception:
        st.error("删除会话失败")

# 提示用户输入提示词
prompt = st.chat_input("请输入聊天内容...")

# 系统输入的提示词 
# %s:占位符，后续会用昵称和性格来替换
system_prompt = """
    你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
    规则：
        每次只回1条消息
        禁止任何场景或状态描述性文字
        匹配用户的语言
        回复简短，像微信聊天一样
        有需要的话可以用❤️ 🌸 等emoji表情
        用符合伴侣性格的方式对话
        回复的内容，要充分体现伴侣的性格特征
    伴侣性格：
        %s
    你必须严格遵守上述规则来回复用户。
"""

# 初始化会话状态
if 'messages' not in st.session_state:
    st.session_state.messages = []
# 昵称    
if 'nick' not in st.session_state:
    st.session_state.nick = "小甜甜" #默认
# 性格    
if 'nature' not in st.session_state:
    st.session_state.nature = "活泼开朗的东北姑娘" #默认
# 会话名字(时间命名) strftime():将时间对象格式化为字符串
if 'current_session' not in st.session_state:
    st.session_state.current_session = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
st.text(st.session_state.current_session)
# 显示聊天记录
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 设置侧边栏
with st.sidebar: 
    st.logo("🤖")
    st.header("AI控制面板")

    # 新建会话 
    # stretch:按钮宽度占满侧边栏
    if st.button("新建会话",width="stretch",icon="📝"):
        # 保存当前会话信息
        save_session()

        # 新建新会话 
        # rerun:重新运行应用程序，刷新页面
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            save_session()
            st.rerun()

    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            if st.button(session,width="stretch",icon="📄",key=f"load_{session}",type="primary" if st.session_state.current_session == session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("",width="stretch",icon="❌",key=f"delete_{session}"):
                delete_session(session)
                st.rerun()  
                
    st.divider()  # 分割线

    # 设置昵称和性格 placeholder:输入框提示文字，value:默认值
    nick = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick) 
    if nick: 
        st.session_state.nick = nick
    nature = st.text_area("性格", placeholder="请输入性格描述", value=st.session_state.nature) 
    if nature: 
        st.session_state.nature = nature

# 创建一个聊天会话
if prompt:
    st.chat_message("user").write(prompt)
    # 保存用户输入的提示词到会话状态
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick, st.session_state.nature)},
            *st.session_state.messages #解包获取会话状态中的所有消息
            ],
        stream=True,
    ) 

    # 显示助手的回复(非流式输出)
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # 显示助手的回复(流式输出) 
    # empty():创建一个空的占位符，后续可以用来显示助手的回复
    response_messages = st.empty()
    full_messages = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_messages += content
            response_messages.chat_message("assistant").write(full_messages)

    # 保存助手的回复到会话状态
    st.session_state.messages.append({"role": "assistant", "content": full_messages})

    save_session()  # 保存会话到文件

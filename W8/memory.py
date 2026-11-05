from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from rich import print as rprint
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model(
    model="deepseek-flash",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

agent = create_agent(
    model=model,
    checkpointer=InMemorySaver(),
)

config1 = {"configurable":{"thread_id":"thread_1"}} 
config2 = {"configurable":{"thread_id":"thread_2"}} 
# 第一次调用，告知AI我的信息
agent.invoke(
    {"messages": [HumanMessage(content="你好我是MIIKII")]},
    config1 # 调用时添加thread_id，区分不同会话
)

response =agent.invoke(
    {"messages": [HumanMessage(content="我是谁？")]},
    config2
)    
rprint(response["messages"][-1].content)

print("--------------------------------------------------")

final_response = agent.invoke(
    {"messages": [HumanMessage(content="我是谁？")]},
    config1 # 调用时添加thread_id，区分不同会话
)
rprint(final_response["messages"][-1].content)
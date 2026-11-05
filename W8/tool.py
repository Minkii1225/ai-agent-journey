import os
from dotenv import load_dotenv
from rich import print as rprint
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_tavily import TavilySearch

# 获取环境变量
load_dotenv()

# 模型初始化
model=init_chat_model(model = "deepseek-flash")

# response = model.stream("你好你是谁？")
# for chunk in response:
#     if chunk.content:
#         print(chunk.content, end="",flush=True)

# agent=create_agent(model=model)
# response = agent.invoke({
#     "messages": [{"role": "user", "content": "月亮的首都是哪里？"}]
# })
# print(response)
# for token, metadata in agent.stream(
#     {"messages": [{"role": "user", "content": "月亮的首都是哪里？"}]},
#     stream_mode="messages"
# ):
#     if token.content:  # Check if there's actual content
#         print(token.content, end="", flush=True)  # Print token

# 自定义工具
# @tool
# def getweather(city: str) -> str:
#     """根据城市名称获取天气信息"""
#     return f"{city}的天气是晴天，温度25°C。"
# agent=create_agent(model=model, tools=[getweather])
# agent_response = agent.invoke({
#     "messages": [{"role": "user", "content": "请告诉我北京的天气情况。"}]
# })
# rprint(agent_response)

# 预定义工具
tool = TavilySearch(
    max_results=5,
    topic="general"
)

# rprint(tool.invoke("杭州今天天气如何？"))

agent=create_agent(
    model=model,
    tools=[tool],
    system_prompt="你是一个ai助手，尽量精简回答用户问题"
)

rprint(agent.invoke({
    "messages":[{"role": "user", "content": "杭州今天天气如何？"}]
}))
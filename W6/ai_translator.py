# 项目日：写一个"AI 翻译助手" CLI	输入中文→英文，输入英文→中文，支持语气切换
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
    )
tone = "正式"
print("直接输入文字翻译 | 1=正式 2=轻松 | 输入 退出 结束") 
while True:
    text = input("你> ")
    if text == "退出":
        break
    elif text == "1":
        tone = "正式"
        print("已切换：正式")
    elif text == "2":
        tone = "轻松"
        print("已切换：轻松")
    else:
        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=[
                {"role": "system", "content": f"你是翻译助手。输入中文就译成英文，输入英文就译成中文。语气：{tone}。只输出译文。"},
                {"role": "user", "content": text},
            ],
            stream=False,
            temperature=0.2,
        )
        print("AI>", response.choices[0].message.content) 



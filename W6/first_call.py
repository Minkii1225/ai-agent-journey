# W6 周五：API Key 安全管理重构，Key 从 .env 读取
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

while True:
    tone = input("请选择语气（1. 正式 2. 口语 3. 幽默）: ")
    
    client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "一句话解释向量数据库"},
    ],
    stream=False
)

print(response.choices[0].message.content)

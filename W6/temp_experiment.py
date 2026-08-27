# 实验观察（2026-08-27，问题：给咖啡店起名，deepseek-v4-pro）
# 1. temp=0 连跑5次 → 4个不同答案：半刻咖啡×2、慢隅咖啡、半日闲、豆留
# 2. 思考链每次不同：reasoning_tokens 在 149~493 波动，无一次重复
# 3. temp=1 输出"豆留"恰好也出现在 temp=0 的第4次 → 答案与温度无稳定映射
# 4. temp=0 第1、5次碰巧相同 → 低温度有收敛倾向，但不保证复现
# 结论：temperature 影响输出"方向"，但工程上不能依赖 temp=0 实现可复现
#       思考型模型（reasoning_content）的不确定性主要来自推理链分岔
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

def ask(temp):
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "给一个咖啡店起名字，只说一个"},
        ],
        temperature=temp,
        stream=False
    )
    return response.choices[0].message.content

print(f"temperature=0 → {ask(0)}")
print(f"temperature=1 → {ask(1)}")
print(f"temperature=0 再跑一次 → {ask(0)}")   # 验证确定性
# 写一个"猜数字游戏"：随机生成 1-100，循环猜，提示大小
import random
num = random.randint(1,100)
while True:
    a = int(input("请输入一个1-100的整数:"))
    if a>num :
        print("太大了")
    elif a==num:
        print("猜对了")
        break
    if a<num :
        print("太小了")
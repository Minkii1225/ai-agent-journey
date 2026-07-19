# 项目日：把前 4 天的程序整合成一个"个人工具箱"菜单程序 | 用 if-else 做菜单选择，调用前几天的功能
import random  # 猜数字需要

while True:
    # 1. 打印菜单
    print("\n" + "="*30)
    print("       【个人工具箱】")
    print("="*30)
    print("1. 成绩等级判断")
    print("2. 猜数字游戏")
    print("3. 密码强度检查器")
    print("0. 退出程序")
    print("-"*30)
    choice = input("请选择功能（输入数字）：")

    if choice == "1":
        # 写一个"成绩等级判断"：输入分数，输出 A/B/C/D/不及格
        score = float(input("请输入成绩："))
        if score >= 90:
            print('A')
        elif score >= 80:
            print('B')
        elif score >= 70:
            print('C')
        elif score >= 60:
            print('D')
        else:
            print('不及格')
        input("按 Enter 键返回菜单...")  # 加这一行，防止屏幕闪退
    
    if choice =="2":
        # 写一个"猜数字游戏"：随机生成 1-100，循环猜，提示大小
        num = random.randint(1,100)
        for a in range(1,101):
            a = int(input("请输入一个1-100的整数"))
            if a>num :
                print("太大了")
            elif a==num:
                print("猜对了")
                break
            if a<num :
                print("太小了")
            input("按 Enter 键返回菜单...")  # 加这一行，防止屏幕闪退

    if choice == "3"        
     # 写一个"简易密码强度检查器"：检查长度/数字/特殊字符
        SPECIALS = "!@#$%^&*"
        password = input("请输入密码")
        has_digit = False
        has_special = False
        for p in password :
            if(p.isdigit()):
                has_digit = True
            if(p in SPECIALS):
                has_special = True
            if(len(password)<6):
                print("弱")
            elif(has_digit & has_special):
                print("强")
            elif(has_digit | has_special):
                print("中")
            else:
                print("弱")

    elif choice == '0':
        print("\n👋 感谢使用工具箱，再见！")
        break  # 这个 break 跳出外层菜单循环，程序结束
        
    else:
        print("❌ 无效输入，请输入 0-3 之间的数字。")

    
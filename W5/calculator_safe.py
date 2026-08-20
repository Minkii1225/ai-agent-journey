# 给计算器加异常处理（除零、非数字输入)
class Calculator:
    def add(self, a, b):
        try:
            return float(a) + float(b)
        except Exception as e:
            print(f"Error: {e}")

    def subtract(self, a, b):
        try:
            return float(a) - float(b)
        except Exception as e:
            print(f"Error: {e}")

    def multiply(self, a, b):
        try:
            return float(a) * float(b)
        except Exception as e:
            print(f"Error: {e}")

    def divide(self, a, b):
        try:
            return float(a) / float(b)
        except Exception as e:
            print(f"Error: {e}")
menu = """
欢迎使用计算器！
请选择操作：
1. 加法
2. 减法
3. 乘法
4. 除法
5. 退出
"""
choice = 0
calc = Calculator()
while True:
    print(menu)
    choice = input("请输入操作编号（1-5）：")
    if choice == '5':
        print("退出计算器。")
        break
    a = input("请输入第一个数字：")
    b = input("请输入第二个数字：")
    if choice == '1':
        result = calc.add(a, b)
        if result is not None:
            print(f"结果: {result}")
    elif choice == '2':
        result = calc.subtract(a, b)
        if result is not None:
            print(f"结果: {result}")
    elif choice == '3':
        result = calc.multiply(a, b)
        if result is not None:
            print(f"结果: {result}")
    elif choice == '4':
        result = calc.divide(a, b)
        if result is not None:
            print(f"结果: {result}")
    else:
        print("无效的操作编号，请重新输入。")
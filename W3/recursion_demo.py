# 用递归实现"阶乘"
# 阶乘
def jc(n):
    if n == 1:
        return 1
    else:
        return n * jc(n - 1)

num = int(input("请输入一个整数："))
print(f"{num}的阶乘是：{jc(num)}")
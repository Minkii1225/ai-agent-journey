#灵活的计算器：用 lambda 定义四则运算，支持多参数运算
#用 lambda 定义四则运算
# 存储四则运算的 lambda
ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,   # 除零在外面判断
}

# 计算函数（支持任意多个数字）
def calc(operator, *args):
    if operator not in ops:
        print("不支持的运算符")
        return None
    if not args:
        print("没有数字")
        return None
    if len(args) < 2:
        print("至少需要两个数字")
        return None
    func = ops[operator]
    result = args[0]
    for num in args[1:]:
        if operator == '/' and num == 0:
            print("除数不能为 0")
            return None
        result = func(result, num)
    return result

# 直接调用示例（运行程序就直接看到结果）
print(calc('+', 1, 2, 3, 4))      # 10
print(calc('-', 100, 10, 5))      # 85
print(calc('*', 2, 3, 4))         # 24
print(calc('/', 100, 2, 5))       # 10.0
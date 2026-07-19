# 写一个"简易密码强度检查器"：检查长度/数字/特殊字符
pwd = input("请输入密码")
if len(pwd) < 6:
    strength = "弱（长度不足）"
elif pwd.isdigit() or pwd.isalpha():
    strength = "中（只有数字或字母）"
else:
    strength = "强（包含数字和特殊字符）"
    print(f"密码强度：{strength}")

    
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

    
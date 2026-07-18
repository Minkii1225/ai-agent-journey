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
# 写一个"班级成绩管理"：用列表存学生成绩，实现增删改查
grades_list = []
students_num = int((input("请输入有多少个学生：")))
#增加
for i in range(students_num):
    grade = int(input("请输入学生成绩："))
    grades_list.append(grade)
print(grades_list)
#删除
num = int(input("请输入要删除的学生成绩的序列："))
if num <= len(grades_list):
    grades_list.pop(num-1)
else:
    print("输入的序列不存在")
print(grades_list)
#修改
num = int(input("请输入要修改的学生成绩的序列："))
if num <= len(grades_list):
    new_grade = int(input("请输入新的成绩："))
    grades_list[num-1] = new_grade
    print("修改成功！")
else:
    print("输入的序列不存在")
print(grades_list)
#查询
num = int(input("请输入要查询的学生成绩的序列："))  
if num <= len(grades_list):
    print(f"第{num}个学生的成绩是：{grades_list[num-1]}")
else:
    print("输入的序列不存在")
# 写一个"班级成绩管理"：把成绩管理升级成字典版（学号→成绩），支持按学号查询，支持菜单
score_dict = {}
menu = """
*******菜单*******
  1. 添加学生
  2. 删除学生
  3. 修改学生成绩
  4. 查询学生成绩
  5. 退出
*****************
"""
while True:
    print(menu)
    choice = input("请输入操作序号：")
    match choice :
        case "1":#添加学生
            student_id = input("请输入学生学号：")
            student_name = input("请输入学生姓名：")
            chinese_score = float(input("请输入学生语文成绩："))
            math_score = float(input("请输入学生数学成绩："))
            english_score = float(input("请输入学生英语成绩："))

            if student_id in score_dict:
                print(f"学号 {student_id} 的学生已存在，无法添加。")
            else:
                score_dict[student_id] = {
                    "姓名": student_name,
                    "语文": chinese_score,
                    "数学": math_score,
                    "英语": english_score
                }
            print(f"学生 {student_name} 的成绩已添加。")
        case "2":#删除学生
            student_id = input("请输入要删除的学生学号：")
            if student_id not in score_dict:
                print(f"学号 {student_id} 的学生不存在，无法删除。")
            else:
                del score_dict[student_id]
                print(f"学号 {student_id} 的学生已删除。")        
        case "3":#修改学生成绩
            student_id = input("请输入要修改成绩的学生学号：")
            if student_id not in score_dict:
                print(f"学号 {student_id} 的学生不存在，无法修改。")
            else:
                student_name = score_dict[student_id]["姓名"]
                chinese_score = float(input("请输入学生语文成绩："))
                math_score = float(input("请输入学生数学成绩："))
                english_score = float(input("请输入学生英语成绩："))
                score_dict[student_id] = {
                    "姓名": student_name,
                    "语文": chinese_score,
                    "数学": math_score,
                    "英语": english_score
                }
                print(f"学生 {student_name} 的成绩已修改。")
        case "4":#查询学生成绩
            student_id = input("请输入要查询成绩的学生学号：")
            if student_id not in score_dict:
                print(f"学号 {student_id} 的学生不存在，无法查询。")
            else:
                student_info = score_dict[student_id]
                print(f"学号: {student_id}, 姓名: {student_info['姓名']}, 语文: {student_info['语文']}, 数学: {student_info['数学']}, 英语: {student_info['英语']}")
        case "5":#退出
            print("退出程序。")
            break
        case _:
            print("无效的操作序号，请重新输入。")

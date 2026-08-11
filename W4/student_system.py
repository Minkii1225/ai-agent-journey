# 一个 Student 类，至少包含：
# 属性：姓名、学号、成绩列表
# 方法：添加成绩、算平均分、判断是否及格
# 一个教务系统类（比如 StudentSystem），用来管理多个学生：
# 添加学生
# 查询学生信息（输入学号或姓名，打印成绩和平均分）

class Student:
    def __init__(self, name, student_id, Chinese, Math, English):
        self.name = name
        self.id = student_id
        self.Chinese = Chinese
        self.Math = Math
        self.English = English
    def __str__(self):
        return f"姓名: {self.name}|学号: {self.id}|语文成绩: {self.Chinese}|数学成绩: {self.Math}|英语成绩: {self.English}"
    def add_score(self, name, student_id, Chinese=None, Math=None, English=None):
        if name != self.name or student_id != self.id:
            print("姓名或学号不匹配，无法添加成绩")
            return
        if Chinese is not None:
            self.Chinese = Chinese
        if Math is not None:
            self.Math = Math
        if English is not None:
            self.English = English
    def average_score(self):
        return (self.Chinese + self.Math + self.English) / 3
    def is_passed(self):
        if self.Chinese >=60:
            print("语文及格")
        else:
            print("语文不及格")
        if self.Math >=60:
            print("数学及格")
        else:
            print("数学不及格")
        if self.English >=60:
            print("英语及格")
        else:
            print("英语不及格")
class StudentSystem:
    systemversion = "1.0"
    systemname = "学生管理系统"
    systemauthor = "MiiKi"
    def __init__ (self):
        self.students_list = []
    # 添加学生
    def add_student(self):
        name = input("请输入学生姓名：")
        student_id = input("请输入学生学号：")
        Chinese = int(input("请输入语文成绩："))
        Math = int(input("请输入数学成绩："))
        English = int(input("请输入英语成绩："))    
        for student in self.students_list:
            if name == student.name and student_id == student.id:
                print("该学生已存在，无法添加")
                return
        if Chinese < 0 or Chinese > 100 or Math < 0 or Math > 100 or English < 0 or English > 100:
            print("成绩输入有误，请重新输入范围是1-100的整数")
        else:
            student = Student(name, student_id, Chinese, Math, English)
            self.students_list.append(student)
            print("学生添加成功")
    # 删除学生
    def delete_student(self):
        name = input("请输入学生姓名：")
        student_id = input("请输入学生学号：")
        for student in self.students_list:
            if student.name == name and student.id == student_id:
                self.students_list.remove(student)
                print("学生删除成功")
                return
        print("未找到该学生，无法删除")
    # 查询学生信息
    def query_student(self):
        name = input("请输入学生姓名（可选）：")
        student_id = input("请输入学生学号（可选）：")
        for student in self.students_list:
            if name is not None and student.name == name:
                print(student)
                print(f"平均分: {student.average_score()}")
                student.is_passed()
                return
            elif student_id is not None and student.id == student_id:
                print(student)
                print(f"平均分: {student.average_score()}")
                student.is_passed()
                return
        print("未找到该学生信息")
    # 修改学生信息
    def modify_student(self):
        name = input("请输入学生姓名：")
        student_id = input("请输入学生学号：")
        Chinese = input("请输入语文成绩（可选）：")
        Math = input("请输入数学成绩（可选）：")
        English = input("请输入英语成绩（可选）：")
        if Chinese:
            Chinese = int(Chinese)
        else:
            Chinese = None
        if Math:
            Math = int(Math)
        else:
            Math = None
        if English:
            English = int(English)
        else:
            English = None
        for student in self.students_list:
            if student.name == name and student.id == student_id:
                student.add_score(name, student_id, Chinese, Math, English)
                print("学生信息修改成功")
                return
        print("未找到该学生信息，无法修改")
    # 查询所有学生信息
    def query_all_students(self):
        for student in self.students_list:
            print(student)
            print(f"平均分: {student.average_score()}")
            student.is_passed()
    def run(self):
        print(f"欢迎使用{StudentSystem.systemname}，版本号：{StudentSystem.systemversion}，作者：{StudentSystem.systemauthor}")
        menu = """
        请选择操作：
        1. 添加学生
        2. 删除学生
        3. 查询学生信息
        4. 修改学生信息
        5. 查询所有学生信息
        6. 退出系统
        """
        while True:
            print(menu)
            choice = input("请输入操作编号：")
            try:
                match choice:
                    case "1":
                        self.add_student()
                    case "2":
                        self.delete_student()
                    case "3":
                        self.query_student()
                    case "4":
                        self.modify_student()
                    case "5":
                        self.query_all_students()
                    case "6":
                        print("退出系统")
                        break
                    case _:
                        print("输入有误，请重新输入")
            except Exception as e:
                print(f"发生错误：{e}")

if __name__ == "__main__":
    studentsystem = StudentSystem()
    studentsystem.run()
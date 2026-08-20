# Employee 父类 → Manager/Developer/Designer 子类，各自计算薪资
# Employee 定义 calculate_salary() 方法，默认返回 base（基本工资）
# 三个子类各自重写 calculate_salary()，加入各自的计算逻辑
# 每个子类的 __init__ 先调 super().__init__(name, emp_id, base) 初始化公共属性，再加自己的特有属性
# 可以写一个 make_payment(employee) 函数，传入不同子类对象，调用 calculate_salary() 返回不同结果——跟之前 make_sound() 一模一样的多态模式
# Manager	基本工资 + 管理津贴 + 团队绩效	base + 3000 + team_size * 500	team_size（团队人数）
# Developer	基本工资 + 项目奖金 + 加班费	base + project_bonus + overtime_hours * 50	project_bonus、overtime_hours
# Designer	基本工资 + 作品数量提成	base + design_count * 200	design_count（完成作品数）
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = float(base_salary)

    def __str__(self):
        return f"员工姓名: {self.name}, 基础工资: {self.base_salary}"

    def calculate_salary(self):
        return self.base_salary
    
class Manager(Employee):
    def __init__(self, name, base_salary, team_size):
        super().__init__(name, base_salary)
        self.team_size = int(team_size)

    def calculate_salary(self):
        return self.base_salary + 3000 + self.team_size * 500
    
class Developer(Employee):
    def __init__(self, name, base_salary, project_bonus, overtime_hours):
        
            super().__init__(name, base_salary)
            self.project_bonus = float(project_bonus)
            self.overtime_hours = int(overtime_hours)

    def calculate_salary(self):
        return self.base_salary + self.project_bonus + self.overtime_hours * 50
    
class Designer(Employee):
    def __init__(self, name, base_salary, design_count):
        
            super().__init__(name, base_salary)
            self.design_count = int(design_count)

    def calculate_salary(self):
        return self.base_salary + self.design_count * 200

def make_payment(employee):
    salary = employee.calculate_salary()
    print(f"支付给 {employee.name} 的薪资为: {salary}")

while True:
    print("请选择员工类型：")
    print("1. Manager")
    print("2. Developer")
    print("3. Designer")
    print("4. 退出")

    choice = input("请输入选项 (1-4): ")
    if choice == '4':
        print("退出程序。")
        break
    elif choice in ['1', '2', '3']:
        try:
            name = input("请输入员工姓名: ")
            base_salary = input("请输入基础工资: ")
            if choice == '1':
                team_size = input("请输入团队人数: ")
                employee = Manager(name, base_salary, team_size)
            elif choice == '2':
                project_bonus = input("请输入项目奖金: ")
                overtime_hours = input("请输入加班小时数: ")
                employee = Developer(name, base_salary, project_bonus, overtime_hours)
            elif choice == '3':
                design_count = input("请输入完成作品数: ")
                employee = Designer(name, base_salary, design_count)
            make_payment(employee)
        except Exception as e:
            print(f"输入错误: {e}")
    else:
        print("无效选项，请重新输入。")


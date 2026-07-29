# # 把通讯录重构成函数版（每个操作一个函数）
# # 写一个"简易通讯录"（命令行 CRUD）用字典存储、支持添加/删除/查询
# contacts = {}
# menu = '''
# *******菜单*******
#   1. 添加联系人
#   2. 删除联系人
#   3. 查询联系人
#   4. 查询所有联系人
#   5. 退出
# *****************
# '''

# while True:
#     print(menu)
#     choice = input("请输入操作序号：")
#     match choice:
#         case "1":  # 添加联系人
#             name = input("请输入联系人姓名：")
#             phone = input("请输入联系人电话：")
#             if name in contacts:
#                 print(f"联系人 {name} 已存在，无法添加。")
#             else:
#                 contacts[name] = phone
#                 print(f"联系人 {name} 已添加。")
#         case "2":  # 删除联系人
#             name = input("请输入联系人姓名：")
#             if name not in contacts:
#                 print(f"联系人 {name} 不存在，无法删除。")
#             else:
#                 del contacts[name]
#                 print(f"联系人 {name} 已删除。")
#         case "3":  # 查询联系人
#             name = input("请输入联系人姓名：")
#             if name in contacts:
#                 print(f"联系人 {name} 的电话是 {contacts[name]}。")
#             else:
#                 print(f"联系人 {name} 不存在。")
#         case "4":  # 查询所有联系人
#             print("所有联系人：",contacts.items())
#         case "5":  # 退出
#             print("退出通讯录程序。")
#             break

def add_contact(name,phone):
    """
    添加联系人
    Args:
        name (_type_): _description_ 姓名
        phone (_type_): _description_ 电话号码
    """
    if name in contacts:
        print(f"联系人 {name} 已存在，无法添加。")
    else:
        contacts[name] = phone
        print(f"联系人 {name} 已添加。")
def delete_contact(name):
    """
    删除联系人
    Args:
        name (_type_): _description_ 姓名
    """
    if name not in contacts:
        print(f"联系人 {name} 不存在，无法删除。")
    else:
        del contacts[name]
        print(f"联系人 {name} 已删除。")
def query_contact(name):
    """
    查询联系人
    Args:
        name (_type_): _description_ 姓名
    """
    if name in contacts:
        print(f"联系人 {name} 的电话是 {contacts[name]}。")
    else:
        print(f"联系人 {name} 不存在。")
def query_all_contacts():
    """
    查询所有联系人
    """
    for name,phone in contacts.items():
        print(f"联系人 {name} 的电话是 {phone}。")
contacts = {}
menu = '''
*******菜单*******
  1. 添加联系人
  2. 删除联系人
  3. 查询联系人
  4. 查询所有联系人
  5. 退出
*****************
'''
print(menu)
while True:
    choice = input("请输入操作序号：")
    match choice:
        case "1":  # 添加联系人
            name: str = input("请输入联系人姓名：")
            phone: str = input("请输入联系人电话：")
            add_contact(name,phone)
        case "2":  # 删除联系人
            name: str = input("请输入联系人姓名：")
            delete_contact(name)
        case "3":  # 查询联系人
            name: str = input("请输入联系人姓名：")
            query_contact(name)
        case "4":  # 查询所有联系人
            query_all_contacts()
        case "5":  # 退出
            print("退出通讯录程序。")
            break
        case _:  # 其他输入
            print("无效的操作序号，请重新输入。")

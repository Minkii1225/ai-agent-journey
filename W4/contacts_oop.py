# 综合练习：用 OOP 重写 W2 的通讯录	定义 Contact 类 + AddressBook 类，用对象管理而非字典
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
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def __str__(self):
        return f"联系人 {self.name} 的电话是 {self.phone}。"
class AddressBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self):
        name = input("请输入联系人姓名：")
        phone = input("请输入联系人电话：")
        for contact in self.contacts:
            if contact.name == name:
                print(f"联系人 {name} 已存在，无法添加。")
                return
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"联系人 {name} 已添加。")
    def delete_contact(self):
        name = input("请输入联系人姓名：")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"联系人 {name} 已删除。")
                return
        print(f"联系人 {name} 不存在，无法删除。")
    def update_contact(self):
        name = input("请输入联系人姓名：")
        for contact in self.contacts:
            if contact.name == name:
                new_phone = input("请输入新的联系人电话：")
                contact.phone = new_phone
                return
        print(f"联系人 {name} 不存在，无法更新。")
    def query_contact(self):
        name = input("请输入联系人姓名：")
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print(f"联系人 {name} 不存在。")
    def query_all_contacts(self):
        if not self.contacts:
            print("通讯录为空。")
            return
        print("所有联系人：")
        for contact in self.contacts:
            print(contact)
menu = '''
    *******菜单*******
    1. 添加联系人
    2. 删除联系人
    3. 修改联系人
    4. 查询联系人
    5. 查询所有联系人
    6. 退出
    *****************
    '''
book = AddressBook()
while True:
    print(menu)
    choice = input("请输入操作序号：")
    match choice:
        case "1":
            book.add_contact()
        case "2":
            book.delete_contact()
        case "3":
            book.update_contact()
        case "4":
            book.query_contact()
        case "5":
            book.query_all_contacts()
        case "6":
            print("退出通讯录程序。")
            break
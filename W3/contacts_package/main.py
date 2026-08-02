import storage
# main.py  （菜单 + 用户输入）
menu = '''
*******菜单*******
  1. 添加联系人
  2. 删除联系人
  3. 查询联系人
  4. 查询所有联系人
  5. 退出
*****************
'''
while True:
    print(menu)
    choice = input("请输入操作序号：")
    match choice:
        case "1":  # 添加联系人
            name: str = input("请输入联系人姓名：")
            phone: str = input("请输入联系人电话：")
            storage.add_contact(name,phone)
        case "2":  # 删除联系人
            name: str = input("请输入联系人姓名：")
            storage.delete_contact(name)
        case "3":  # 查询联系人
            name: str = input("请输入联系人姓名：")
            storage.query_contact(name)
        case "4":  # 查询所有联系人
            storage.query_all_contacts()
        case "5":  # 退出
            print("退出通讯录程序。")
            break
        case _:  # 其他输入
            print("无效的操作序号，请重新输入。")
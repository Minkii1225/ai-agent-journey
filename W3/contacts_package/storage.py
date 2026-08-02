from models import contacts
# storage.py  （增删查函数）
def add_contact(name:str,phone:str):
    """
    添加联系人
    Args:
        name:姓名
        phone:电话号码

    Returns:None

    """
    if name in contacts:
        print(f"联系人 {name} 已存在，无法添加。")
    else:
        contacts[name] = phone
        print(f"联系人 {name} 已添加。")
def delete_contact(name:str):
    """
    删除联系人
    Args:
        name:姓名·

    Returns:None

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
        name:姓名

    Returns:None

    """
    if name in contacts:
        print(f"联系人 {name} 的电话是 {contacts[name]}。")
    else:
        print(f"联系人 {name} 不存在。")
def query_all_contacts():
    """
    查询所有联系人
    """
    if len(contacts) == 0:
        print("通讯录为空。")
        return
    for name, phone in contacts.items():
        print(f"联系人 {name} 的电话是 {phone}。")

    
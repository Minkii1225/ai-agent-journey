from abc import ABC,abstractmethod
class LibraryItem(ABC):  # 父类：所有馆藏的公共部分
    def __init__(self, title, item_id):
        self.title = title          # 书名
        self.item_id = item_id      # 编号
        self.is_borrowed = False    # 是否借出

    def borrow(self):               # 借出
        if self.is_borrowed:
            print(f"《{self.title}》已被借出")
        else:
            self.is_borrowed = True
            print(f"《{self.title}》借出成功")
    def return_item(self):          # 归还
        if not self.is_borrowed:
            print(f"《{self.title}》没有被借出，无法归还")
        else:
            self.is_borrowed = False
            print(f"《{self.title}》归还成功")

    @abstractmethod
    def get_info(self):
        pass             # 抽象方法：子类必须实现
    @property
    def is_available(self):        # 计算属性：未借出为True
        return not self.is_borrowed

class Book(LibraryItem):            # 纸质书
    def __init__(self, title, item_id, author, pages):  # 作者、页数
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def get_info(self):             # 返回"纸质书：书名/作者/页数"
        status = "已借出" if self.is_borrowed else "可借阅"
        return f"【纸质书】{self.title} | 作者：{self.author} | {self.pages}页 | {status}"
    
class Ebook(LibraryItem):           # 电子书
    def __init__(self, title, item_id, file_size):      # 大小，下载次数=0
        super().__init__(title, item_id)
        self.file_size = file_size
        self.download_count = 0

    def borrow(self):               # 重写：电子书无需借出
        print(f"《{self.title}》是电子书，无需借出，可直接下载")

    def download(self):             # 下载次数+1
        self.download_count += 1
        print(f"《{self.title}》下载成功，累计下载{self.download_count}次")

    def get_info(self):             # 返回"电子书：书名/大小/下载次数"
        return f"【电子书】{self.title} | 大小：{self.file_size}MB | 已下载{self.download_count}次"

class Library:                      # 管理所有馆藏
    def __init__(self): 
        self.items = {}

    def find_item(self,item_id):
        return self.items.get(item_id)   # dict.get() 找不到返回 None

    @property
    def available_count(self):
        return len([item for item in self.items.values() if item.is_available])

    def add_item(self, item):       # 添加（编号不重复）
        if self.find_item(item.item_id) is not None:
            print(f"编号 {item.item_id} 已存在，无法添加")
        else:
            self.items[item.item_id] = item 
            print(f"添加成功：{item.get_info()}")

    def remove_item(self, item_id): # 按编号删除
        item = self.find_item(item_id)
        if item is None:
            print("未找到该编号的馆藏")
            return
        del self.items[item_id]          # 删除时要先拿到 item 打印信息
        print(f"已删除：{item.get_info()}")

    def search_item(self, item_id): # 按编号搜索并打印信息
        item = self.find_item(item_id)
        if item is None:
            print("未找到该编号的馆藏")
        else:
            print(item.get_info())
        
    def borrow_item(self, item_id): # 调 item.borrow()，多态
        item = self.find_item(item_id)
        if item is None:
            print("未找到该编号的馆藏")
        else:
            item.borrow()

    def show_all(self):             # 打印所有馆藏
        if not self.items:
            print("馆藏为空")
            return
        for item in self.items.values():
            print(item.get_info())

    def return_item(self, item_id):
        item = self.find_item(item_id)
        if item is None:
            print("未找到该编号的馆藏")
        else:
            item.return_item()

    def download_item(self,item_id):
        item = self.find_item(item_id)
        if item is None:
            print("未找到该编号的馆藏")
        elif isinstance(item, Ebook):
            item.download()
        else:
            print(f"《{item.title}》是纸质书，无法下载")

menu = """
===== 图书管理系统 =====
1. 添加纸质书
2. 添加电子书
3. 删除馆藏
4. 搜索馆藏
5. 借出
6. 归还
7. 下载电子书
8. 显示全部
9. 退出
=======================
"""

library = Library()

while True:
    print(menu)
    print(f"当前馆藏 {len(library.items)} 项，可借阅 {library.available_count} 项")
    choice = input("请输入操作编号：")
    try:
        if choice == "1":
            title = input("书名：")
            item_id = input("编号：")
            author = input("作者：")
            pages = int(input("页数："))
            library.add_item(Book(title, item_id, author, pages))
        elif choice == "2":
            title = input("书名：")
            item_id = input("编号：")
            file_size = float(input("文件大小(MB)："))
            library.add_item(Ebook(title, item_id, file_size))
        elif choice == "3":
            library.remove_item(input("编号："))
        elif choice == "4":
            library.search_item(input("编号："))
        elif choice == "5":
            library.borrow_item(input("编号："))
        elif choice == "6":
            library.return_item(input("编号："))
        elif choice == "7":
            library.download_item(input("编号："))
        elif choice == "8":
            library.show_all()
        elif choice == "9":
            print("退出系统")
            break
        else:
            print("无效的操作编号")
    except ValueError:
        print("输入有误，请输入正确的数字")



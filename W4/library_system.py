# 项目日：写一个"图书管理小系统"	Book 类 + Library 类（添加/删除/搜索/借出/归还）
class Book:
    def __init__(self,name, author, book_id, price):
        self.name = name
        self.author = author
        self.id = book_id
        self.price = price
        self.is_borrowed = False
    def __str__(self):
        return f"书名：{self.name}，作者：{self.author}，编号：{self.id}，价格：{self.price}"
class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []
    def add_book(self): #添加书籍
        name = input("请输入书名：")
        author = input("请输入作者：")
        book_id = input("请输入编号：")
        price = float(input("请输入价格："))
        book = Book(name, author, book_id, price)
        self.books.append(book)
        print(f"已添加图书：{book}")
    def remove_book(self): #删除书籍
        book_id = input("请输入要删除的书籍编号：")
        for book in self.books + self.borrowed_books:
            if book.id == book_id:
                if book in self.books:
                    self.books.remove(book)
                else:
                    self.borrowed_books.remove(book)
                print(f"已删除图书：{book}")
                return
        print("未找到该书籍。")
    def search_book(self): #搜索书籍
        book_id = input("请输入要搜索的书籍编号：")
        for book in self.books + self.borrowed_books:
            if book.id == book_id:
                print(f"找到图书：{book}")
                if book.is_borrowed:
                    print("该书籍已被借出。")
                return
        print("未找到该书籍。")
    def borrow_book(self): #借出书籍
        book_id = input("请输入要借出的书籍编号：")
        for book in self.books + self.borrowed_books:
            if book.id == book_id:
                if book in self.books:
                    self.books.remove(book)
                if book.is_borrowed:
                    print("该书籍已被借出。")
                    return
                self.borrowed_books.append(book)
                book.is_borrowed = True
                print(f"已借出图书：{book}")
                return
        print("未找到该书籍。")
    def return_book(self): #归还书籍
        book_id = input("请输入要归还的书籍编号：")
        for book in self.borrowed_books:
            if book.id == book_id:
                self.borrowed_books.remove(book)
                self.books.append(book)
                book.is_borrowed = False
                print(f"已归还图书：{book}")
                return
        print("未找到该书籍。")
menu = """
欢迎使用图书管理小系统，请选择操作：
1. 添加书籍
2. 删除书籍
3. 搜索书籍
4. 借出书籍
5. 归还书籍
6. 退出系统
"""
library = Library()
while True:
    print(menu)
    choice = input("请输入操作编号：")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.remove_book()
    elif choice == "3":
        library.search_book()
    elif choice == "4":
        library.borrow_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        print("退出系统。")
        break
    else:
        print("无效的操作编号，请重新输入。")
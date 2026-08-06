# 定义一个 Book 类，有三样东西：
# 属性（__init__ 里写）：
# 书名
# 作者
# 价格
# 方法（两个行为）：
# describe()：把这本书的信息格式化打印出来
# # apply_discount()：传入一个折扣比例，把价格改掉

class Book:
    def __init__(self, b_name, b_author, b_price):
        self.name = b_name
        self.author = b_author
        self.price = b_price

    def describe(self):
        print(f"书名：{self.name}，作者：{self.author}，价格：{self.price}")

    def apply_discount(self, discount):
        self.price = self.price * discount
book = Book("Python编程", "张三", 100)
book.describe()
book.apply_discount(0.5)
book.describe()
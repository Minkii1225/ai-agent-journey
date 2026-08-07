# 给 Book 加 str（打印格式化信息）、eq（按书名判断相等）	
# 定义一个 Book 类，有三样东西：
# 属性（__init__ 里写）：
# 书名
# 作者
# 价格
# 方法（两个行为）：
# # apply_discount()：传入一个折扣比例，把价格改掉

class Book:
    def __init__(self, b_name, b_author, b_price):
        self.name = b_name
        self.author = b_author
        self.price = b_price
    def apply_discount(self, discount):
        self.price = self.price * discount

    def __str__(self):
        return f"书名：{self.name}，作者：{self.author}，价格：{self.price}"
    def __eq__(self, other):
        return self.name == other.name
    
book1 = Book("Python编程", "张三", 100)
book2 = Book("Python编程", "李四", 200)
print(book1)
book1.apply_discount(0.5)
print(f"打折后：{book1.price}")
print(book2)
print(book1 == book2)  # True，因为书名相同
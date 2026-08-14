# Animal 父类 → Dog/Cat 子类，各自重写 speak()
class Animal:
    def speak(self):
        print("动物发出叫声")
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")
animal = Animal()
dog = Dog()
cat = Cat()
animal.speak()  # 输出: 动物发出叫声
dog.speak()     # 输出: 汪汪汪
cat.speak()     # 输出: 喵喵喵
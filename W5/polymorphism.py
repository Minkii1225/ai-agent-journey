# 写一个 make_sound() 函数，传入不同动物调用各自 speak()
class Animal:
    def speak(self):
        print("动物发出声音")
class Dog:
    def speak(self):
        print("汪汪汪")
class Cat:
    def speak(self):
        print("喵喵喵")
class Cow:
    def speak(self):
        print("哞哞哞")
# 多继承写法：
# class Run(Animal, Dog, Cat, Cow):
#     def make_sound(self):
#         Animal.speak(self)
#         Dog.speak(self)
#         Cat.speak(self)
#         Cow.speak(self)
# run = Run()
# run.make_sound()
# 多态：
def make_sound(animal):
    animal.speak()
make_sound(Animal())  # 输出: 动物发出声音
make_sound(Dog())  # 输出: 汪汪汪
make_sound(Cat())  # 输出: 喵喵喵
make_sound(Cow())  # 输出: 哞哞哞
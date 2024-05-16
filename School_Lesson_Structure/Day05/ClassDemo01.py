"""
author : Yan Peng Bo
Date: 2023-6-4
content: class_demo_01 project
"""


# 经典类 不由任何内置类派生出来的类
class Washer:
    def Wash(self):
        print("我会洗衣服")


haier = Washer()
print(haier)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)


class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()

cnt = 0
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
    cnt += 1
print(x.counter)
print(cnt)

"""
author : Yan Peng Bo
Date: 2023-6-4
content: extends_class_demo project
"""

"""
class Father(object):
    # object 为顶级类
    def __init__(self):
        self.num = 1

    def print_info(self):
        print(self.num)


class Child(Father):
    pass

child = Child()
child.print_info()

"""

# 单继承
"""
class Master(object):
    def __init__(self):
        self.kong_fu = 'delicious 🥞'

    def make_cook(self):
        print(f'师傅制作{self.kong_fu}')


class Apprentice(Master):
    pass


p1 = Apprentice()
p1.make_cook()
print(p1.kong_fu)
"""

# 多继承

"""
class A:
    def __init__(self):
        self.id = 'a'

    def print_msg(self):
        print('a')


class B:
    def __init__(self, id):
        self.id = id

    def print_msg(self):
        print(self.id)


class C(B, A):

    pass


c = C('a')
c.print_msg()
"""


#    子类调用父类同名的方法和属性

class A(object):
    def __init__(self):
        self.a = 10

    def print_all(self):
        print(f"a的值为{self.a}")


class B(object):
    def __init__(self):
        self.a = 20

    def print_all(self):
        print(f"a的值为{self.a}")


class AB(A, B):

    def __init__(self):
        super().__init__()
        self.a = 30

    def print_all(self):
        # 如果先调用父类的属性和方法，父类属性会覆盖子类属性，故在调用属性前，先调用自己子类初始化方法
        self.__init__()
        print(f"子类自己a的值为{self.a}")

    #  调用父类方法，但是为保证调用到的属性也是父类的属性，必须在调用方法去调用父类的初始化
    def print_A(self):
        A.__init__(self)
        A.print_all(self)

    def print_B(self):
        B.__init__(self)
        B.print_all(self)


ab = AB()
ab.print_all()
ab.print_A()
ab.print_B()

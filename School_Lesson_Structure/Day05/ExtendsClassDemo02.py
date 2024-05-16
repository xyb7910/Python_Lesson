"""
author : Yan Peng Bo
Date: 2023-6-4
content: extends_class_demo_02 project
"""


# 多层继承
class A(object):
    def __init__(self):
        self.num = 10

    def print_info(self):
        print(self.num)


class B(object):
    def __init__(self):
        self.num = 20

    def print_info(self):
        print(self.num)


class AB(A, B):
    def __init__(self):
        super().__init__()
        self.num = 20

    def print_info(self):
        print(self.num)

    def printA(self):
        A.__init__(self)
        A.print_info(self)

    def printB(self):
        B.__init__(self)
        B.print_info(self)


class ABC(AB):
    pass


abc = ABC()
abc.print_info()
abc.printA()
abc.printB()

"""
author : Yan Peng Bo
Date: 2023-6-4
content: super_extends_class_demo project
"""

"""
class A:
    def add(self, x):
        y = x + 1
        print(y)


class B(A):
    def add(self, x):
        super().add(x)


b = B()
b.add(2)
"""


class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        super(FooChild, self).__init__()
        print('Child')

    def bar(self, message):
        super(FooChild, self).bar(message)
        print('Child Bar Function')
        print(self.parent)


if __name__ == '__main__':
    foochild = FooChild()
    foochild.bar('HelloWorld')

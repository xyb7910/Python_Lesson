"""
author : Yan Peng Bo
Date: 2023-6-4
content: class_demo_03 project
"""

# 类的 mutable

"""
共享变量会共同使用，给你一个出乎意料的结果
"""


class Dogs:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dogs('Fido')
e = Dogs('Buddy')
d.add_trick('roller over')
e.add_trick('play dead')

# print(d.tricks)


# 修改为非共享型
class Dogs1:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


d1 = Dogs1('Fido')
e1 = Dogs1('Buddy')
d1.add_trick('roller over')
e1.add_trick('play dead')

print(d1.tricks)

"""
author : Yan Peng Bo
Date: 2023-6-4
content: class_demo_02 project
"""


class PersonMessage:

    #  初始化函数
    def __init__(self):
        self.university = 'pku'
        self.age = 18
        self.name = 'yxc'

    def print_info(self):
        print(f'该学生的姓名为{self.name}')
        print(f'该学生的年龄为{self.age}')
        print(f'该学生所在的大学是{self.university}')


p = PersonMessage()
p.print_info()

""""
p.name = 'ypb'
p.age = 18
"""


class StudentMessage:

    #  初始化函数
    def __init__(self, name, age, university):
        self.university = university
        self.age = age
        self.name = name

    def print_info(self):
        print(f'该学生的姓名为{self.name}')
        print(f'该学生的年龄为{self.age}')
        print(f'该学生所在的大学是{self.university}')


stu = StudentMessage('ypb', 19, 'yau')
stu.print_info()

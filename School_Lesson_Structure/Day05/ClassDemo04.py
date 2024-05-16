"""
author : Yan Peng Bo
Date: 2023-6-4
content: class_demo_04 project
"""


# __str__
class StudentMessage:
    #  初始化函数
    def __init__(self, name, age, university):
        self.university = university
        self.age = age
        self.name = name

    def __str__(self):
        return "姓名:{}--年龄:{}--学校{}".format(self.name, self.age, self.university)


"""
    def __del__(self):
        print("实例对象的名称" % self.name)
        print("python解释器开始回收%s对象了" % self.name)
"""

Stu = StudentMessage('yxc', 18, 'pku')
print(Stu)

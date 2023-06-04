"""
author : Yan Peng Bo
Date: 2023-6-4
content: private_class_demo project
"""


# 定义私有权限属性和方法

"""

"""
class Person(object):
    def __init__(self):
        self.__id = 1000
        self.name = 'yxc'
        self.age = 18

    def print_info(self):
        print(f'姓名为：{self.name},年龄为{self.age}')

    # 获取私有属性
    def get_id(self):
        return self.__id

    # 修改私有属性
    def set_id(self):
        self.__id = 2222

class Student(Person):
    def __init__(self):
        super().__init__()
        self.__id = 1001
        self.name = 'ypb'
        self.age = 19

    def print_info(self):
        self.__init__()
        print(f'id为{self.__id},姓名为：{self.name},年龄为{self.age}')

    # 此方法在类外无法访问
    def __info_print(self):
        print(self.__id)
        print(self.name)
        print(self.age)

    def get_id(self):
        return self.__id

    # 修改私有属性
    def set_id(self):
        self.__id = 2222


# 对象无法访问私有属性和私有方法
Per = Person()
print(Per.get_id())

Stu = Student()
print(Stu.get_id())

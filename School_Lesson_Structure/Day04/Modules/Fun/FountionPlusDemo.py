"""
author : Yan Peng Bo
Date: 2023-5-28
content: fun_plus_demo project
"""

i = 5


def f(arg=i):
    print(arg)


# 存在一个共享变量
def append(a, L=[]):
    L.append(a)
    return L


# 将变量L变为非共享变量
def append_(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# 函数参数的选择
def add_msg(name, age=18, active=70, type_s="S"):
    print(f"这个学生的信息为：姓名：{name}, 年龄:{age}, 活跃度:{active}, 类型为:{type_s}")


# *name形参接受一个元组
# **name形参接受一个字典
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

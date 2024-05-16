"""
author : Yan Peng Bo
Date: 2023-5-28
content: tuple_demo project
"""
# tuple foundation
"""
# tuple pack
t = 12345, 'hello', ['yxc', 123]
print(type(t))

u = t, (1, 2, 3, 4, 5)
print(type(u))

# Tuples are immutable
# t[0] = 54321

v = ([1, 2, 3], [3, 2, 1])
print(v)

# <class 'tuple'>
empty_tuple = ()
# <class 'tuple'>
one_tuple = (3,)
# <class 'int'>
one_array = (3)
print(type(empty_tuple))
print(type(one_tuple))
print(type(one_array))
"""

# tuple pack
"""
a = (1, 2, 3, 4)
b = ('a', 'b', 'c', 'd')
c = a, b
print(type(a))
print(type(b))
print(type(c))
print(c)
"""

# 虽然元组是不可变的，但元组中的列表是可以修改的
"""
a = ('a', 'b', 'c', [1, 2, 3, 4])
a[3][1] = 4
print(a[3][1])
"""











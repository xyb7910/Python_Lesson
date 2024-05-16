"""
author : Yan Peng Bo
Date: 2023-5-28
content: set_demo project
"""

# 集合是由不重复元素组成的无序容器。基本用法包括成员检测、消除重复元素。集合对象支持合集、交集、差集、对称差分等数学运算。

"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(type(basket))

print('orange' in basket)
print('goat' in basket)
"""

# empty set
# 创建空集合只能使用set(), 不能使用{}， 因为{}用来创建一个空的字典

"""
s1 = set()
print(type(s1))
"""

# 不支持索引
# print(s1[0]) # 报异常


# operator
"""
a = set('abracadabra')
b = set('alacazama')
print(a)
print(b)

# -
c = a - b
print(c)

# |
d = a | b
print(d)

# ^
e = a ^ b
print(e)
"""


# function

# 追加元素
"""
s1 = {1, 2, 3, 4}
s1.add(5)
s1.add(6)
s1.add(7)
print(s1)

s1.update('a', 'b', 'c')
print(s1)
"""

# 删除元素

"""
s1 = {'a', 'b', 'c', 'd'}
print(s1)
s1.remove('a')
print(s1)

# remove无法删除不存在的元素，报异常
# s1.remove('e')

s1.discard('b')
print(s1)

# 若删除元素不存在也不会报错
s1.discard('e') 
"""

s1 = {2, 4, 1, 5, 6}
print(s1)
elem = s1.pop()
print(s1)
print(elem)

s2 = {'b', 'd', 'e', 'f', 'a'}
print(s2)
elem_s = s2.pop()
print(s2)
print(elem_s)





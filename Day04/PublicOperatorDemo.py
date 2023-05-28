"""
author : Yan Peng Bo
Date: 2023-5-28
content: public_operator_demo project
"""

# + 合并 支持字符串，列表，元组

"""
# 字符串
str1 = 'abc'
str2 = 'def'
str3 = str1 + str2
print(str3)

# 列表
list1 = [1, 2]
list2 = [3, 4, 5]
list3 = list1 + list2
print(list3)

# 元组
t1 = (1, 2)
t2 = (3, 4, 5)
t3 = t1 + t2
print(t3)

"""

# * 复制 支持字符串，列表，元组

"""
# 字符串
str1 = 'abc'
str3 = str1 * 2
print(str3)

# 列表
list1 = [1, 2]
list3 = list1 * 2
print(list3)

# 元组
t1 = (1, 2)
t3 = t1 * 2
print(t3)
"""


# in 判断存在 支持字符串，列表，元组，字典
# not in 判断不存在 支持字符串，列表，元组，字典
"""
# 字符串
str1 = 'abcdefg'
print('a' in str1)
print('z' in str1)

# 列表
list1 = [1, 2, 3, 4, 5, 6]
print(1 in list1)
print(10 in list1)

# 元组
t1 = (1, 2, 3, 4, 5, 6)
print(1 in t1)
print(10 in t1)

# 字典
c = {'jack': 4098, 'sape': 4139, 'yxc':8976}
print('jack' in c)
print('yob' in c)

print(4098 in c)
"""

# is / not is 比较两个对象是否为同一个对象

list1 = [1, 2, [3, 4, 5], 6, 7]
list2 = list1
tuple1 = (1, 2, [3, 4, 5], (6, 7))

print(list1 is list2)
print(list1 is tuple1)


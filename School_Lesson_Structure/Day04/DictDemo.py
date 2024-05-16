"""
author : Yan Peng Bo
Date: 2023-5-28
content: dict_demo project
"""

# 初始化 key : value

"""
# 空字典
a = {}
print(type(a))

tel = {'jack': 4098, 'sape': 4139}
print(tel)

# 修改值
tel['alice'] = 5327
print(tel)

# 删除元素
del tel['jack']
print(tel)

# 强制转换 list
print(list(tel))
print(sorted(tel))
print('alice' in tel)
print('tom' in tel)
"""

# 创建dict
"""
a = dict([('sape', 4321), ('tom', 6799), ('jack', 5674)])
print(a)
b = dict(sape=4139, guido=4127, jack=4098)
print(b)
c = {'jack': 4098, 'sape': 4139}
print(c)
"""

# 清空 clear()
"""
a = {'jack': 4098, 'sape': 4139}
a.clear()
print(a)

"""

# 查询

"""
# name[key]
message = {'yxc': 18, 'ypb': 19, 'abc': 11}
print(message['yxc'])

# get()
a = message.get('yxc')
print(a)

# keys() 方法返回所有的键
print(message.keys())

# values() 方法返回所有的键值
print(message.values())

# items() 方法可同时取出键和对应的值
print(message.items())

for key in message.keys():
    print(key)

for value in message.values():
    print(value)

for key, value in message.items():
    print(f"{key}:{value}")
"""

# 遍历技巧

#  enumerate() 函数可以同时取出位置索引和对应的值
s = ['abc', 'bcd', 'def', 'deg']
for i, v in enumerate(s):
    print(f"下表为{i}的元素为{v}")

#  zip() 函数可以将其内的元素一一匹配

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q, a))

# 逆向遍历
arr = [12, 21, 13, 4, 59, 32, 4, 32]
for i in reversed(arr):
    print(i)

# sorted() 函数
for i in sorted(arr):
    print(i)

# sorted() + set()
for i in sorted(set(arr)):
    print(i)

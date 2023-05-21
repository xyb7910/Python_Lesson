"""
author : Yan Peng Bo
Date: 2023-5-12
content: type_trans_demo project
"""
# input
"""
# 后跟提示语， 且接受到的所有数据均作为字符串处理
name = input("我的名字")
age = input("我的年龄")

print(name)
# 如若输出 age + 1, 则会报错，因为类型不匹配
print(age)

"""
# 强制转换
"""
s_num = input("请输入你的幸运数字：")
print(f"你的幸运数字是{s_num}")
print(f"你的幸运数字的类型是：{type(s_num)}")

num = int(s_num)
print(f"你的幸运数字是{num}")
print(f"你的幸运数字的类型是：{type(num)}")
"""

""""
s_num = '123456789'
print(f"s_num的类型为{type(s_num)}")
n_num = int(s_num)
print(f"n_num的类型为{type(n_num)}")
"""

"""
animals1 = ['pig', 'cat', 'dog', 'fish']
print(animals1)
print(f"animals_cate的类型为：{type(animals1)}")
animals_cate = str(animals1)
print(animals_cate)
print(f"animals_cate的类型为：{type(animals_cate)}")

animals2 = ('pig', 'cat', 'dog', 'fish')
print(animals2)
print(f"animals_cate的类型为：{type(animals2)}")
animals_cate = str(animals2)
print(animals_cate)
print(f"animals_cate的类型为：{type(animals_cate)}")

users = {'Hans': 'active', 'Tom': 'inactive', 'Alice': 'active', 'Bob': 'inactive'}
message = str(users)
print(users)
print(f"animals_cate的类型为：{type(users)}")
messaged = str(users)
print(messaged)
print(f"animals_cate的类型为：{type(messaged)}")
"""


str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(100, 200, 300)'

print(str1)
print(f"str1的类型为：{type(str1)}")
print(str2)
print(f"str1的类型为：{type(str2)}")
print(str3)
print(f"str1的类型为：{type(str3)}")

str1_d = eval(str1)
print(str1_d)
print(f"str1的类型为：{type(str1_d)}")
str2_d = eval(str2)
print(str2_d)
print(f"str2的类型为：{type(str2_d)}")
str3_d = eval(str3)
print(str3_d)
print(f"str3的类型为：{type(str3_d)}")

"""
author : Yan Peng Bo
Date: 2023-5-12
content: homework_demo project
🥹🥹🥹
"""

# test1
"""
# 水仙花数判断
num = int(input("请输入一个三位数字："))
ge = int(num % 10)
shi = int(num / 10 % 10)
bai = int(num / 100)
# print(ge, shi, bai)
if ge ** 3 + shi ** 3 + bai ** 3 == num:
    print("这个数字是水仙花数字")
else:
    print("这个数字不是水仙花数字")
"""

# 成绩判断

"""
grade = int(input("请你输入一个成绩："))
if grade > 85:
    print("优秀")
elif 75 <= grade <= 85:
    print("良好")
elif 60 <= grade < 75:
    print("及格")
elif 0 <= grade < 60:
    print("不及格")
elif grade < 0 or grade > 100:
    print("请不要乱搞呀，成绩的范围为0 ～ 100！！！😅")
"""

# 判断年份
"""
year = int(input("请你输入你喜欢的年份🤪："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("你输入的年份是闰年")
else:
    print("你输入的年份不是闰年")
"""

# 3, 7除
"""
num = int(input("请输入一个数字："))
if num % 3 == 0 and num % 7 == 0:
    print("你输入的数字能同时被三和七整除")
elif num % 3 == 0 and num % 7 != 0:
    print("你输入的数字能能被三整除，但不能被七整除")
elif num % 3 != 0 and num % 7 == 0:
    print("你输入的数字能被七整除，但是不能被三整除")
else:
    print("你输入的数字既不能被三整除，也不能被七整除")
"""

# odd or even
"""
num = int(input("请输入一个数字："))
if num % 2 == 0:
    print("你输入的数字是一个偶数")
else:
    print("你输入的数字是一个奇数")
"""



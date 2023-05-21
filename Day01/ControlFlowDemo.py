"""
author : Yan Peng Bo
Date: 2023-5-5
content: control_flow_demo project
"""

# if
"""
x = int(input("Please input a integer: "))
x = 0
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("More")

"""

# while
"""
num = int(input("这是对你的💌数字:"))
while num:
    if 0 >= num <= 10:
        print("你输入的数字有点小了")
    elif 10 < num < 100:
        print("恭喜你中奖了🥰")
    else:
        print("请再一次输入一个数字吧")
    num = 0
"""

"""
i = 0
while i < 3:
    print("Hello World!!!")
    i += 1
print("循环结束！")
"""

"""
i = 0
sum = 0
while i < 100:
    i += 2
    sum += i
print(f"1~100之间的和为{sum}")
"""
    
# for

"""
words = ['cat', 'pig', 'window', 'desk']
for w in words:
    print(w)
"""

"""
users = {'Hans': 'active', 'Tom': 'inactive', 'Alice': 'active', 'Bob': 'inactive'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for v in active_users:
    print(v)
"""

# range function

"""
for i in range(10):  # 左开右闭
    print(i)
"""

"""
a = ['ypb', 'loves', 'eating', '.']
for i in range(len(a)):
    print(i, a[i])
"""

# break, continue, else
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '==', x, '*', n // x)
    else:
        print(n, 'is a prime number')
"""

"""
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number:", num)
        continue
    print("Found an add number:", num)
"""

# python3.9 不支持此类型
""""
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's worng with the interest"
"""
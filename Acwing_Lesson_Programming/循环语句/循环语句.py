"""
acwing python 基础课
第三章题目
"""
'''
'''

# 斐波那契数列
'''
a1 = 0
a2 = 1
i = 0
while i <= 100:
    a1, a2 = a2, a1 + a2
    i += 1
print(a1, a2)
'''

# 求100之内所有数的立方和
'''
sum = 0
for i in range(100):
    sum += i ** 3
print(sum)
'''

# 求斐波那契数列的第n项
'''
n = int(input())
a, b = 1, 1
for i in range(n):
    a, b = b, a + b
print(a)
'''

# 偶数
'''
# while
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1

# for
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
'''

# 奇数 模拟计数
'''
x = int(input())
for i in range(1, x + 1):
    if i % 2 == 1:
        print(i)
'''

# 正数
'''
sum = 0
for n in range(6):
    num = float(input())
    if num > 0:
        sum += 1

print("%d positive numbers" % sum)
'''

# 递增序列
'''
while True:
    num = int(input())
    if num == 0:
        break
    for i in range(1, num + 1):
        print(i, end=' ')
    print()
'''

# PUM
'''
x, y = map(int, input().split()) #  7 4
num = 1
for i in range(x):
    for j in range(y):
        if num == ((i + 1) * y):
            print("PUM")
        else:
            print(num, end=' ')
        num += 1
'''

# 完全数
'''
n = int(input())

for i in range(n):  # 枚举n次
    x = int(input())
    s = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:  # 如果i是x的约数
            s += i
            if i != x / i:  # 防止x是完全平方数时重复计算
                s += x / i
    s -= x
    if s == x:
        print("%d is perfect" % x)
    else:
        print("%d is not perfect" % x)
'''


# 连续奇数的和1
'''
x = int(input())
y = int(input()) 
# 默认x < y
if x > y:
    x, y = y, x
res = 0
for i in range(x + 1, y):
    if i % 2 != 0:
        res += i
print(res)
'''

# 最大数和它的位置
'''
max_value = -1
max_pos = 0
for i in range(1, 101):
    num = int(input())
    if num > max_value:
        max_value = num
        max_pos = i
print(max_value)
print(max_pos)
'''

# 约数
'''
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
'''

# 余数
'''
n = int(input())
for i in range(1, 10000):
    if i % n == 2:
        print(i)
'''

# 六个奇数
'''
x = int(input())
if x % 2 == 0:
    x += 1
    for i in range(6):
        print(x)
        x += 2
else:
    for i in range(6):
        print(x)
        x += 2
'''

# 乘法表
'''
n = int(input())
for i in range(1, 11):
    print("%d x %d = %d" % (i, n, n * i))
'''

# 区间2
'''
n = int(input())
exist, no_exist = 0, 0
for i in range(n):
    num = int(input())
    if 10 <= num <= 20:
        exist += 1
    else:
        no_exist += 1
print("%d in" % exist)
print("%d out" % no_exist)
'''

# 连续奇数的和 2
'''
n = int(input())
for i in range(n):
    res = 0
    start, end = map(int, input().split())
    if start > end:
        start, end = end, start
    for j in range(start + 1, end):
        if j % 2 != 0:
            res += j
    print(res)
'''

# 简单斐波那契
'''
n = int(input())
a, b = 0, 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
'''

# 数字序列和它的和
'''
while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break
    if n < m:
        # 默认 m < n
        n, m = m, n
    sum = 0
    for i in range(m, n + 1):
        sum += i
        print(i, end=" ")
    print("Sum=%d" % sum)
'''

# 质数
'''
n = int(input())
for i in range(n):
    num = int(input())
    is_prime = True
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            is_prime = False
    if is_prime is True:
        print("%d is prime" % num)
    else:
        print("%d is not prime" % num)
'''

# 菱形
'''
n = int(input())
cx = cy = n // 2
for i in range(n):
    for j in range(n):
        if abs(i - cx) + abs(j - cy) <= n // 2:
            print("*", end='')
        else:
            print(" ", end='')
    print()
'''








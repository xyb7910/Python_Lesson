"""
acwing python 基础课
第五章题目
"""

# 阶乘
'''
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


n = int(input())
print(fact(n))
'''

#  x和y的最大值
'''
def max(x, y):
    if x > y:
        return x
    else:
        return y


x, y = map(int, input().split())
print(max(x, y))
'''

# 最大公约数
'''
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a, b = map(int, input().split())
print(gcd(a, b))
'''

# 打印数字
'''
def print1D(a, size):
    for i in range(size):
        print(a[i], end=' ')


n, size = map(int, input().split())
a = list(map(int, input().split()))
print1D(a, size)
'''

# 数组翻转
'''
def reverse(a, size):
    i, j = 0, size - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


n, size = map(int, input().split())
a = list(map(int, input().split()))
reverse(a, size)
for i in range(n):
    print(a[i], end=' ')
'''

# 递归求阶乘
'''
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

n = int(input())
print(fact(n))
'''

# 递归求斐波那契数列
'''
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input())
print(fibonacci(n))
'''


# 绝对值
'''
def abs(n):
    if n == 0:
        return n
    elif n > 0:
        return n
    else:
        return - n


n = int(input())
print(abs(n))
'''

# 两个数的和
'''
def add(a, b):
    return a + b
x, y = map(float, input().split())
print("%.2f" % add(x, y))
'''

# 区间求和
'''
def sum(a, b):
    sum = 0
    for i in range(a, b + 1):
        sum += i
    return sum
l, r = map(int, input().split())
print(sum(l, r))
'''

# 最小公倍数
# 个人思路不明确
'''
def lcm(a, b):
    
a, b = map(int, input().split())
print(lcm(a, b))
'''


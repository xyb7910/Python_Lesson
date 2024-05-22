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
''''
def lcm(a, b) -> int:
    # find greater
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            res = greater
            break
        greater += 1
    return res


def gcd(a, b) -> int:
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_lcm(a, b) -> int:
    res = (a * b) // gcd(a, b)
    return res


a, b = map(int, input().split())
print(gcd_lcm(a, b))
'''

# 复制数组
'''
def copy(a, b, size):
    for i in range(size):
        b[i] = a[i]


n, m, size = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
copy(a, b, size)
for i in range(m):
    print(b[i], end=" ")
'''

# 打印字符串
'''
def print_str(s):
    print(s)


str1 = input()
print_str(str1)
'''

# 打印矩阵
'''
def print2D(a, row, col):
    for i in range(row):
        for j in range(col):
            print(a[i][j], end=" ")
        print()


row, col = map(int, input().split())
a = []
for i in range(row):
    a.append(list(map(int, input().split())))
print2D(a, row, col)
'''

# 数组去重
'''
def get_unique_count(l, n) -> int:
    cnt = 0
    for i in range(n):
        for j in range(i):
            if l[i] == l[j]:
                break
        else:
            cnt += 1
    return cnt


n = int(input())
a = list(map(int, input().split()))
print(get_unique_count(a, n))

n = int(input())
l = list(map(int, input().split()))
'''

# 数组排序
'''
def sort(a, l, r):
    for i in range(l, r + 1):
        for j in range(i + 1, r + 1):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


n, l, r = map(int, input().split())
a = list(map(int, input().split()))
sort(a, l, r)
for u in a:
    print(u, end=" ")
'''

# 跳台阶
'''
def solve(n):
    if 0 < n <= 2:
        return n
    return solve(n - 1) + solve(n - 2)


n = int(input())
print(solve(n))
'''

# 走方格
'''
def solve(n, m) -> int:
    if n < 0 or m < 0:
        return 0
    if n == 0 and m == 0:
        return 1
    return solve(n - 1, m) + solve(n, m - 1)


n, m = map(int, input().split())
print(solve(n, m))
'''


# 排列
n = int(input())
path = [0 for i in range(n)]
st = [False for i in range(n)]


def dfs(u):
    if u == n:
        for x in path:
            print(x + 1, end= ' ')
        print()
    else:
        for i in range(n):
            if not st[i]:
                path[u] = i
                st[i] = True
                dfs(u + 1)
                st[i] = False
                path[u] = 0

dfs(0)

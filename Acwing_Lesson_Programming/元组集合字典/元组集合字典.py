"""
acwing python 基础课
第七章题目
"""
# 不同正整数的个数
'''
n = int(input())
L = list(map(int, input().split()))

S = set()
for v in L:
    if v > 0:
        S.add(v)

print(len(S))
'''
# 模拟散列表
'''
n = int(input())
S = set()
for i in range(n):
    op, num = input().split()
    num = int(num)
    if op == 'I':
        S.add(num)
    else:
        if num in S:
            print("Yes")
        else:
            print("No")
'''

# 字符串赋值
'''
n = int(input())
dic = dict()
for i in range(n):
    str, value = input().split()
    dic[str] = value
m = int(input())
for i in range(m):
    target = input()
    if target in dic:
        print(dic[target])
    else:
        print("-1")
'''

#  门禁系统
'''
n = int(input())
dic = dict()
for x in map(int, input().split()):
    if x not in dic:
        dic[x] = 0
    dic[x] += 1
    print(dic[x], end=' ')
'''

# 数字排序
'''
n = int(input())
L = list(map(int, input().split()))
dic = dict()

for x in L:
    if x not in dic:
        dic[x] = 0
    dic[x] += 1

a = list(dic.items())
a.sort(key=lambda item: (-item[1], item[0]))
for k, v in a:
    print(k, v)
'''

# 奇偶
'''
str = input()
S = set()
for v in range(len(str)):
    if 'a' <= str[v] <= 'z':
        S.add(str[v])

if len(S) % 2 == 0:
    print("even")
else:
    print("odd")
'''

#  字符串
'''
n = int(input())
str = input().lower()
S = set()

for x in str:
    S.add(x)

if len(S) == 26:
    print("YES")
else:
    print("NO")
'''

# 查找
'''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
S = set()
for x in a:
    S.add(x)

for x in b:
    if x not in S:
        print("NO")
    else:
        print("YES")
'''

# 出现次数最多的数
'''
n = int(input())
a = list(map(int, input().split()))
cnt = {}
for x in a:
    if x not in cnt:
        cnt[x] = 0
    cnt[x] += 1

rk, rv = 0, 0
for k, v in cnt.items():
    if v > rv or v == rv and k < rk:
        rk, rv = k, v
print(rk)
'''

# 子串计算
from sys import stdin
for s in stdin.readlines():
    cnt = {}
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            t = s[i:j]
            if t not in cnt:
                cnt[t] = 0
            cnt[t] += 1

    for k in sorted(cnt):
        if cnt[k] > 1:
            print(k, cnt[k])

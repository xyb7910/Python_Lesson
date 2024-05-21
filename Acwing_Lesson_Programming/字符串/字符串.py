"""
acwing python 基础课
第四章题目
"""
# 字符串长度
'''
str1 = input()
print(len(str1))
'''

#  字符串中的数字个数
'''
str1 = input()
res = 0
for i in str1:  
    if i.isdigit():
        res += 1
print(res)
'''

# 字符串加空格
'''
str1 = input()
for i in str1:
    print(i, end=" ")
'''

# 替换字符
'''
str1 = input()
target = input()
print(str1.replace(target, '#'))
'''

# 字符串插入
'''
from sys import stdin

for line in stdin.readlines():
    a, b = line.strip().split()
    k = 0
    for i in range(1, len(a)):
        if a[i] > a[k]:
            k = i
    print(a[:k + 1] + b + a[k + 1:])
'''

# 只出现一次的字符
'''
str1 = input()
cnt = [0 for i in range(len(str1))]

for c in str1:
    # 获取字符的ASCII
    t = ord(c) - 97
    cnt[t] += 1

for c in str1:
    t = ord(c) - 97
    if cnt[t] == 1:
        print(c)
        break
else:
    print("no")
'''

# 输出字符串
'''
a = input()
for i in range(len(a)):
    t = ord(a[i]) + ord(a[(i + 1) % len(a)])
    print(chr(t), end="")

'''

# 字符串中最长的连续出现的字符
'''
n = int(input())

for i in range(n):
    s = input()
    c, d = ' ', 0
    for j in range(len(s)):
        for k in range(j, len(s)):
            if s[j] != s[k]:
                break
            cnt = k - j + 1
            if cnt > d:
                c = s[j]
                d = cnt
    print(c, d)
'''

# 字符串匹配
'''
k = float(input())
a = input()
b = input()
cnt = 0
for i in range(len(a)):
    if a[i] == b[i]:
        cnt += 1

if cnt / len(a) >= k:
    print("yes")
else:
    print("no")
'''

# 忽略大小写比较字符串大小
'''
str1 = input().lower()
str2 = input().lower()

if str1 > str2:
    print(">")
elif str1 < str2:
    print("<")
else:
    print("=")
'''

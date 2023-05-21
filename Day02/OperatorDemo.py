"""
author : Yan Peng Bo
Date: 2023-5-12
content: operator project
"""

# 三元运算符 + 函数
def gcd(a, b):
    return gcd(b, a % b) if b else a

div = gcd(4, 6)
print(div)

def max_3(a, b, c):
    return a if a > b else b if a > c else c

num = max_3(4, 2, 3)
print(num)

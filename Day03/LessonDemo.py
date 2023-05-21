"""
author : Yan Peng Bo
Date: 2023-5-21
content: Lesson_demo project
"""
# 打印满正方形
"""
for i in range(4):
    for j in range(4):
        print(f"*", end="")
    print()
"""
# 打印镂空正方形
"""
size = int(input("请输入打印镂空正方形的规模："))
for i in range(size):
    for j in range(size):
        if(i == 0 or j == 0 or i == size - 1 or j == size - 1):
            print(f"*", end="")
        else:
            print(f" ", end='')
    print()
"""

# 打印镂空矩形
"""
length = int(input("请输入镂空矩阵的长："))
width = int(input("请输入镂空矩阵的宽："))
for i in range(width):
    for j in range(length):
        if (i == 0 or j == 0 or i == width - 1 or j == length - 1):
            print(f"*", end="")
        else:
            print(f" ", end='')
    print()
"""

# 打印偏三角形（直角）
"""
for i in range(5):
    for j in range(i):
        print(f"*", end="")
    print()
"""

# 打印💠
"""
n = int(input("请你输入💠的大小："))
c = n // 2
for i in range(n):
    for j in range(n):
        if abs(i - c) + abs(j - c) <= n / 2:
            print(f"*", end='')
        else:
            print(f" ", end='')
    print()
"""


# 打印正三角
"""
size = int(input("请输入正三角形的大小:"))
for i in range(size):
    # 控制打印空格的个数
    for j in range(0, size - i):
        print(end=" ")
    # 控制打印*的个数
    for k in range(size - i, size):
        print("*", end=" ")
    print()
"""

# 打印倒三角
"""
size = int(input("请输入倒三角形的大小："))
for i in range(size):
    for j in range(0, i):
        print(end=" ")
    for k in range(i, size):
        print("*", end=" ")
    print()
"""

# 打印左上角三角形
"""
size = int(input("请输入左上角三角形的大小："))
for i in range(size):
    for j in range(0, size - i):
        print("*", end=" ")
    print()
"""

# 打印右上角三角形
"""
size = int(input("请输入右上角三角形的大小："))
for i in range(size):
    for j in range(0, i):
        print(" ", end=" ")
    for k in range(i, size):
        print("*", end=" ")
    print()
"""

# 打印左下角三角形
"""
size = int(input("请输入左下角三角形的大小："))
for i in range(size):
    for j in range(0, i):
        print("*", end=" ")
    print()
"""

# 打印右下角三角形
"""
size = int(input("请输入右下角三角形的大小："))
for i in range(size):
    for j in range(0, size - i):
        print(" ", end=" ")
    for k in range(size - i, size):
        print("*", end=" ")
    print()
"""

# 九九乘法表
"""
for i in range(10):
    for j in range(i + 1):
        if(j > 0):
            print(f"{i}*{j}={i * j}", end=" ")
    print()
"""


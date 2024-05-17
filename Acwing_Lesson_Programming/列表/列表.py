"""
acwing python 基础课
第三章题目
"""
# 数组替换
'''
for i in range(10):
    num = int(input())
    if num <= 0:
        num = 1
    print("X[%d] = %d" % (i, num))
'''

# 数组填充
'''
#  第一种写法
list = []
v = int(input())
for i in range(10):
    list.append(v)
    v *= 2
    print("N[%d] = %d" % (i, list[i]))

# 第二种写法
list1 = [v * 2 ** i for i in range(10)]
for i in range(10):
    print("N[%d] = %d" % (i, list1[i]))
'''



"""
author : Yan Peng Bo
Date: 2023-5-21
content: str_test_demo project
"""
# 起始位置 ： 终止位置 ： 步长(步向)
string = "123456789"
print(f"{string}的长度为{len(string)}")
# 1 ～ 3
print(string[:4])
# 1 ～ 9
print(string[:])
# 2 ～ 9
print(string[2:])
# 1 ～ 6
print(string[:-3])
# 5 ～ 8
print(string[-5:-1])
# 1 ～ 9
print(string[-100:])
# 13579
print(string[::2])
# 975
print(string[-1:-6:-2])
# 12345678
print(string[:-1])
# 特殊值验证
print(f"下表为0时的元素为{string[0]}", end=" ")
print(f"下表为1时的元素为{string[1]}", end=" ")
print(f"下表为-1时的元素为{string[-1]}", end=" ")

"""
author : Yan Peng Bo
Date: 2023-5-21
content: loop_else_demo project
"""
# 查找元素
"""
string = 'I Love You'
s = input("请输入你所要查找的字母是：")
cnt = 1
for word in string:
    if word != s:
        cnt += 1
    else:
        print(f"{s}是这句话之中的第{cnt}个元素")
        break
else:
    print("没有找到你所要找的字母")
"""

# 跳过元素
"""
string = "abcdefg"
s = input("请输入你所要跳过的字母（a ~ g）是：")
for word in string:
    if s == word:
        continue
    else:
        print(word, end="")
else:
    print("程序运行结束")
# continue指的是退出当前一次循环继而继续下一次循环，这样continue循环是正常结束的，else之后的的代码是正常执行的。
"""

# 终止位置输出
"""
string = "abcdefg"
s = input("请输入你所要跳过的字母（a ~ g）是：")
for word in string:
    if s == word:
        break
    else:
        print(word, end="")
else:
    print("程序运行结束")
# break是终止循环，一旦遇到break就代表循环是非正常结束的，因为break是终止循环这个时候else之后的的代码是不执行的。
"""





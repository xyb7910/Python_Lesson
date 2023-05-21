"""
author : Yan Peng Bo
Date: 2023-5-21
content: str_methods_demo project
"""
string1 = "I Love SJTU, It Is An University!"
string2 = "SJTU"

# find(str, beg, end) 接受部分省略

"""
print(string1.find(string2))
print(string1.find(string2, 5))
print(string1.find(string2, 0, len(string1)))
"""

# index(str, beg, end) 接受部分省略
"""
print(string1.index(string2))
print(string1.index(string2, 5))
# print(string1.index("This", 5))
print(string1.index(string2, 0, len(string1)))
"""

# count(str, beg, end)
"""
print(string1.count(" ", 0, len(string1)))
print(string1.count(" ", 10, len(string1)))
"""

# replace(old_str, new_str, [max_count]) 若没有max_count，则全部修改
"""
string1_test = "I Love SJTU SJTU SJTU SJTU, It Is An University!"
print(f"修改之前的字符串是:{string1}")
string_rep1 = string1_test.replace("SJTU", "YAU")
string_rep2 = string1_test.replace("SJTU", "YAU", 3)
print(f"修改之后的字符串是:{string_rep1}")
print(f"修改3次之后的字符串是:{string_rep2}")
"""

# split(str, num) 分割会造成串的丢失

"""
string3 = "1a 2a 3a 1b 2b 3b 4b 5b 6b 7b 8b 9b"
print(string3.split(" "))
print(string3.split("b"))
print(string3.split("b", 5))
"""


# join(str) 序列中的元素以指定的字符连接生成一个新的字符串
"""
s1 = "-"
s2 = ""
s3 = "❤️"
seq = ("1", "2", "3", "4", "5", "6")
print(s1.join(seq))
print(s2.join(seq))
print(s3.join(seq))
"""



my_str = "Hello"
print("该字符串为：", my_str)
# ljust(width, fillchar) 返回一个原字符串左对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
print("该字符串左对齐后的字符串为：", my_str.ljust(10, "p"))
# rjust(width, fillchar) 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串
print("该字符串右对齐后的字符串为：", my_str.rjust(10, "p"))
# center(width, fillstr) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
print("该字符串居中对齐后的字符串为：", my_str.center(10, "p"))

print("--------------------------------------")

print("该字符串为：", string1)
# startwith（substr, beg, end）检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。
print("该字符串是否以I开头：", string1.startswith("I"))
print("该字符串从第5个位置到第10个位置是否以I开头：", string1.startswith("I", 5, 10))
# 对应的的 endwith(substr, beg, end)
print("该字符串以！结尾：", string1.endswith("!"))
print("该字符串从第-5个位置到第-10个位置是否以I开头：", string1.endswith("I", -5, -10))

# isdigit() 如果字符串只包含数字则返回 True 否则返回 False
print("该字符串是否只包含数字：", string1.isdigit())
# isalpha() 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False
print("该字符串是否只包含字母或者中文：", string1.isalpha())

# isspace() 如果字符串中只包含空白，则返回 True，否则返回 False
print("该字符串是否只包含空白：", string1.isspace())
# isnumeric() 如果字符串中只包含数字字符，则返回 True，否则返回 False
print("该字符串是否只包含数字：", string1.isnumeric())
# isalnum() 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False
print("该字符串是否只包含数字和字符：", string1.isalnum())
# islower() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
print("该字符串是否所有的字母都是小写：", string1.islower())
# isupper() 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print("该字符串是否所有的字母都是大写：", string1.isupper())
# istitle() 如果字符串是标题化的(见 title())则返回 True，否则返回 False
print("该字符串是否为规格化的字符串：",string1.istitle())


# other
"""
my_str = 'i love Scy!'
print("原字符串为：", my_str)
# capitlize() 将字符串的第一个字母变成大写，其他字母变小写
print("把整个字符串的第一个字母变为大写为：", my_str.capitalize())
# title()  返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写
print("把整个自字符串的每个单词的首字母变为大写为：", my_str.title())
# upper() 转换字符串中的小写字母为大写
print("把整个字符串全部变为大写为：", my_str.upper())
# lower() 转换字符串中所有大写字符为小写
print("把整个字符串全部变为小写为：", my_str.lower())

content = "   i love yxc   "
# lstrip() 删除字符串左边的空白字符串
print("删除字符串的左侧空白：", content.lstrip())
# rstrip() 删除字符串右边的空白字符串
print("删除字符串的右侧空白：", content.rstrip())
# strip() 删除字符串两边的空白字符串
print("删除字符串的两侧空白：", content.strip())

str1 = "AbCdeFg"
print("此字符串中最大的字母为：", max(str1))
print("此字符串中最小的字母为：", min(str1))
print("此字符串的大小写互相转换为：", str1.swapcase())
"""




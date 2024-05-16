"""
author : Yan Peng Bo
Date: 2023-5-28
content: atm_module_demo project
"""

from atm import *

select_fun()

num = int(input("请输入你所要执行的业务"))

if num == 1:
    card_num = int(input("请输入你的卡号"))
    find(card_num)
elif num == 2:
    card_num = int(input("请输入你的卡号"))
    num = int(input("请输入你所要存入的现金"))
    add(card_num, num)
elif num == 3:
    card_num = int(input("请输入你的卡号"))
    num = int(input("请输入你所要取走的现金"))
    withdrawal(card_num, num)
else:
    print("欢迎下次使用，祝你一路顺风")
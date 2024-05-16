"""

author : Yan Peng Bo
Date: 2023-5-12
content: Practice_Demo project

猜拳游戏🎮

需求：
    人机对战
        玩家：手动输入
        电脑：随机出拳
    判断输赢：
        玩家获胜🏅️
        电脑获胜🏅️
    规则：0 - ✊ 1 - ✂️ 2 - 布
"""
import random

computer = random.randint(0, 2)
print(computer)

player = int(input("请出拳：0 - ✊ 1 - ✂️ 2 - 布"))
while 0 <= player <= 2:
    if player == 0 and computer == 1:
        print("Player Win!!!")
    elif player == 1 and computer == 2:
        print("Player Win!!!")
    elif player == 2 and computer == 0:
        print("Player Win!!!")
    elif player == 1 and computer == 0:
        print("Computer Win!!!")
    elif player == 2 and computer == 1:
        print("Computer Win!!!")
    elif player == 0 and computer == 2:
        print("Computer Win!!!")
    else:
        print("Draw!!!")
    player = -1



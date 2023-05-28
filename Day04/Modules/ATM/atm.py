def select_fun():
    print("-----请选择功能-----")
    print("1查询余额")
    print("2存款")
    print("3取款")
    print("4退出系统")
    print("-------------------")


card = {1: 102, 2: 901, 3: 876, 4: 897, 5: 111, 6: 435}


def find(card_num):
    print(f"你账户的余额为{card[card_num]}")


def add(card_num, num):
    print(f"你账户的余额为{card[card_num]}")
    card[card_num] += num
    print(f"目前你账户的余额为{card[card_num]}")


def withdrawal(card_num, num):
    print(f"你账户的余额为{card[card_num]}")
    card[card_num] -= num
    print(f"目前你账户的余额为{card[card_num]}")

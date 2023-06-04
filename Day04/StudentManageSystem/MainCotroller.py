from StuManageFunction import *
"""
author : Yan Peng Bo
Date: 2023-5-28
content: student_manage_system_main_controller_demo project
"""
"""
应用： 学员管理系统
需求：进入系统显示功能界面，功能如下：
    添加学员
    删除学员
    修改学员信息
    查询学员信息
    显示所有学员信息
    退出系统
系统总共6个功能，用户根据自己的需求选取

步骤分析：
    1.显示功能界面
    2.用户输入功能序号
    3.根据用户输入的功能，执行不同的功能（函数）
        3.1 定义函数
        3.2 调用函数
"""


# 主界面
def main_info():
    print("-----欢迎登录学员管理系统-----")
    print("      1.添加学员信息")
    print("      2.删除学员信息")
    print("      3.修改学员信息")
    print("      4.查询学员信息")
    print("      5.显示所有学员信息")
    print("      6.退出系统")
    print("----------------------------")


# 所有的功能函数都是操作学员信息，所有存储学员信息应该是一个全局变量，数据类型为列表
info = []  # 存储学员信息

# 循环 重复操作
while True:
    # 1.显示用户的主界面
    main_info()
    # 2.用户输入序号，选择功能
    user_num = int(input("请选择您需要执行的操作："))
    # 3.根据序号执行对应功能
    if user_num == 1:
        print("-----添加学员信息-----")
        add_info()
    elif user_num == 2:
        print("-----删除学员信息-----")
        del_info()
    elif user_num == 3:
        print("-----修改学员信息-----")
        modify_info()
    elif user_num == 4:
        print("-----查询学员信息-----")
        find_info()
    elif user_num == 5:
        print("-----所有学员信息-----")
        print_all()
    elif user_num == 6:
        exit_flag = input("确定要退出吗？yes or no:")
        if exit_flag == 'yes':
            break
    else:
        print("您的输入有误，请重新输入！！！")

"""
author : Yan Peng Bo
Date: 2023-6-3
content: student_manage_system_main_controller_demo project
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


info = []  # 存储学员信息


def add_info():

    stu_id = int(input("请输入学号："))
    stu_name = input("请输入姓名:")
    stu_sex = input("请输入性别:")

    global info

    for i in info:
        if stu_id == i["id"]:
            print("该学号的学员信息已经存在！")
            return

    info_dict = {"id": stu_id, "name": stu_name, "sex": stu_sex}
    info.append(info_dict)

    print(info)

def del_info():

    while True:
        del_id = int(input("请输入要删除的学员学号："))
        global info
        for i in info:
            if i.get("id") == del_id:
                del_flag = input("确定要删除吗？yes or no:")
                if del_flag == 'yes':
                    del info[info.index(i)]
                print(info)

                return
            else:
                print("输入学员学号有误，请重新输入")

def modify_info():
    while True:
        update_id = int(input("请输入要修改的学员学号："))

        global info

        for i in info:

            if i.get("id") == update_id:
                print(f"该学员的学号：{i.get('id')},姓名：{i.get('name')},性别：{i.get('sex')}")
                i["id"] = int(input("请输入学号:"))
                i["name"] = input("请输入姓名:")
                i["sex"] = input("请输入性别:")
                update_flag = input("确定要修改吗？yes or no:")
                if update_flag == 'yes':
                    print(info)
                return
            else:
                print("输入学员学号有误，请重新输入")

def find_info():
    find_name = input("请输入要查找的学员姓名:")
    for i in info:
        if find_name == i["name"]:
            print("查到信息如下：")
            print(f"该学员的学号：{i['id']},姓名：{i['name']},性别：{i['sex']}")
            break
    else:
        print("查无此人......")




def print_all():

    print('学号\t姓名\t性别')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['sex']}")


while True:
    main_info()
    user_num = int(input("请选择您需要执行的操作："))
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

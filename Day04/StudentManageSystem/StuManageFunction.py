"""
author : Yan Peng Bo
Date: 2023-5-28
content: student_manage_system_function project
"""
"""
    功能一 添加学员信息
    需求分析：
        1. 接收用户输入的学员信息，并保存
        2. 判断是否添加学员信息
            2.1 如果学员学号已经存在，则报错提示
            2.2 如果学员学号不存在，则准备空字典，将用户输入的数据追加到字典，再在列表中追加字典数据
        3. 对应的if条件成立的位置调用该函数
"""


def add_info():
    """添加学员信息"""
    # 从键盘接收学员信息
    stu_id = int(input("请输入学号："))
    stu_name = input("请输入姓名:")
    stu_sex = input("请输入性别:")
    # 声明info为全局变量
    global info
    # 检测用户输入的学号是否存在，存在则报错提示
    for i in info:
        if stu_id == i["id"]:
            print("该学号的学员信息已经存在！")
            return
    # 如果用户输入的学号不存在，则添加该学员信息
    info_dict = {"id": stu_id, "name": stu_name, "sex": stu_sex}

    # 将用户输入的数据添加到字典

    # 将这个学员字典追加到列表中
    info.append(info_dict)
    # 暂时输出  后期会删掉
    print(info)


"""
    功能二 删除学员信息
    需求分析：
     按用户输入的学员的学号进行删除
        1. 接收用户输入的学员学号
        2. 判断该学号对应的学员是否存在
            2.1 如果学员学号已经存在，则从列表中删除数据
            2.2 如果学员学号不存在，则报错，并重新输出
        3. 对应的if条件成立的位置调用该函数
"""


def del_info():
    """删除学员"""
    while True:
        del_id = int(input("请输入要删除的学员学号："))
        # 声明info为全局变量
        global info
        # 检查学员是否存在
        for i in info:
            # 如果存在则删除列表指定下标的数据
            if i.get("id") == del_id:
                del_flag = input("确定要删除吗？yes or no:")
                if del_flag == 'yes':
                    # 找到当前学员的整体信息(字典)在列表中的下标 然后再删除这个列表元素。
                    del info[info.index(i)]
                print(info)
                # 删除了目标学员后退出循环
                return
            else:
                print("输入学员学号有误，请重新输入")


"""
    功能三 修改学员信息
    需求分析：
     按用户输入的学员的学号进行修改
        1. 接收用户输入的学员学号
        2. 判断该学号对应的学员是否存在
            2.1 如果学员学号已经存在，显示学员信息，然后修改数据
            2.2 如果学员学号不存在，则报错，并重新输出
        3. 对应的if条件成立的位置调用该函数
"""


def modify_info():
    """修改学员信息"""
    while True:
        update_id = int(input("请输入要修改的学员学号："))
        # 声明info为全局变量
        global info
        # 检查学员是否存在
        for i in info:
            # 如果存在显示学生数据
            if i.get("id") == update_id:
                print(f"该学员的学号：{i.get('id')},姓名：{i.get('name')},性别：{i.get('sex')}")
                i["id"] = int(input("请输入学号:"))
                i["name"] = input("请输入姓名:")
                i["sex"] = input("请输入性别:")
                update_flag = input("确定要修改吗？yes or no:")
                if update_flag == 'yes':
                    print(info)
                # 修改了目标学员后退出循环
                return
            else:
                print("输入学员学号有误，请重新输入")


"""
    功能四 查询学员信息
    需求分析：
     按用户输入的学员的姓名进行查询
        1. 接收用户输入的学员姓名
        2. 判断该姓名对应的学员是否存在
            2.1 如果学员姓名已经存在，显示学员信息
            2.2 如果学员姓名不存在，则报错
        3. 对应的if条件成立的位置调用该函数
"""


def find_info():
    """查询学员信息"""
    find_name = input("请输入要查找的学员姓名:")
    for i in info:
        if find_name == i["name"]:
            print("查到信息如下：")
            print(f"该学员的学号：{i['id']},姓名：{i['name']},性别：{i['sex']}")
            break
    else:
        print("查无此人......")


"""
    功能5 显示所有学员信息
    需求分析：
        打印所有学员信息
"""


def print_all():
    """显示所有学员信息"""
    print('学号\t姓名\t性别')
    for i in info:
        print(f"{i['id']}\t{i['name']}\t{i['sex']}")

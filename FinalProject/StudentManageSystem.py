"""
author : Yan Peng Bo
Date: 2023-6-8
content: student_manage_system project
"""
import csv


# 学生类
class Student:
    def __init__(self, student_id, name, age, gender, contact):
        self.student_id = student_id  # 学号
        self.name = name  # 姓名
        self.age = age  # 年龄
        self.gender = gender  # 性别
        self.contact = contact  # 联系方式


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # 增加学员信息
    def add_student(self, student):
        self.students.append(student)
        print("学员信息添加成功！")

    # 删除学员信息
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                confirmation = input("确定要删除学员信息吗？(Y/N): ")
                if confirmation.lower() == "y":
                    self.students.remove(student)
                    print("学员信息删除成功！")
                else:
                    print("取消删除学员信息。")
                return
        print("找不到该学员信息！")

    # 修改学员信息
    def modify_student(self, student_id, **kwargs):
        for student in self.students:
            if student.student_id == student_id:
                print("找到以下学员信息：")
                print(vars(student))
                confirmation = input("确定要修改学员信息吗？(Y/N): ")
                if confirmation.lower() == "y":
                    for key, value in kwargs.items():
                        if hasattr(student, key):
                            setattr(student, key, value)
                        else:
                            print(f"无效的属性名: {key}")
                            return
                    print("学员信息修改成功！")
                else:
                    print("取消修改学员信息。")
                return
        print("找不到该学员信息！")

    # 通过学员姓名进行模糊查询
    def query_student_name(self, *keywords):
        results = []
        for student in self.students:
            match = True
            for keyword in keywords:
                if keyword.lower() not in student.name.lower():
                    match = False
                    break
            if match:
                results.append(student)

        if results:
            for student in results:
                print(vars(student))
        else:
            print("找不到符合条件的学员信息！")

    # 通过学员id进行查询
    def query_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(vars(student))
                return

        print("找不到符合条件的学员信息！")

    # 展示信息
    def display_students(self):
        for student in self.students:
            print(vars(student))

    # 加载数据
    def load_data(self, filename):
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                student = Student(row["学号"], row["姓名"], row["年龄"], row["性别"], row["联系方式"])
                self.students.append(student)

    # 存储数据
    def save_data(self, filename):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["学号", "姓名", "年龄", "性别", "联系方式"])
            writer.writeheader()
            for student in self.students:
                writer.writerow({
                    "学号": student.student_id,
                    "姓名": student.name,
                    "年龄": student.age,
                    "性别": student.gender,
                    "联系方式": student.contact
                })

    def show_menu(self):
        while True:
            print("\n欢迎使用学员管理系统")
            print("1. 增加学员信息")
            print("2. 删除学员信息")
            print("3. 修改学员信息")
            print("4. 查询学员信息")
            print("5. 展示所有学员")
            print("6. 退出系统")
            choice = input("请输入功能编号：\n")

            if choice == "1":
                student_id = input("请输入学号：")
                name = input("请输入姓名：")
                age = input("请输入年龄：")
                gender = input("请输入性别：")
                contact = input("请输入联系方式：")
                student = Student(student_id, name, age, gender, contact)
                self.add_student(student)
            elif choice == "2":
                student_id = input("请输入要删除的学号：")
                self.delete_student(student_id)
            elif choice == "3":
                student_id = input("请输入要修改的学号：")
                self.query_student_id(student_id)
                name = input("请输入新的姓名（留空表示不修改）：")
                age = input("请输入新的年龄（留空表示不修改）：")
                gender = input("请输入新的性别（留空表示不修改）：")
                contact = input("请输入新的联系方式（留空表示不修改）：")
                kwargs = {}
                if name:
                    kwargs["name"] = name
                if age:
                    kwargs["age"] = age
                if gender:
                    kwargs["gender"] = gender
                if contact:
                    kwargs["contact"] = contact
                self.modify_student(student_id, **kwargs)
            elif choice == "4":
                num = int(input('请选择你的查询方式:1-姓名  2-学号\n'))
                if num == 1:
                    keyword = input("请输入查询关键词：")
                    self.query_student_name(keyword)
                else:
                    id = input('请输入查询学号\n')
                    self.query_student_id(id)
            elif choice == "5":
                self.display_students()
            elif choice == "6":
                print("感谢使用学员管理系统，再见！")
                break
            else:
                print("无效的选择，请重新输入。")


# 使用示例

if __name__ == "__main__":
    system = StudentManagementSystem()
    system.load_data("students.csv")
    system.show_menu()
    system.save_data("students.csv")

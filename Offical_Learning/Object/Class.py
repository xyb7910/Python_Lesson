class Person:
    '这是一个基类'

    sum = 0

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        Person.sum += 1

    def display(self):
        print("Name:", self.name, ", Age:", self.age, ", Address:", self.address)

    def displaySum(self):
        print("Sum:", self.sum)


class Employee(Person):
    empCount = 1

    def getEmployee(self):
        print("Employee:", self.empCount)

    def getEmployeeMessage(self):
        for i in range(self.empCount):
            print("Employee:", self.name, self.age, self.address)


p1 = Person('yxc', 18, 'yau')
p1.display()
p1.displaySum()

p2 = Employee('ypb', 21, 'Shanxi')
p2.getEmployee()
p2.getEmployeeMessage()

print("-----------------------------------------")

'''
# 获取类的相关信息

# __dict__ 类的属性
for elem in Person.__dict__:
    print(elem, Person.__dict__[elem])

print("\n")

for elem in Employee.__dict__:
    print(elem, Employee.__dict__[elem])
print("\n")

# __name__ 类名
print("Person.__name__:", Person.__name__)
print("Employee.__name__:", Employee.__name__)

# __module__   类定义所在的模块
print("Person.__module__:", Person.__module__)
print("Employee.__module__:", Employee.__module__)

# __bases__ 类的所有父类构造元素
print("Person.__bases__:", Person.__bases__)
print("Employee.__bases__:", Employee.__bases__)
'''
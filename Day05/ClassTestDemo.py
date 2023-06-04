"""
author : Yan Peng Bo
Date: 2023-6-4
content: class_test_demo project
"""
"""
5.1 烤地瓜
    5.1.1 需求
    需求主线：
        1. 被烤的时间和对应的地瓜状态：
            0-3分钟：生的
            3-5分钟：半生不熟
            5-8分钟：熟的
            超过8分钟：烤糊了
        2. 添加的调料：
            用户可以按自己的意愿添加调料
    5.1.2 步骤分析
        需求涉及一个事物： 地瓜，故案例涉及一个类：地瓜类。
    5.1.2.1 定义类
    地瓜的属性
        被烤的时间
        地瓜的状态
        添加的调料
    地瓜的方法
        被烤
            用户根据意愿设定每次烤地瓜的时间
            判断地瓜被烤的总时间是在哪个区间，修改地瓜状态
        添加调料
            用户根据意愿设定添加的调料
            将用户添加的调料存储
    显示对象信息
"""


# 定义类
# 地瓜属性  地瓜初始化  后续根据需求更新实例属性
class SweetPotato():
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 地瓜的状态
        self.cook_static = "生的"
        # 调料列表
        self.coodiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.cook_static = "生的"
        elif 3 <= self.cook_time < 5:
            self.cook_static = "半生不熟"
        elif 5 <= self.cook_time < 8:
            self.cook_static = "熟了"
        elif self.cook_time >= 8:
            self.cook_static = "烤糊了"

    # 添加调料
    def add_coodiments(self, coodiments):
        self.coodiments.append(coodiments)

    # 输出对象状态
    def __str__(self):
        return f"这个地瓜烤了{self.cook_time}分钟，目前的状态是{self.cook_static},添加的调料有{self.coodiments}"


# 创建对象 测试实例属性和实例方法
digua1 = SweetPotato()
print(digua1)  # 这个地瓜烤了0分钟，目前的状态是生的

digua1.cook(2)
digua1.add_coodiments("冰糖")
print(digua1)  # 这个地瓜烤了2分钟，目前的状态是生的,添加的调料有['冰糖']

digua1.cook(2)
digua1.add_coodiments("辣椒面儿")
print(digua1)  # 这个地瓜烤了4分钟，目前的状态是半生不熟,添加的调料有['冰糖', '辣椒面儿']

digua1.cook(5)
print(digua1)  # 这个地瓜烤了9分钟，目前的状态是烤糊了,添加的调料有['冰糖', '辣椒面儿']

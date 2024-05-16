"""
author : Yan Peng Bo
Date: 2023-6-4
content: homework_demo project
"""


class Room:
    def __init__(self, location, area):
        self.location = location  # 地理位置
        self.area = area  # 面积
        self.remaining_area = area  # 剩余面积
        self.furniture_list = []  # 家具列表

    # judge function
    def accommodate_furniture(self, furniture):
        if self.remaining_area >= furniture.area:
            self.furniture_list.append(furniture)
            self.remaining_area -= furniture.area
            print(f"{furniture.name} has been placed in the room.")
        else:
            print(f"Not enough space in the room to accommodate {furniture.name}.")

    # display function
    def display_info(self):
        print(f"Room Location: {self.location}")
        print(f"Total Area: {self.area} sq. units")
        print(f"Remaining Area: {self.remaining_area} sq. units")
        print("Furniture in the room:")
        if self.furniture_list:
            for furniture in self.furniture_list:
                print(f"- {furniture.name}")
        else:
            print("No furniture in the room.")


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


# 创建房间对象
room = Room("Living Room", 100)

# 创建家具对象
sofa = Furniture("Sofa", 20)
table = Furniture("Dining Table", 10)
bed = Furniture("Bed", 30)

# 放置家具到房间内
room.accommodate_furniture(sofa)
room.accommodate_furniture(table)
room.accommodate_furniture(bed)

# 显示房间信息
room.display_info()

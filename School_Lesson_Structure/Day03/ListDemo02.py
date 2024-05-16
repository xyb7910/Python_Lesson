"""
author : Yan Peng Bo
Date: 2023-5-21
content: list_demo02 project
"""
animals_list = ['dog', 'cat', 'duck', 'eagle', 'dove', 'fish', 'fish', 'deer']
# sort(key=None, reverse=False) key 为标准元素
"""
# 升序
animals_list.sort(key=None, reverse=False)
print(animals_list)
# 降序
animals_list.sort(key=None, reverse=True)
print(animals_list)

animals_list1 = animals_list.copy()
print(animals_list1)
"""

# 遍历列表
"""
print("---------------for循环遍历当前列表中元素---------------")
for animal in animals_list:
    print(animal, end=" ")
print()
print("---------------------------------------------------")


print("---------------while循环遍历当前列表中元素---------------")
animal = 0
while animal < len(animals_list):
    print(animals_list[animal], end=" ")
    animal += 1
print()
print("----------------------------------------------------")
"""

# 嵌套
object1 = [['dog', 'cat', 'fish', 'hen'], ['yxc', 'ypb', 'scy'], [1, 2, 4]]
for ob in object1:
    for i in ob:
        if i == 'yxc':
            print("存在yxc")
            break
    else:
        print('不存在yxc')


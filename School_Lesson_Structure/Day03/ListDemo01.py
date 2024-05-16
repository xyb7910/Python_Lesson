"""
author : Yan Peng Bo
Date: 2023-5-21
content: list_demo01 project
"""
animals_list = ['dog', 'cat', 'duck', 'eagle', 'dove', 'fish', 'fish', 'deer']

print("---------------当前列表中元素---------------")
for i in animals_list:
    print(i, end=" ")
print()
print("-----------------------------------------")
# 下表索引
print("列表下标为0的元素为：", animals_list[0])
print("列表下标为1的元素为：", animals_list[1])
print("列表下标为-1的元素为：", animals_list[-1])
# 超域是报异常
# print("列表下标为50的元素为：",animals_list[50])

print("-----------------------------------------")

# append(x) 在列表末尾添加一个元素，相当于 a[len(a):] = [x]
print("追加前列表的最后一个元素为：", animals_list[len(animals_list) - 1])
print("追加前列表的长度为：", len(animals_list))
animals_list.append('fox')
print("将fox追加到列表的尾部")
print("追加后列表的最后一个元素为：", animals_list[len(animals_list) - 1])
print("追加后列表的长度为：", len(animals_list))
animals_list[len(animals_list):] = ['elephant']
print("将elephant追加到列表的尾部")
print("再次追加后列表的最后一个元素为：", animals_list[len(animals_list) - 1])
print("再次追加后列表的长度为：", len(animals_list))

print("---------------当前列表中元素---------------")
for i in animals_list:
    print(i, end=" ")
print()
print("-----------------------------------------")

# insert(i, x) 在指定位置插入元素。第一个参数是插入元素的索引，因此，a.insert(0, x) 在列表开头插入元素， a.insert(len(a), x) 等同于 a.append(x)
animals_list.insert(0, 'monkey')
animals_list.insert(len(animals_list), 'goose')

print("---------------当前列表中元素---------------")
for i in animals_list:
    print(i, end=" ")
print()
print("-----------------------------------------")

# remove(x) 从列表中删除第一个值为 x 的元素。未找到指定元素时，触发 ValueError 异常
print("删除之前列表的长度为", len(animals_list))
animals_list.remove('dog')
print("删除之后列表的长度为", len(animals_list))

print("---------------当前列表中元素---------------")
for i in animals_list:
    print(i, end=" ")
print()
print("-----------------------------------------")

# pop([i]) 删除列表中指定位置的元素，并返回被删除的元素。未指定位置时，a.pop() 删除并返回列表的最后一个元素
pop_first_animal = animals_list.pop(4)
print("删除第五个元素：", pop_first_animal)
pop_second_animal = animals_list.pop()
print("删除最后一个位置的元素：", pop_second_animal)

print("-----------------------------------------")

# count() 返回列表中元素 x 出现的次数
print("fish出现的次数为", animals_list.count('fish'))

print("-----------------------------------------")

# reverse() 反转列表中的元素
print("反转前列表的第一个元素是：", animals_list[0])
print("反转前列表的最后一个元素是：", animals_list[len(animals_list) - 1])
animals_list.reverse()
print("反转后列表的第一个元素是：", animals_list[0])
print("反转后列表的最后一个元素是：", animals_list[len(animals_list) - 1])

# del list_name[index]
print("---------------当前列表中元素---------------")
for i in animals_list:
    print(i, end=" ")
print()
print("-----------------------------------------")

del animals_list[0]
del animals_list[-1]
# 超域是报异常
# del animals_list[50]

print("---------------当前列表中元素---------------")
for i in animals_list:
    print(i, end=" ")
print()
print("-----------------------------------------")

# clear() 删除列表里的所有元素，相当于 del a[:]
print("清空前列表的长度为：", len(animals_list))
animals_list.clear()
print("清空后列表的长度为：", len(animals_list))
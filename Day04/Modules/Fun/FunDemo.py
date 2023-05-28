from FountionPlusDemo import f as print_
from FountionPlusDemo import append as append
from FountionPlusDemo import append_ as append_
from FountionPlusDemo import add_msg as add_msg
from FountionPlusDemo import cheeseshop as cs

# 单次函数，只会执行一次
print_()

# 存在共享变量

print(append(1))
print(append(2))
print(append(3))

# 消除共享变量的影响

print(append_(1))
print(append_(2))
print(append_(3))

# 函数参数 name age active type
# 此函数接受一个必须参数和三个可选参数

add_msg('yxc', age=20, active=20)
add_msg('ypb', active=100, type_s='B')
add_msg('zmz')
# add_msg() 无效的方法调用

cs("Limburger",
   "It's very runny, sir.",
   "It's really very, VERY runny, sir.",
   shopkeeper="Michael Palin",
   client="John Cleese",
   sketch="Cheese Shop Sketch")

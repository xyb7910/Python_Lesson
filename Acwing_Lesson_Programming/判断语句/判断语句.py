"""
acwing python 基础课
第二章题目
"""

# 倍数
'''
a, b = map(int, input().split())
if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
'''

# 零食
'''
# match python3.10 以上支持
x, y = map(int, input().split())
match x:
    case 1:
        print("Total: R$ %.2f" % (y * 4.0))
    case 2:
        print("Total: R$ %.2f" % (y * 4.50))
    case 3:
        print("Total: R$ %.2f" % (y * 5.00))
    case 4:
        print("Total: R$ %.2f" % (y * 2.00))
    case 5:
        print("Total: R$ %.2f" % (y * 1.50))

if x == 1:
    print("Total: R$ %.2f" % (y * 4.0))
elif x == 2:
    print("Total: R$ %.2f" % (y * 4.50))
elif x == 3:
    print("Total: R$ %.2f" % (y * 5.00))
elif x == 4:
    print("Total: R$ %.2f" % (y * 2.00))
elif x == 5:
    print("Total: R$ %.2f" % (y * 1.50))
'''

# 加薪
'''
num = float(input())
if 0 <= num <= 400.00:
    rate = 15
elif 400.00 < num <= 800.00:
    rate = 12
elif 800.00 < num <= 1200.00:
    rate = 10
elif 1200.00 < num <= 2000.00:
    rate = 7
else:
    rate = 4

multi = num * rate / 100

print("Novo salario: %.2f" % (num + multi))
print("Reajuste ganho: %.2f" % multi)
print("Em percentual: %d %%" % rate)
'''

# DDD
'''
num = int(input())
if num == 61:
    print("Brasilia")
elif num == 71:
    print("Salvador")
elif num == 11:
    print("Sao Paulo")
elif num == 21:
    print("Rio de Janeiro")
elif num == 32:
    print("Juiz de Fora")
elif num == 19:
    print("Campinas")
elif num == 27:
    print("Vitoria")
elif num == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
'''

# 游戏时间
'''
start, end = map(int, input().split())
if start > end:
    print("O JOGO DUROU %d HORA(S)" % (24 - start + end))
elif start < end:
    print("O JOGO DUROU %d HORA(S)" % (end - start))
else:
    print("O JOGO DUROU 24 HORA(S)")
'''

# 简单排序
''''
a, b, c = map(int, input().split())
x, y, z = a, b, c
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(a)
print(b)
print(c)
print()
print(x)
print(y)
print(z)
'''

# 选择练习1
'''
a, b, c, d = map(int, input().split())
if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    # 如果所有的数都时正数的可以使用 右移运算
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
'''

# 三角形
'''
a, b, c = map(float, input().split())
if a + b > c and a + c > b and b + c > a:
    print("Perimetro = %.1f" % (a + b + c))
else:
    print("Area = %.1f" % ((a + b) * c * 0.5))
'''

# 区间
'''
x = float(input())

if x < 0 or x > 100:
    print("Fora de intervalo")
elif x <= 25:
    print("Intervalo [0,25]")
elif x <= 50:
    print("Intervalo (25,50]")
elif x <= 75:
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")
'''

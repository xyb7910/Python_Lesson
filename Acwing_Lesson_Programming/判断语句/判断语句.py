"""
acwing python 基础课
第二章题目
"""
import math

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

# 点的坐标
'''
x, y = map(float, input().split())
if x > 0 and y > 0:
    print("Q1")
elif x > 0 > y:
    print("Q4")
elif x < 0 and y < 0:
    print("Q3")
elif x < 0 < y:
    print("Q2")
elif x == 0 and y != 0:
    print("Eixo Y")
elif y == 0 and x != 0:
    print("Eixo X")
else:
    print("Origem")
'''

# 税
'''
salary = float(input())
tax = 0
if salary > 4500:
    tax += (salary - 4500) * 0.28
    salary = 4500
if 3000 < salary <= 4500:
    tax += (salary - 3000) * 0.18
    salary = 3000
if 2000 < salary <= 3000:
    tax += (salary - 2000) * 0.08
    salary = 2000
else:
    tax += 0

if tax == 0:
    print("Isento")
else:
    print("R$ %.2f" % tax)
'''

# 游戏时间2
'''
start_hour, start_minus, end_hour, end_minus = map(int, input().split())

# 根据秒数去判断是否为同一天
begin = start_hour * 60 + start_minus
end = end_hour * 60 + end_minus

if begin < end:
    total = end - begin
else:
    total = 24 * 60 - begin + end

hours = total // 60
minus = total % 60

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (hours, minus))
'''

# 一元二次方程公式
'''
from math import sqrt

a, b, c = map(float, input().split())
x1, x2 = 0, 0
delta = b ** 2 - 4 * a * c
if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
print('R1 = %.5f' % x1)
print('R2 = %.5f' % x2)
'''

# 三角形类型
'''
a, b, c = map(float, input().split())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    b, c = c, b
he = b ** 2 + c ** 2
A = a ** 2
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    if A == he:
        print("TRIANGULO RETANGULO")
    if A > he:
        print("TRIANGULO OBTUSANGULO")
    if A < he:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b != c or b == c != a or c == a != b:
        print("TRIANGULO ISOSCELES")
'''

# 动物
'''
a = input()
b = input()
c = input()

if a == "vertebrado":
    if b == "ave":
        if c == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if c == "onivoro":
            print("homem")
        else:
            print("vaca")
else:
    if b == "inseto":
        if c == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if (c == "hematofago"):
            print("sanguessuga")
        else:
            print("minhoca")
'''

# 平均数3
a, b, c, d = map(float, input().split())
x = (a * 2 + b * 3 + c * 4 + d) / 10
print("Media: %.1f" % x)
if x >= 7.0:
    print("Aluno aprovado.")
elif x < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    y = float(input())
    print("Nota do exame: %.1f" % y)
    z = (x + y) / 2
    if z >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % z)

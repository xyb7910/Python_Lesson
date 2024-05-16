"""
acwing python 基础课
第一章题目
"""
# A + B
'''
a, b = map(int, input().split())
print(a + b)
'''

# 圆的面积
'''
a = float(input())
PI = 3.14159
res = PI * a * a
# 两种保留四位小数写法
print("A=%.4f" % res)
print("A=" + str(round(res, 4)))
'''

# 平均数1
'''
a = float(input())
b = float(input())
pow_a, pow_b = 3.5, 7.5
res = (a * pow_a + b * pow_b) / (pow_a + pow_b)
print("MEDIA = %.5f" % res)
'''

#两点间的距离
'''
from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(str(round(dist, 4)))
'''

# 钞票
'''
money = int(input())
print(money)
list = [100, 50, 20, 10, 5, 2, 1]
bnum, rest = money // list[0], money % list[0]
print("%d nota(s) de R$ 100,00" % bnum)
ws_num, rest = rest // list[1], rest % list[1]
print("%d nota(s) de R$ 50,00" % ws_num)
es_num, rest = rest // list[2], rest % list[2]
print("%d nota(s) de R$ 20,00" % es_num)
snum, rest = rest // list[3], rest % list[3]
print("%d nota(s) de R$ 10,00" % snum)
wsum, rest = rest // list[4], rest % list[4]
print("%d nota(s) de R$ 5,00" % wsum)
esum, rest = rest // list[5], rest % list[5]
print("%d nota(s) de R$ 2,00" % esum)
ysum, rest = rest // list[6], rest % list[6]
print("%d nota(s) de R$ 1,00" % ysum)
'''

# 差
'''
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("DIFERENCA = %d" % (a * b - c * d))
'''

# 工资
'''
people_id = int(input())
people_work_time = int(input())
people_hour_salary = float(input())
print("NUMBER = %d" % people_id)
print("SALARY = U$ %.2f" % (people_hour_salary * people_work_time))
'''

# 油耗
'''
x = int(input())
y = float(input())
print("%.3f km/l" % (x / y))
'''

# 时间转化
'''
time = int(input())
hours, minutes, seconds = int(time / 3600), int(time % 3600 / 60), int(time % 3600 % 60)
print(str(hours) + ':' + str(minutes) + ':' + str(seconds))
'''

# 简单乘积
'''
a = int(input())
b = int(input())
x = a * b
print("PROD = %d" % x)
'''

# 简单计算
'''
product_a_id, product_a_num, product_a_price = map(float, input().split())
product_b_id, product_b_num, product_b_price = map(float, input().split())
x = product_a_num * product_a_price + product_b_num * product_b_price
print("VALOR A PAGAR: R$ %.2f" % x)
'''

# 球的体积
'''
r = int(input())
PI = 3.14159
V = (4 / 3) * PI * r ** 3
print("VOLUME = %.3f" % V)
'''

# 面积
'''
a, b, c = map(float, input().split())
print("TRIANGULO: %.3f" % (a * c * 0.5))
PI = 3.14159
print("CIRCULO: %.3f" % (PI * c ** 2))
print("TRAPEZIO: %.3f" % ((a + b) * c * 0.5))
print("QUADRADO: %.3f" % (b ** 2))
print("RETANGULO: %.3f" % (a * b))
'''

# 平均数2
'''
a = float(input())
b = float(input())
c = float(input())
print("MEDIA = %.1f" % ((a * 2 + b * 3 + c * 5) / 10))
'''

# 工资和奖金
'''
name = input()
salary = float(input())
sum = float(input())
print("TOTAL = R$ %.2f" % (sum * 0.15 + salary))
'''

# 最大值
'''
def self_max(a, b):
    return (a + b + abs(b - a)) / 2


a, b, c = map(int, input().split())
print("%d eh o maior" % self_max(self_max(a, b), c))
'''

# 距离
'''
L = int(input())
DIST = 30
print("%d minutos" % (L / DIST * 60))
'''

# 燃料消耗
'''
S = int(input())
T = int(input())
dist = S * T
print("%.3f" % (dist / 12))
'''

# 钞票和硬币
'''
n = float(input())
n = int(n * 100)

print("NOTAS:")
print("%d nota(s) de R$ 100.00" % (n // 10000))
n %= 10000
print("%d nota(s) de R$ 50.00" % (n // 5000))
n %= 5000
print("%d nota(s) de R$ 20.00" % (n // 2000))
n %= 2000
print("%d nota(s) de R$ 10.00" % (n // 1000))
n %= 1000
print("%d nota(s) de R$ 5.00" % (n // 500))
n %= 500
print("%d nota(s) de R$ 2.00" % (n // 200))
n %= 200

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % (n // 100))
n %= 100
print("%d moeda(s) de R$ 0.50" % (n // 50))
n %= 50
print("%d moeda(s) de R$ 0.25" % (n // 25))
n %= 25
print("%d moeda(s) de R$ 0.10" % (n // 10))
n %= 10
print("%d moeda(s) de R$ 0.05" % (n // 5))
n %= 5
print("%d moeda(s) de R$ 0.01" % n)
'''

# 天数转换
age = int(input())
year, month, day = age // 365, age % 365 // 30, age % 365 % 30
print("%d ano(s)" % year)
print("%d mes(es)" % month)
print("%d dia(s)" % day)

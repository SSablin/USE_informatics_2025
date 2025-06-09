"""Прогноз ЕГЭ-2025"""

# 2 №22215
print('x y z w F')
from itertools import product

for s in product(range(2), repeat=4):
    x, y, z, w = s
    f = (not z) and (not (y and (not x))) and (not (x == w))
    if f:
        print(x, y, z, w, f)
# x y z w F
# 0 0 0 1 True
# 1 0 0 0 True
# 1 1 0 0 True
# wxzy


# 8 №22221
from itertools import product

c = 0
for i in product('01234567', repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('0') == 2:
            f = s
            for h in '0246': f = f.replace(h, 'H')
            for n in '1357': f = f.replace(n, 'N')
            if f.count('HH') == 0 and f.count('NN') == 0:
                c += 1
                print(s, c)
print(c)  # 4032

# 9 №22222
f = open('files/9_22222.txt')
c = 0
for s in f:
    a = list(map(int, s.split()))
    npov = [x for x in a if a.count(x) == 1]
    pov = [x for x in a if a.count(x) == 2]
    mx = max(a)
    # 1
    if len(npov) == 4 and len(pov) == 2:
        # 2
        if mx not in pov:
            # 3
            if (pov[0]) ** 2 >= (sorted(npov)[0] ** 2 + sorted(npov)[1] ** 2):
                c += 1
                print(c, a, pov, npov)
print(c)  # 23

# 11 №22224
from math import ceil, log2

for N in range(1, 2000):
    i = ceil(log2(N))
    if ceil(i * 94 / 8) * 205_000 > 7 * 1024 ** 2:
        print(N)  # 5
        break

# 12 №22225
for n in range(4, 10_000):
    s = '4' + '0' * n
    while '40' in s or '800' in s or '000' in s:
        if '40' in s:
            s = s.replace('40', '0', 1)
        if '800' in s:
            s = s.replace('800', '04', 1)
        if '000' in s:
            s = s.replace('000', '8', 1)
    if sum(map(int, s)) == 36:
        print(n)  # 63

# 13 №22226
from ipaddress import *

ip = ip_address('142.36.195.251')
net = ip_network(f'{ip}/255.255.255.192', False)
for ip in net.hosts():
    print(str(ip).replace('.', ''))  # 14236195193
    break

# 14 №22227
alf = "123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:20]  # x!=0
for x in alf:
    a = int(x + "5B" + x + "8", 21) + int("H053" + x + "7", 21)
    if a % 12 == 0:
        print(x, a // 12)

# 15 №22228
mn = float('inf')
for i in range(1, 2400):
    a = i / 4
    for b in range(int(a + 1), 600):
        f = False
        for x in range(1, 600):
            A = a <= x <= b
            P = 84 <= x <= 341
            Q = 198 <= x <= 412
            if (not (P == Q)) and (not A):
                f = True
                break
        if not f and (b - a) < mn:
            mn = b - a
            print(mn, a, b)  # 328


def f(x):
    p = 84 <= x <= 341
    q = 198 <= x <= 412
    a = a1 <= x <= a2
    return not (p == q) and (not a)


r = []
d = [y for x in [84, 198, 341, 412] for y in [x, x + 0.01, x - 0.01]]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) == 0 for x in d):
            r += [a2 - a1]
print(min(r))  # 328

# 16 №22229
f = [0]
for n in range(1, 5170):
    if n == 1:
        f.append(1)
    else:
        f.append((4 * n - 3) * f[n - 1])
print((f[5168] // 11 + f[5166]) // f[5165])  # 802257043296

# 17 №22230
s = [int(x) for x in open('files/17_22230.txt')]

mn_8 = float('inf')
for x in s:
    if abs(x) % 10 == 8 and abs(x) == x:
        mn_8 = min(mn_8, x)

mx_25 = 0
for x in s:
    if abs(x) % 25 == 0:
        mx_25 = max(mx_25, x)

ans = []
for i in range(len(s) - 2):
    if (((len(str(abs(s[i]))) == 4) + (len(str(abs(s[i + 1]))) == 4) + (len(str(abs(s[i + 2]))) == 4)) == 2 and
            ((abs(s[i]) % mn_8 == 0) + (abs(s[i + 1]) % mn_8 == 0) + (abs(s[i + 2]) % mn_8 == 0)) >= 1 and
            sum(s[i:i + 3]) >= mx_25):
        ans.append(sum(s[i:i + 3]))
print(len(ans), max(ans))  # 10 19674

f = [int(x) for x in open("17_22230.txt")]
mi = min([int(x) for x in open("17_22230.txt") if int(x) > 0 and int(x) % 10 == 8])
ma = max([int(x) for x in open("17_22230.txt") if abs(int(x)) % 25 == 0])
c = 0
maa = 0
for i in range(len(f) - 2):
    a1 = f[i]
    a2 = f[i + 1]
    a3 = f[i + 2]
    y1 = 1 if 1000 <= abs(a1) < 10000 else 0
    y2 = 1 if 1000 <= abs(a2) < 10000 else 0
    y3 = 1 if 1000 <= abs(a3) < 10000 else 0
    y_1 = 1 if abs(a1) % mi == 0 else 0
    y_2 = 1 if abs(a2) % mi == 0 else 0
    y_3 = 1 if abs(a3) % mi == 0 else 0
    su = a1 + a2 + a3
    if (y1 + y2 + y3) == 2 and (y_1 + y_2 + y_3) >= 1 and su >= ma:
        c += 1
        maa = max(maa, su)
print(c, maa)  # 10 19674

"""
№ 22232 Прогноз ЕГЭ-2025
(М. Попков) Два игрока, Патрик и Валера, играют в следующую игру. 
Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Патрик. За один ход игрок может:
– убрать из кучи три камня;
– уменьшить количество камней в куче в два раза, если оно четно, 
иначе сначала добавить 3 камня, а после уменьшить в 2 раза.
Например, из кучи в 30 камней за один ход можно получить кучу из 27 или 15 камней, 
а из кучи в 29 камней за один ход можно получить кучу из 26 или 16 камней.
Игра завершается, когда количество камней в куче становится не более 24.
Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, 
в которой будет 24 или меньше камней. В начальный момент в куче было S камней, S ≥ 25.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
Укажите минимальное значение S, 
при котором Патрик не может выиграть за один ход, но при любом ходе Патрика Валера может выиграть своим первым ходом.

Задание 20.
Для игры, описанной в задании 19, найдите два наименьших значения S, 
при которых у Патрика есть выигрышная стратегия, причём одновременно выполняются два условия:
– Патрик не может выиграть за один ход;
– Патрик может выиграть своим вторым ходом независимо от того, как будет ходить Валера.
Найденные значения запишите в ответе в порядке возрастания.

Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором одновременно выполняются два условия:
– у Валеры есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Патрика;
– у Валеры нет стратегии, которая позволит ему гарантированно выиграть первым ходом. """


# 19 №22232
def g(s, h):
    if s <= 24 and h == 2:
        return True
    if s <= 24 and h != 2:
        return False
    if s > 24 and h == 2:
        return False

    if h % 2 != 0:  # Патрик
        if s % 2 == 0:
            return g(s - 3, h + 1) or g(s // 2, h + 1)
        else:
            return g(s - 3, h + 1) or g((s + 3) // 2, h + 1)
    else:  # Валера
        if s % 2 == 0:
            return g(s - 3, h + 1) and g(s // 2, h + 1)
        else:
            return g(s - 3, h + 1) and g((s + 3) // 2, h + 1)


for s in range(25, 1000):
    if g(s, 0):
        print(s)  # 47


# 20 №22232
def g(s, h):
    if s <= 24 and h == 3:
        return True
    if s <= 24 and h != 3:
        return False
    if s > 24 and h == 3:
        return False

    if h % 2 != 0:  # Патрик
        if s % 2 == 0:
            return g(s - 3, h + 1) and g(s // 2, h + 1)
        else:
            return g(s - 3, h + 1) and g((s + 3) // 2, h + 1)
    else:  # Валера
        if s % 2 == 0:
            return g(s - 3, h + 1) or g(s // 2, h + 1)
        else:
            return g(s - 3, h + 1) or g((s + 3) // 2, h + 1)


for s in range(25, 1000):
    if g(s, 0):
        print(s)  # 50 52


# 21 №22232
# неоч
def g(s, h):
    if s <= 24 and (h == 4 or h == 2):
        return True
    if s <= 24 and h != 2 and h != 4:
        return False
    if s > 24 and h == 4:
        return False

    if h % 2 != 0:  # Патрик
        if s % 2 == 0:
            return g(s - 3, h + 1) or g(s // 2, h + 1)
        else:
            return g(s - 3, h + 1) or g((s + 3) // 2, h + 1)
    else:  # Валера
        if s % 2 == 0:
            return g(s - 3, h + 1) and g(s // 2, h + 1)
        else:
            return g(s - 3, h + 1) and g((s + 3) // 2, h + 1)


for s in range(25, 1000):
    if g(s, 0):
        print(s)  # 53

# 19-21 №22232
from functools import lru_cache


@lru_cache(None)
def game(a):
    if a <= 24: return 'END'
    h = [game(a - 3)]
    if a % 2 == 0:
        h.append(game(a // 2))
    else:
        h.append(game((a + 3) // 2))
    if 'END' in h: return 'W1'
    if set(h) == {'W1'}: return 'L1'
    if 'L1' in h: return 'W2'
    if set(h) in [{'W2'}, {'W1', 'W2'}]: return 'L12'


print(min(s for s in range(25, 1000) if game(s) == 'L1'))  # 47
print([s for s in range(25, 1000) if game(s) == 'W2'])  # 50 52
print(min(s for s in range(25, 1000) if game(s) == 'L12'))  # 53


# 23 №22234
def f(x, end):
    if x == end:
        return True
    if x < end or x == 24:
        return False
    if x > end:
        return f(x - 3, end) + f(x // 3, end)


print(f(308, 81) * f(81, 5))  # 152

# 24 №22235
"""№ 22235 Прогноз ЕГЭ-2025

(М. Попков) Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности,
являющейся корректным арифметическим выражением с целыми неотрицательными числами (без знака),
значение которого равно нулю, а каждое положительное число либо четно, либо делится на 5, но не делится на 10.
В этом выражении никакие два знака арифметических операций не стоят рядом,
порядок действий определяется по правилам математики, в записи чисел отсутствуют незначащие (ведущие) нули."""

from re import *

s = open('files/24_22235.txt').readline()

num = r'(?:[024685]|[1-9][0-9]*[24568])'
proiz = rf'(?:(?:{num}\*)*0(?:\*{num})*)'
reg = rf'(?:{proiz}(?:\+{proiz})*)'
m = max((x.group(0) for x in finditer(reg, s)), key=len)
print(m)
print(len(m))  # 79


# 25 №22236
def div(x):
    s = set()
    for i in range(1134, x, 1000):
        if x % i == 0:
            return i
    return 0


c = 0
x = 30_000_000
while c < 5:
    D = div(x)
    if D != 0:
        print(x, D)
        c += 1
    x += 1

# 30000268 15000134
# 30000402 10000134
# 30000438 4134
# 30000536 7500134
# 30000618 1111134

# 26 №22237
"""
№ 22237 Прогноз ЕГЭ-2025
(М. Попков) В автосалоне продаётся N автомобилей нескольких моделей. Автомобили одной модели имеют одинаковую цену.
Учёт автомобилей ведётся поштучно, для каждого автомобиля известен его текущий статус (продан или нет).
Автомобили разделены на два сегмента: премиум и обычные. К премиум-сегменту относятся автомобили,
цена на которые превышает среднюю цену (среднее арифметическое) всех автомобилей
в базе данных автосалона без учёта их текущего статуса, остальные автомобили относятся к обычному сегменту.
Лидером продаж называется автомобиль с такой моделью, наибольшее количество экземпляров которой продано.
Лидер продаж выбирается среди автомобилей премиум-сегмента,
а если продано одинаковое количество автомобилей премиум-сегмента с разными моделями,
лидером выбирается автомобиль с наибольшей ценой.
Если и таких автомобилей несколько, лидер продаж — тот из них, которого осталось меньше всего.
Найдите суммарную выручку автосалона от реализации автомобиля — лидера продаж,
а также оставшееся количество автомобилей этой модели.
Входные данные
В первой строке входного файла находится число
N — количество автомобилей в базе данных автосалона (натуральное число, не превышающее 10 000).
В каждой из следующих N строк находится три числа, разделённых пробелом:
ID модели автомобиля (натуральное число, не превышающее 100 000),
его цена (натуральное число, не превышающее 10 000)
и статус (0, если автомобиль уже продан, и 1, если ещё не продан).
Выходные данные
Два числа: сумма выручки от реализации автомобиля — лидера продаж,
а также количество автомобилей этой модели, оставшееся в наличии."""
# 1. Количество проданных автомобилей модели (чем больше, тем лучше)
# 2. Цену модели (чем выше, тем лучше, если количество одинаково)
# 3. Количество оставшихся автомобилей (чем меньше, тем лучше, если количество и цена одинаковы)

f = open('files/26_22237.txt')
n = int(f.readline())
data = list(list(map(int, s.split())) for s in f)
# example
# n = 8
# data = [[10, 1_000_000, 1], [3, 100_000, 0], [10, 1_000_000, 0], [2, 100_000, 1], [10, 1_000_000, 0],
#         [3, 100_000, 1], [11, 1_000_000, 0], [1, 2_000_000, 0]]
# example2
# n = 8
# data = [[10, 1_000_000, 1], [10, 1_000_000, 1], [3, 100_000, 0], [10, 1_000_000, 0], [2, 100_000, 1],
#         [10, 1_000_000, 0], [3, 100_000, 1], [11, 1_000_000, 0], [11, 1_000_000, 0], [1, 2_000_000, 0],
#         [1, 2_000_000, 1], [1, 2_000_000, 1], [1, 2_000_000, 1], [1, 2_000_000, 1],
#         [12, 2_000_000, 0], [12, 2_000_000, 0], [12, 2_000_000, 0], [1, 2_000_000, 0], [1, 2_000_000, 0]]
middle_cost = sum(x[1] for x in data) / len(data)
premium = [x for x in data if x[1] > middle_cost]
print(premium)
celled = [x for x in premium if x[2] == 0]
print(celled)
mx_celled = max(celled.count(x) for x in premium)
leaders1 = [x for x in celled if celled.count(x) == mx_celled]
print(leaders1)
mx_cost = max(x[1] for x in leaders1)
leaders2 = [x for x in leaders1 if x[1] == mx_cost]
print(leaders2)
available = [x[0] for x in data if x[2] == 1]
print(available)
ceil_leader = max(x for x in available if x in [x[0] for x in leaders2])
print(ceil_leader)
ans1 = sum(x[1] for x in premium if x[0] == ceil_leader and x[2] == 0)
ans2 = len([x for x in premium if x[0] == ceil_leader and x[2] == 1])
print(ans1, ans2)  # 974760 25

# 27 №22238
from math import dist
from random import random
from turtle import *


def dbscan(points, eps):
    clusters = []
    while points:
        cluster = [points[0]]
        del points[0]
        for star in cluster:
            new = [point for point in points if dist(point, star) <= eps]
            cluster += new
            for point in new: points.remove(point)
        clusters.append(cluster)
    return clusters


def visual(clusters, k):
    up()
    tracer(0)
    for cluster in clusters:
        color = random(), random(), random()
        for x, y in cluster:
            goto(x * k, y * k)
            dot(5, color)
    update()
    done()


def get_centroid(cluster):
    res = []
    for star in cluster:
        res.append([sum(dist(star, point) for point in cluster), star])
    return min(res)[1]


points = [list(map(float, line.split())) for line in open('files/27B_22238.txt')]
clusters = dbscan(points, 1)
print([len(cluster) for cluster in clusters])
visual(clusters, 40)

centroids = [get_centroid(cluster) for cluster in clusters]
px = int(sum(x for x, y in centroids) / len(centroids) * 10000 // 1)
py = int(sum(y for x, y in centroids) / len(centroids) * 10000 // 1)
print(px, py)
# 47237 40080
# 29546 23047

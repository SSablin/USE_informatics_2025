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

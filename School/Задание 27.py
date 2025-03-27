# № 18150 (Уровень: Базовый)
"""clastersA = [[], []]

for s in open('files/27A_18150.txt'):
    x, y = [float(c) for c in s.split()]
    if x < -2 and y < -1:
        clastersA[0].append([x, y])
    else:
        clastersA[1].append([x, y])

print([len(kl) for kl in clastersA])

clastersB = [[], [], []]

for s in open('files/27B_18150.txt'):
    x, y = [float(c) for c in s.split()]
    if x < -2:
        clastersB[0].append([x, y])
    elif y > 5:
        clastersB[1].append([x, y])
    else:
        clastersB[2].append([x, y])

print([len(kl) for kl in clastersB])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]

pxA = sum(x for x, y in centerA) / 2 * 1000
pyA = sum(y for x, y in centerA) / 2 * 1000
print(int(pxA), int(pyA))  # -336 1859


pxB = sum(x for x, y in centerB) / 3 * 1000
pyB = sum(y for x, y in centerB) / 3 * 1000
print(int(pxB), int(pyB))  # 2467 1343"""

# № 18622 (Уровень: Базовый)

"""clastersA = [[], []]

for s in open('files/27A_18622.txt'):
    x, y = [float(c) for c in s.split()]
    if -1.5 <= x <= 0.5 and -1 <= y <= 2:
        clastersA[0].append([x, y])
    if 0 <= x <= 3 and 3 <= y <= 6:
        clastersA[1].append([x, y])

print([len(kl) for kl in clastersA])

clastersB = [[], [], [], []]

for s in open('files/27B_18622.txt'):
    x, y = [float(c) for c in s.split()]
    if x < 0.5 and y < 1.5:
        clastersB[0].append([x, y])
    if x > 3 and y < 1.5:
        clastersB[1].append([x, y])
    if x < 2.5 and y > 3:
        clastersB[2].append([x, y])
    if x > 4 and y > 5:
        clastersB[3].append([x, y])

print([len(kl) for kl in clastersB])


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p1, p) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]
print(centerA, centerB)

pxA = sum(x for x, y in centerA) / 2 * 10000
pyA = sum(y for x, y in centerA) / 2 * 10000
print(int(pxA), int(pyA)) # 4597 23685

pxB = sum(x for x, y in centerB) / 4 * 10000
pyB = sum(y for x, y in centerB) / 4 * 10000
print(int(pxB), int(pyB))  # 25450 24994"""

# № 19257 ЕГКР 21.12.24 (Уровень: Базовый)
"""clastersA = [[], []]
for s in open('files/27A_19257.txt'):
    x, y = [float(kl) for kl in s.split()]
    if -9 < x < -3 and -2 < y < 4:
        clastersA[0].append([x, y])
    if -6.5 < x < 0.5 and 10 < y < 16:
        clastersA[1].append([x, y])
print([len(kl) for kl in clastersA])


clastersB = [[], [], []]
for s in open('files/27B_19257.txt'):
    x, y = [float(kl) for kl in s.split()]
    if -6 < x < -2 and -1 < y < 4:
        clastersB[0].append([x, y])
    if 1 < x < 6 and 2 < y < 7:
        clastersB[1].append([x, y])
    if 2 < x < 7 and 8 < y < 13:
        clastersB[2].append([x, y])
print([len(kl) for kl in clastersB])
        

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]
print(centerA, centerB)


pxA = sum(x for x,y in centerA) / 2 * 10_000
pyA = sum(y for x,y in centerA) / 2 * 10_000
print(abs(int(pxA)), abs(int(pyA)))  # 43789 62202


pxB = sum(x for x,y in centerB) / 3 * 10_000
pyB = sum(y for x,y in centerB) / 3 * 10_000
print(abs(int(pxB)), abs(int(pyB)))  # 14271 54727"""

# № 18625 (Уровень: Сложный)
# SS
"""
clastersA = [[], []]

for s in open('files/27A_18625.txt'):
    x, y = [float(kl) for kl in s.split()]
    if (x < 3 and y > 5) or (x < 7 and 2 < y < 5):
        clastersA[0].append([x, y])
    if (x > 8 and 1.5 < y < 5) or (x > 3.5 and y > 5):
        clastersA[1].append([x, y])
print([len(kl) for kl in clastersA])  # [247, 246]

clastersB = [[], [], []]

for s in open('files/27B_18625.txt'):
    x, y = [float(kl) for kl in s.split()]
    if x > 1 and y > 5.3:
        clastersB[0].append([x, y])
    if (x < 2 and 2 < y < 5) or (x < 7 and y < 2):
        clastersB[1].append([x, y])
    elif 2 < x < 9.2 and (1.5 < y < 5.5):
        clastersB[2].append([x, y])
print([len(kl) for kl in clastersB])  # [3328, 3331, 3300]


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]
print(centerA, centerB)

pxA = sum(x for x, y in centerA) / 2 * 100_000
pyA = sum(y for x, y in centerA) / 2 * 100_000
print(int(pxA), int(pyA))  # 515933 498987

pxB = sum(x for x, y in centerB) / 3 * 100_000
pyB = sum(y for x, y in centerB) / 3 * 100_000
print(int(pxB), int(pyB))  # 471077 409201"""

# Кабанов
# Автоматическая кластеризация

"""data = []

for s in open('files/27A_18625.txt'):
    x, y = [float(c) for c in s.split()]
    data.append([x, y])
print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def getCluster(p):
    cluster = [p1 for p1 in data if dist(p, p1) < 1]
    if len(cluster) > 0:
        for p1 in cluster:
            data.remove(p1)
        next_cluster = [getCluster(p1) for p1 in cluster]
        for c in next_cluster:
            cluster.extend(c)
    return cluster


cluaters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    print(len(cluster))
    cluaters.append(cluster)

clusters = [kl for kl in cluaters if len(kl) > 10]


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centers = [center(kl) for kl in clusters]

px = sum(x for x, y in centers) / len(clusters)
py = sum(y for x, y in centers) / len(clusters)

print(int(px * 100_000), int(py * 100_000))
# file_A: 515933 498987
# file_B: 471077 409201"""

# kpolyakov 7584
# Кабанов
# DBSCAN

"""f = open('files/27_7584A.txt')

data = []
for s in f:
    s = s.replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append(p)

print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def getCluster(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    # В file_B меняем 1 на 0.2, т.к. там кластеры находятся на расстоянии < 1
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [getCluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    clusters.append(cluster)
    print(len(cluster))

K = len(clusters)


def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]


centroid = [center(kl) for kl in clusters]
print(centroid)

px = sum(x for x, y in centroid)
py = sum(y for x, y in centroid)
print(int(px / K * 10_000), int(py / K * 10_000))
# file_A: 32055 58097
# file_B: 31886 25834"""

# kpolyakov 7944
"""
clastersA = [[], []]

for s in open('files/27-7944A.txt'):
    x, y = [float(kl) for kl in s.replace(',', '.').split()]
    if x < 1 and y < 3:
        clastersA[0].append([x, y])
    else:
        clastersA[1].append([x, y])
print([len(kl) for kl in clastersA])  # [40, 56]

clastersB = [[], [], []]

for s in open('files/27-7944B.txt'):
    x, y = [float(kl) for kl in s.replace(',', '.').split()]
    if x < 2.5 and y < 3:
        clastersB[0].append([x, y])
    elif x > 5:
        clastersB[1].append([x, y])
    else:
        clastersB[2].append([x, y])
print([len(kl) for kl in clastersB])  # [3333, 3333, 6667]


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]
print(centerA, centerB)

pxA = sum(x for x, y in centerA) / 2 * 100_00
pyA = sum(y for x, y in centerA) / 2 * 100_00
print(int(pxA), int(pyA))  # file_A: 43789 62202

pxB = sum(x for x, y in centerB) / 3 * 10_000
pyB = sum(y for x, y in centerB) / 3 * 10_000
print(int(pxB), int(pyB))  # file_B: 14271 54727"""

# Автоматическое решение

"""f = open('files/27-7944B.txt')

data = []
for s in f:
    s = s.replace(',', '.')
    p = [float(c) for c in s.split()]
    data.append(p)

print(len(data))


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def getCluster(p0):
    cluster = [p for p in data if dist(p0, p) < 1]
    # В file_B меняем 1 на 0.2, т.к. там кластеры находятся на расстоянии < 1
    if len(cluster) > 0:
        for p in cluster: data.remove(p)
        next_cluster = [getCluster(p) for p in cluster]
        cluster = cluster + sum(next_cluster, [])
    return cluster


clusters = []
while len(data) > 0:
    p0 = data.pop()
    cluster = [p0] + getCluster(p0)
    clusters.append(cluster)
    print(len(cluster))

K = len(clusters)


def center(kl):
    m = []
    for p in kl:
        s = sum(dist(p, p1) for p1 in kl)
        m.append([s, p])
    return min(m)[1]


centroid = [center(kl) for kl in clusters]
print(centroid)

px = sum(x for x, y in centroid)
py = sum(y for x, y in centroid)
print(int(px / K * 10_000), int(py / K * 10_000))
# file_A: 10738 30730
# file_B: 37522 51277"""

# 18884
# Шастин
# https://youtu.be/U65my47LR-c?si=A8vl4T61mVjGZbUH&t=8020
"""from math import dist


def filial(cluster):
    min_s = float('inf')
    for p1 in cluster:
        s = 0
        for p2 in cluster:
            s += dist(p1, p2)
        if s < min_s:
            min_s = s
            fil = p1
    return fil


f = open('files/27_B_18884.txt')
data = [[int(x) for x in s.split()] for s in f]
clusters = []
while data:
    clusters.append([data.pop()])
    for el in clusters[-1]:
        for p in data[:]:
            if dist(el, p) < 20:
                clusters[-1].append(p)
                data.remove(p)

filials = [filial(c) for c in clusters]
sx = sum([x[0] for x in filials]) / len(filials)
sy = sum([x[1] for x in filials]) / len(filials)
print(int(sx), int(sy))
# A: 40 -30
# B: -19 -176
"""

# 27 №18390
"""from math import dist


def metoid(cluster):
    min_s = 10 ** 100
    for m in cluster:  # потенциальный метоид
        s = 0
        for p in cluster:  # все точки кластера
            s += dist(m, p)
        if s < min_s:
            min_s = s
            point = m
    return point


f = open('files/27_A_18390.txt')
r, k = map(float, f.readline().replace(',', '.').split())
data = [tuple(map(float, s.replace(',', '.').split())) for s in f]
data_cor = []  # список точек без аномалий
for p1 in data:
    for p2 in data:
        if p1 != p2:
            if dist(p1, p2) <= k:
                data_cor.append(p1)
                break

data_2 = data_cor.copy()
# DBSCAN
clusters = []
while data_cor:  # while len(data_cor) > 0
    clusters.append([data_cor.pop()])
    for p1 in clusters[-1]:
        for p2 in data_cor.copy():
            if dist(p1, p2) < r:
                clusters[-1].append(p2)
                data_cor.remove(p2)

metoids = [metoid(cl) for cl in clusters]

# определяем конечный метоид
min_s = 10 ** 100
for p in data_2:
    s = 0
    for m in metoids:
        s += dist(p, m)
    if s < min_s:
        min_s = s
        ans = p
print(int(ans[0] * 10_000), int(ans[1] * 10_000))
# A: 33923 51105
# B: 33732 37221"""

# 27 №20168
"""from math import dist


def get_centroid(c):
    r = []
    for p in c:
        r += [(sum(dist(p, p1) for p1 in c), p)]
    return min(r)[1]


a = [tuple(map(float, x.split())) for x in open('files/27_B_20168.txt')]
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a[:]:
            if dist(p1, p2) < 1:
                c[-1] += [p2]
                a.remove(p2)
print(len(c))
cs = [kl for kl in c if len(kl) >= 20]
cl = min(cs, key=len)
print(get_centroid(cl))
# A: 352342 343732
# B: 6446 857780"""

# 27 №18625
"""from math import dist


def get_centroid(c):
    r = []
    for p in c:
        r += [(sum(dist(p, p1) for p1 in c), p)]
    return min(r)[1]


a = [tuple(map(float, x.split())) for x in open('files/27B_18625.txt')]
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a[:]:
            if dist(p1, p2) < 1:
                c[-1] += [p2]
                a.remove(p2)
cs = [get_centroid(cl) for cl in c if len(cl) >= 30]

print(int(100_000 * sum(p[0] for p in cs) / len(cs)), int(100_000 * sum(p[1] for p in cs) / len(cs)))
# A: 515933 498987
# B: 471077 409201"""

# 27 №19647
# Шастин
"""from math import *


def centroid(cl):
    res = []
    for p1 in cl:
        s = sum([dist(p1, p2) for p2 in cl])
        res.append([s, p1])
    return min(res)[1]


def centr(cl, a):
    r = []
    for p in a:
        r.append((sum(dist(p, p1) for p1 in cl), p))
    return min(r)[1]


fA = open('files/27_A_19647.txt')
rA = float(fA.readline().strip().replace(',', '.'))
aA = [tuple(map(float, x.replace(',', '.').split())) for x in fA]
cA = [[], []]
for x, y in aA:
    if x < 4:
        cA[0].append([x, y])
    else:
        cA[1].append([x, y])
csA = [centroid(cl) for cl in cA]
print(csA)
print(*[10_000 * x for x in centr(csA, aA)])

fB = open('files/27_B_19647.txt')
rB = float(fB.readline().strip().replace(',', '.'))
aB = [tuple(map(float, x.replace(',', '.').split())) for x in fB]
cB = [[], [], []]
for x, y in aB:
    if x < 10.5:
        cB[0].append([x, y])
    elif y < 19:
        cB[1].append([x, y])
    else:
        cB[2].append([x, y])
csB = [centroid(cl) for cl in cB]
print(csB)
print(*[10_000 * x for x in centr(csB, aB)])
# A: 23392 26712
# B: 101947 210484"""

# 27 №19647
"""from math import dist
from turtle import *


def visual():
    up()
    tracer(0)
    for cluster, colour in zip(c, ('green', 'red', 'blue')):
        for x, y in cluster:
            goto(x * 50, y * 50)
            dot(3, colour)
    done()

def centroid(c):
    r = []
    for p in c:
        r.append((sum(dist(p, p1) for p1 in c), p))
    return min(r)[1]


def centr(c):
    r = []
    for p in a_2:
        r.append((sum(dist(p, p1) for p1 in c), p))
    return min(r)[1]


f = open('files/27_A_19647.txt')
r = float(f.readline().strip().replace(',', '.'))
a = [tuple(map(float, x.replace(',', '.').split())) for x in f]
a_2 = a.copy()
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a[:]:
            if dist(p1, p2) < r:
                c[-1] += [p2]
                a.remove(p2)
cs = [centroid(cl) for cl in c]
print(*[10_000 * x for x in centr(cs)])
# A: 23392 26712
# B: 101947 210484
visual()"""

# № 17882 Демоверсия 2025 (Уровень: Базовый)
# from Shastin's comments
# +20% speed boost
"""from math import dist

a = [list(map(float, x.split())) for x in open('files/27_A_17882.txt')]
c = []
while a:
    c += [[[0, a.pop()]]]
    for s, p1 in c[-1]:
        for p in a:
            if dist(p1, p) < 1:
                s = 0
                for n in c[-1]:
                    d = dist(p, n[1])
                    n[0] += d
                    s += d
                c[-1].append([s, p])
                a.remove(p)
cents = [min(c1) for c1 in c]
print(sum(c[1][0] for c in cents) / len(cents) * 10000, sum(c[1][1] for c in cents) / len(cents) * 10000)"""

# № 20497 (Уровень: Средний)
"""№ 20497 (Уровень: Средний)
(М. Попков) Учёный решил провести кластеризацию некоторого множества звёзд по их 
расположению на карте звёздного неба. Кластер звёзд – это набор звёзд (точек) на графике, 
лежащий внутри прямоугольника. Каждая звезда обязательно принадлежит только одному из кластеров.
Истинный край кластера – это одна из звёзд на графике, сумма расстояний от которой до 
всех остальных звёзд кластера максимальна."""
"""from math import dist


def krai(cl):
    r = []
    for p1 in cl:
        sm = sum(dist(p1, p2) for p2 in cl)
        r.append([sm, p1])
    return max(r)[1]


f = open('files/27.19.A_20497.txt')
a = [tuple(map(float, s.replace(',', '.').split())) for s in f]
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a.copy():
            if dist(p1, p2) < 0.5:  # A - 0.5 B - 4
                c[-1].append(p2)
                a.remove(p2)
cs = [krai(cl) for cl in c if len(cl) > 10]
print([len(cl) for cl in c])
print(len(cs))
px = sum(x for x, y in cs) / len(cs) * 10_000
py = sum(y for x, y in cs) / len(cs) * 10_000
print(int(px), int(py))
# A: 13258 2656
# B: -209434 474989"""

# 27 Горбачев5
"""from math import dist

data = [tuple(map(float, s.replace(',', '.').split())) for s in open('files/27B_горбачев5.txt')]

# DBSCAN
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data.copy():
            if dist(p1, p2) <= 1:
                clusters[-1].append(p2)
                data.remove(p2)
clusters = [cl for cl in clusters if len(cl) > 30]
print([len(cl) for cl in clusters])


def centroid(cl):
    r = []
    for p1 in cl:
        r.append([sum(dist(p1, p2) for p2 in cl), p1])
    return min(r)[1]


centr = [centroid(cl) for cl in clusters]
print(int(sum(x for x, y in centr) / len(centr) * 10000), int(sum(y for x, y in centr) / len(centr) * 10000))"""
# A: 15615 19452
# B: 2415 3237


# 27 шастин10
"""(Л. Шастин) Ведущие агрономы компании «Царство кленового сиропа» изучают качество земли в большом
кленовом саду. Перед ними стоит задача — проанализировать различные участки сада и сделать выводы о
наиболее плодородных местах для дальнейшей посадки новых деревьев, что позволит возрастить объемы
производства кленового сиропа. По итогам сбора информации имеется отчёт — набор данных, включающий
записи о позициях в саду, отмеченных агрономами. Каждая позиция характеризуется двумя вещественными
координатами, отражающими ее положение в декартовой системе координат. Специалисты включили в
отчет позиции двух видов: плодородные и неплодородные. Чтобы минимизировать количество
неприжившихся саженцев кленовых деревьев, решено, что нельзя сажать новые деревья в областях,
близлежащих к неплодородным позициям. Такие запретные области определяются как окружности с
радиусом R1 5, центрами которых являются неплодородные позиции. В конце концов необходимо
выделить области, подходящие для посадки, которые характеризуются как окружности с радиусом R2 7
с центрами, которые определяются ранее выделенными плодородными позициями. Среди таких областей
нужно найти оптимальную: такую, внутри которой находится наибольшее количество плодородных позиций
(разумеется, находящихся вне запретных областей). А если оптимальных областей несколько, выбрать
область с наибольшей суммой координат."""
"""from math import dist

f = open('files/27A_шастин10.txt')
n, k = [int(x) for x in f.readline().split()]
pl = [[float(x) for x in f.readline().split()] for _ in range(n)]
npl = [[float(x) for x in f.readline().split()] for _ in range(k)]
for zp in npl:
    for i in range(n):
        if pl[i] != -1 and dist(zp, pl[i]) <= 5:
            pl[i] = -1
pl = [p for p in pl if p != -1]
res = []
for p1 in pl:
    cnt = 0
    for p2 in pl:
        if dist(p1, p2) <= 7:
            cnt += 1
    res.append([cnt, sum(p1), p1])
x, y = sorted(res)[-1][-1]
print(x * 10**9, y * 10 ** 9)"""

# 20132
# В. Лашин
"""from math import dist

clasters = []
for point in open('files/27B_1_20132.txt'):
    point = list(map(float, point.replace(',', '.').split()))
    clasters.append([point])
    for claster in clasters[:-1]:
        if any(dist(point, claster_point) < 1 for claster_point in claster):
            clasters[-1] += claster
            clasters.remove(claster)


def extreme_point(claster_1, claster_2):
    distances = []
    for point_1 in claster_1:
        for point_2 in claster_2:
            distances.append([dist(point_1, point_2), [point_1, point_2]])
    return min(distances)[1]


extreme_points = [extreme_point(clasters[0], clasters[1]), extreme_point(clasters[0], clasters[2]),
                  extreme_point(clasters[1], clasters[2])]
# print(len(clasters))
print(abs(int(sum(p1[0] + p2[0] for p1, p2 in extreme_points) / (2 * len(extreme_points)) * 10000)), end=' ')
print(abs(int(sum(p1[1] + p2[1] for p1, p2 in extreme_points) / (2 * len(extreme_points)) * 10000)))
"""
# ОТ ХАОСА К ПОРЯДКУ | 27 ЗАДАНИЕ КЕГЭ
# https://vkvideo.ru/video-225440929_456239106
# Максим Попков
# 1
"""from math import dist

# file = open('files/27.1.A.txt')
# k1, k2 = [], []
# for line in file:
#     x, y = map(float, line.split())
#     if x > 2:
#         k2.append([x, y])
#     else:
#         k1.append([x, y])
file = open('files/27.1.B.txt')
k1, k2, k3 = [], [], []
for line in file:
    x, y = map(float, line.split())
    if x > 4:
        k2.append([x, y])
    elif y > 2:
        k1.append([x, y])
    else:
        k3.append([x, y])


def centr(cluster):
    min_sum_dist = float('inf')
    final_centroid = []
    for centroid in cluster:
        sum_dist = 0
        for point in cluster:
            sum_dist += dist(point, centroid)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            final_centroid = centroid
    return final_centroid


centroids = [centr(cluster) for cluster in [k1, k2, k3]]
px = int(sum(x for x, y in centroids) / len(centroids) * 10_000)
py = int(sum(y for x, y in centroids) / len(centroids) * 10_000)
print(px, py)
# 17314 11271
# 29257 21424"""

# 5
"""from math import dist

def center(cluster):
    min_sum_dist = float('inf')
    final_centroid = []
    for centroid in cluster:
        sum_dist = sum(dist(point, centroid) for point in cluster)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            final_centroid = centroid
    return final_centroid

file = open('files/27.5.A.txt')
# k1, k2, k3 = [], [], []
# for line in file:
#     x, y = map(float, line.split())
#     if x < 0.4:
#         k1.append([x, y])
#     elif y > 1:
#         k2.append([x, y])
#     else:
#         k3.append([x, y])
k1, k2, k3, k4, k5 = [], [], [], [], []
for line in file:
    x, y = map(float, line.split())
    if x > 5:
        k1.append([x, y])
    elif y < -1.2:
        k2.append([x, y])
    elif x < 0:
        k3.append([x, y])
    elif y > 3:
        k4.append([x, y])
    else:
        k5.append([x, y])

clusters = [k1, k2, k3, k4, k5]
clusters.sort(key=len)
del clusters[0]

centroids = [center(cluster) for cluster in clusters]
px = int(sum(x for x, y in centroids) / len(centroids) * 10_000)
py = int(sum(y for x, y in centroids) / len(centroids) * 10_000)
print(px, py)
# 5692 -11075
# 15394 4837"""


# 8
"""def dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
def kray(cluster):
    max_dum_dist = 0
    final_kray = []
    for kr in cluster:
        sum_dist = sum(dist(kr, point) for point in cluster)
        if sum_dist > max_dum_dist:
            max_dum_dist = sum_dist
            final_kray = kr
    return final_kray

# file = open('files/27.8.A.txt')
# k1, k2 = [], []
# for line in file:
#     x, y = map(float, line.split())
#     if x > 1.5:
#         k1.append([x, y])
#     else:
#         k2.append([x, y])
#
# kraya = [kray(cluster) for cluster in [k1, k2]]

file = open('files/27.8.B.txt')
k1, k2, k3 = [], [], []
for line in file:
    x, y = map(float, line.split())
    if y < -x - 4:
        k1.append([x, y])
    elif y < x + 4.8:
        k2.append([x, y])
    else:
        k3.append([x, y])

kraya = [kray(cluster) for cluster in [k1, k2, k3]]

tx = int(sum(x for x, y in kraya) / len(kraya) * 10_000)
ty = int(sum(y for x, y in kraya) / len(kraya) * 10_000)
print(tx, ty)
# 3071 -2558
# -40637 14149"""

# 10
"""from math import dist

def kray(cluster):
    max_sum_dist = 0
    final_kray = []
    for kr in cluster:
        sum_dist = sum(dist(kr, point) for point in cluster)
        if sum_dist > max_sum_dist:
            max_sum_dist = sum_dist
            final_kray = kr
    return final_kray

# file = open('files/27.10.A.txt')
# cl = [[] for i in range(3)]
# for line in file:
#     x, y = map(float, line.split())
#     if x > 0:
#         cl[0].append([x, y])
#     elif y > -1:
#         cl[1].append([x, y])
#     else:
#         cl[2].append([x, y])
file = open('files/27.10.B.txt')
cl = [[] for i in range(5)]
for line in file:
    x, y = map(float, line.split())
    if y > 1 and x < -2:
        cl[0].append([x, y])
    elif y > 1 and y > x + 0.4:
        cl[1].append([x, y])
    elif x > 1 and y > -2.4:
        cl[2].append([x, y])
    elif x > 1 and y < -2.4:
        cl[3].append([x, y])
    else:
        cl[4].append([x, y])

kraya = [kray(cluster) for cluster in cl]
tx = int(sum(x for x, y in kraya) / len(kraya) * 10000)
ty = int(sum(y for x, y in kraya) / len(kraya) * 10000)
print(tx, ty)
# -11053 -1583
# 1488 5057"""

# 15
"""from math import dist

def centr(cluster):
    min_sum_dist = float('inf')
    final_centroid = []
    for centroid in cluster:
        sum_dist = sum(dist(centroid, point) for point in cluster)
        if sum_dist < min_sum_dist:
            min_sum_dist = sum_dist
            final_centroid = centroid
    return final_centroid

# file = open('files/27.15.A.txt')
# cl = [[] for i in range(2)]
# anomaly = []
# for line in file:
#     x, y = map(float, line.split())
#     if (-2 < y < 2 and -4 < x < 4) or (-22 < y < -16 and -16 < x < -12) or (0 < y < 4 and 76 < x < 84):
#         anomaly.append([x, y])
#     elif y > 0:
#         cl[0].append([x, y])
#     else:
#         cl[1].append([x, y])

file = open('files/27.15.B.txt')
cl = [[] for i in range(8)]
anomaly = []
for line in file:
    x, y = map(float, line.split())
    if (y > 60 or (30 < y < 32 and 20 < x < 23) or (-1 < x < 1 and 2 < y < 6) or
            (-12 < y < -8 and 9 < x < 11) or (-12 < y < -8 and 26 < x < 28)):
        anomaly.append([x, y])
    elif y < -10:
        if x < 9.5:
            cl[0].append([x, y])
        else:
            cl[1].append([x, y])
    elif y < 6:
        if x > 13:
            cl[2].append([x, y])
        else:
            cl[3].append([x, y])
    elif y < 26:
        if x > 16.5:
            cl[4].append([x, y])
        else:
            cl[5].append([x, y])
    elif y < 40:
        cl[6].append([x, y])
    else:
        cl[7].append([x, y])

centroids = [centr(cluster) for cluster in cl]
px = int(sum(x for x, y in centroids) / len(centroids) * 10_000)
py = int(sum(y for x, y in centroids) / len(centroids) * 10_000)
print(px, py)
# 323977 -87831
# 131932 104997"""



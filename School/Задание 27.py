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
"""clastersA = [[], []]

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




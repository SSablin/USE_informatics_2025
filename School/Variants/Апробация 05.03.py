# 14 №20808
"""def i7(a):
    s = ''
    while a > 0:
        s = str(a % 7) + s
        a //= 7
    return s


m = 0
for x in range(1, 2031):
    a = 7 ** 170 + 7 ** 100 - x
    a7 = i7(a)
    m = max(m, a7.count('0'))
print(m)  # 73
for x in range(1, 2031):
    a = 7 ** 170 + 7 ** 100 - x
    a7 = i7(a)
    if a7.count('0') == 73:
        print(x)  # 1715"""
# 23 №17877
"""def f(x, end):
    if x == end: return 1
    if x < end: return 0
    if x > end:
        return f(x - 2, end) + f(x // 2, end)


print(f(38, 16) * f(16, 2))  # 36"""

# 24 №20813
"""from re import *

f = open('files/24_20813.txt').readline()
a = findall('(?:0|[7-9]\d*)(?:[-*](?:0|[7-9]\d*))+', f)
ans = max((str(x) for x in a), key=len)
print(len(ans), ans)  # 111"""

# 25 №20814
"""def r(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sum(s)


print(r(20))
for i in range(500_000, 501_000):
    if r(i) % 10 == 9:
        print(i, r(i))"""
# 500014 250009
# 500038 495289
# 500040 1170359
# 500054 250029
# 500058 667289

# 26 №20815
# Excel

# 27 №20816
"""from math import dist

clustersA = [[], []]
for s in open('files/27_A_20816.txt'):
    x, y = (float(t) for t in s.split())
    if x > 0:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], []]
for s in open('files/27_B_20816.txt'):
    x, y = (float(t) for t in s.split())
    if x < -5:
        clustersB[0].append([x, y])
    elif y > -3:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


def center(cl):
    r = []
    for p1 in cl:
        r.append([sum(dist(p1, p2) for p2 in cl), p1])
    return min(r)[1]


centerA = [center(cl) for cl in clustersA]
print(centerA)
centerB = [center(cl) for cl in clustersB]
print(centerB)

pxA = sum(x for x, y in centerA) / len(clustersA) * 10_000
pyA = sum(y for x, y in centerA) / len(clustersA) * 10_000
print(abs(int(pxA)), abs(int(pyA)))  # 10592 6300

pxB = sum(x for x, y in centerB) / len(clustersB) * 10_000
pyB = sum(y for x, y in centerB) / len(clustersB) * 10_000
print(abs(int(pxB)), abs(int(pyB)))  # 15981 37287"""

# DBSCAN
"""from math import dist


def centroid(cl):
    r = []
    for p in cl:
        r.append([sum(dist(p, p1) for p1 in cl), p])
    return min(r)[1]


f = open('files/27_B_20816.txt')
data = [list(map(float, x.split())) for x in f]
clusters = []
while data:
    clusters.append([data.pop()])
    for p in clusters[-1]:
        for p1 in data.copy():
            if dist(p, p1) < 2:
                clusters[-1].append(p1)
                data.remove(p1)
print([len(cl) for cl in clusters])  # 50 50
centroid = [centroid(cl) for cl in clusters]
print(int(abs(sum(cl[0] for cl in centroid) / len(clusters) * 10_000)))
print(int(abs(sum(cl[1] for cl in centroid) / len(clusters) * 10_000)))"""

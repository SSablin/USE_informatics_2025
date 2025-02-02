# 2 №18870
"""print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= z) <= w) or (not y)
                if not f:
                    print(x, y, z, w, f)"""

# x y z w F
# 0 1 0 0 False
# 0 1 1 0 False
# 1 1 1 0 False
# yzxw

# 3 №19029

# 5 №18941
"""for i in range(1000, 10000):
    n = str(i)
    n1 = eval(n[0] + '*' + n[1])
    n2 = eval(n[2] + '*' + n[3])
    r = str(min(n1, n2)) + str(max(n1, n2))
    if r == '5472':
        print(i)  # 6989
        break"""

# 6 №18871
"""from turtle import *
screensize(2000, 2000)
tracer(0)

lt(90)
c = 30

for i in range(2):
    fd(10*c)
    rt(90)
    fd(20*c)
    rt(90)
up()
bk(4*c)
rt(90)
fd(7*c)
lt(90)
down()
for i in range(4):
    fd(8*c)
    lt(90)
    fd(12*c)
    lt(90)
up()
fd(10*c)
down()
for i in range(4):
    fd(12*c)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'green')

exitonclick()
update()"""

# 8 №18942
"""from itertools import product

c = 0
for i in product(sorted(set('ДИОНИСИЙ')), repeat=6):
    s = ''.join(i)
    if ('Д' in s and 'Н' not in s) or ('Н' in s and 'Д' not in s):
        if sum(s.count(i+i) for i in s) == 0:
            c += 1
            print(s, c)
print(c)  # 8296"""

# 9 №18943

"""c = 0
for s in open('files/9_18943.txt'):
    a = [int(x) for x in s.split()]
    p3 = [int(x) for x in a if a.count(x) == 3]
    p2 = [int(x) for x in a if a.count(x) == 2]
    p1 = [int(x) for x in a if a.count(x) == 1]
    if len(p3) == 3 and len(p2) == 2 and len(p1) == 2:
        if p3[0] + p2[0] >= sum(p1):
            c += 1
print(c)   # 32"""

# 12 №18875
"""s = '8' * 140
while ('888' in s) or ('2222' in s):
    if '2222' in s:
        s = s.replace('2222', '88')
        # не ставим параметр 1, потому что нам нужно заменить все вхождения
    else:
        s = s.replace('888', '22')
print(s)  # 228228"""

# 13 №18955
# два адреса зарезервированны
"""from ipaddress import *

ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0')
for mask in range(32, -1, -1):
    net1 = ip_network(f'200.154.190.12/{mask}', 0)
    net2 = ip_network(f'200.154.184.0/{mask}', 0)
    if net1 == net2 and ip1 not in [net1[0], net1[-1]] and ip2 not in [net2[0], net2[-1]]:
        print(mask)  # 20"""

# 14 №18956
"""for a in range(1000000):
    for x in range(15):
        m = int(f'432{x}3', 15)
        n = int(f'86{x}86', 15)
        if (m + a) % n == 0:
            print(a)  # 212298
            break"""

# 15 №18877
"""for a in range(1, 300):
    f = 0
    for x in range(1, 300):
        for y in range(1, 300):
            if not((x < 7) or (y >= 5*x + a - 60) or (x >= 36) or (y < 225)):
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        print(a)  # 110"""

# 16 №17749
"""from sys import setrecursionlimit
setrecursionlimit(7000)

def f(n):
    if n > 7000:
        return n + 4
    if n <= 7000:
        return 3 * n + 5 + f(n + 3)

print(f(707) - f(716))  # 6405"""

# 23 №18959
"""def f(x, end):
    if x == end:
        return 1
    if x < end or x == 40:
        return 0
    if x > end:
        return f(x - 3, end) + f(x // 2, end) + f(x // 5, end)


print(f(120, 49) * f(49, 6))  # 40"""

# 24 №18530
# https://youtu.be/U65my47LR-c?si=ozowbjlOy_9haDK0&t=5636
# Шастин
"""s = 'A' + open('files/24_18530.txt').readline().strip().replace('E', 'A') + 'A'
ind = [i for i in range(len(s)) if s[i] == 'A']
i = 1
mx = 0
while i < len(ind) - 3:
    d = (ind[i + 2] - ind[i + 1]) - (ind[i + 1] - ind[i])
    l = ind[i + 1] - ind[i]
    start = i
    while ind[i + 1] - ind[i] == l:
        i += 1
        l += d
    mx = max(mx, ind[i + 1] - ind[start - 1] - 1)
    i -= 1
print(mx)  # 107831"""

# from comments
"""s = open('24.txt').readline()
a = [i for i, v in enumerate(s) if v in 'AE']
b = [a[i] - a[i - 1] for i in range(1, len(a))]
b = [b[i] - b[i - 1] for i in range(1, len(a) - 1)]
l = m = 0
for r in range(1, len(a) - 2):
    if b[r] == b[r - 1]:
        if l == 0:
            m = max(m, a[r + 3])
        elif r == len(a) - 3:
            m = max(m, len(s) - 1 - a[l - 1])
        else:
            m = max(m, a[r + 3] - a[l - 1] - 1)
    else:
        l = r

print(m)"""

# 25 №18962
"""from fnmatch import fnmatch

def div(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            if fnmatch(str(i), '2*3?'):
                s.add(i)
            if fnmatch(str(x // i), '2*3?'):
                s.add(x // i)
    return sorted(s)


c = 0
for i in range(500_000, 600_000):
    if c < 5:
        if len(div(i)) > 0:
            c += 1
            print(i, min(div(i)))
    else:
        break"""
# 500016 20834
# 500018 233
# 500020 230
# 500038 238
# 500040 20835

# 26
"""f = open('files/26_18967.txt')
n, k = [int(x) for x in f.readline().split()]
# n - общее кол-во мест, к - кол-во людей, которых нужно посмотреть
data = [[int(x) for x in s.split()] for s in f]
# ID, time, M - кол-во номерков
data.sort(key=lambda x: (x[1], x[0]))
# сортируем по времени подхода, если в одно время(совпадение), то по ID
visited = set()  # уже посетили
left = set()  # приходили, но покинули кинотеатр
top_top = time = 0
for i in range(len(data)):  # перебираем клиентов
    if data[i][0] not in visited:
        if n - data[i][2] >= 0:  # если есть место
            n -= data[i][2]
        else:
            top_top += data[i][2]
            left.add(data[i][0])
    else:
        if data[i][0] not in left:
            n += data[i][2]
    visited.add(data[i][0])  # отмечаем, что клиент обслужен
    if n == 0:  # не осталось свободного места в гардеробе
        time += data[i + 1][1] - data[i][1]
print(top_top, time)  # 5190 294"""

# 27

"""clustersA = [[], []]
for s in open('files/27_A_18884.txt'):
    x, y = [int(kl) for kl in s.split()]
    if -25 <= x <= 25 and -25 <= y <= 25:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

print([len(kl) for kl in clustersA])  # [901, 1217]

clustersB = [[], [], []]
for s in open('files/27_B_18884.txt'):
    x, y = [int(kl) for kl in s.split()]
    if x <= -200:
        clustersB[0].append([x, y])
    elif x >= 200:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])

print([len(kl) for kl in clustersB])  # [4018, 5025, 6416]


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clustersA]
centerB = [center(kl) for kl in clustersB]
print(centerA, centerB)
# [[0, 0], [80, -60]] 
# [[-410, -240], [351, -290], [0, 0]]
pxA = sum(x for x, y in centerA) / 2
pyA = sum(y for x, y in centerA) / 2
print(int(pxA), int(pyA))  # 40 -30
pxB = sum(x for x, y in centerB) / 3
pyB = sum(y for x, y in centerB) / 3
print(int(pxB), int(pyB))  # -19 -176"""

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

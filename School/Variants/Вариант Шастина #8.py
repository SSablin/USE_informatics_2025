# 2 №19637
"""from itertools import *


def f(x, y, w, z):
    return (z <= x) and ((x and (y == (not z))) <= w)


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    table = {(a1, 1, 1, a2), (0, 0, a3, a4), (a5, 0, 0, 0)}
    for p in permutations('xywz'):
        if [f(**dict(zip(p, r))) for r in table] == [0, 0, 0]:
            print(*p)  # z w y x"""

# 5 №19639
"""m = 0
for i in range(1, 1000):
    n = bin(i)[2:]
    if n.count('0') % 2 == 0:
        n = '1' + n + '1'
    else:
        n = '10' + n
    r = int(n, 2)
    if r < 100:
        m = max(m, r)
print(m)  # 97"""

# 8 №19480
"""from itertools import permutations

c = 0
for x in set(permutations('ПАРИЖАНКА')):
    s = ''.join(x).replace('И', 'А')
    if s.count('АА') == 1 and s.count('ААА') == 0:
        c += 1
        print(c, s)  # 28800"""

# 12 №19483
"""for n in range(4, 10_000):
    s = '2' + '5' * n
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '522', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    if s.count('2') == 10:
        print(n)  # 681
        break"""

# 13 №19843
"""from ipaddress import *
net = ip_network('158.214.121.40/255.255.255.224', 0)
for ip in net.hosts():
    print(str(ip).replace('.', ''))
    break  # 15821412133"""

# 14 №19484
"""def i27(x):
    s = []
    while x > 0:
        s.append(x % 27)
        x //= 27
    return s[::-1]


x = 5 * 729 ** 2024 + 3 * 243 ** 1413 - 7 * 81 ** 169 - 2 * 9 ** 107 + 3017
x7 = i27(x)
print(sum(x for x in x7 if x % 2 == 0 and x <= 25))  # 26"""

# 15 №19485
"""def DEL(n, m):
    if n % m == 0:
        return True
    return False


c = 0
B = [x for x in range(170, 221)]
for a in range(1, 500):
    f = True
    for x in range(1, 500):
        if not (DEL(x, a) or ((x in B) <= (not DEL(x, 24)))):
            f = False
            break
    if f:
        c += 1
print(c)  # 8"""

# 16 №19597
"""def f(n):
    if n < 15:
        return 4
    if n >= 15 and n % 3 == 0:
        return f(2 * n / 3) + n - 1
    elif n % 3 != 0:
        return f(n - 1) + 3

for n in range(10000):
    f(n)
    if f(n) == 251:
        print(n)  # 96"""

# 17 №19486
"""s = [int(x) for x in open('files/17_19486.txt')]

c_7 = sum(1 for x in s if abs(x) % 10 == 7)

ans = []
for i in range(len(s) - 1):
    if (s[i] == abs(s[i]) and s[i + 1] != abs(s[i + 1])) or (s[i] != abs(s[i]) and s[i + 1] == abs(s[i + 1])):
        if (s[i] + s[i + 1]) < c_7:
            ans.append(s[i] + s[i + 1])
print(len(ans), max(ans))  # 2452 962"""

# 23 №19487
"""def f(start, end, c):
    if start == 20:
        c += 1
    if start == 30:
        c += 1
    if start > end or c >= 2:
        return 0
    if start == end and c < 2:
        return 1
    if start < end:
        return f(start + 2, end, c) + f(start + 3, end, c) + f(start * 2, end, c)


print(f(8, 35, 0))  # 786"""
# 24 №19489
"""f = open('files/24_19489.txt').readline().strip()
m = 0
f = f.replace('WSFWW', 'WSFW SFWW')
for s in f.split():
    if len(s) > m:
        l = 0
        c_wwf = 0
        for r in range(2, len(s)):
            if s[r - 2] == 'W' and s[r - 1] == 'W' and s[r] == 'F':
                c_wwf += 1
            while c_wwf > 120:
                if s[l - 2] == 'W' and s[l - 1] == 'W' and s[l] == 'F':
                    c_wwf -= 1
                l += 1
            if c_wwf <= 120:
                m = max(m, r - l + 1)

print(m)  # 3080"""

# 25 №18591
"""from fnmatch import fnmatch
for i in range(1984, 10**10, 1984):
    if fnmatch(str(i), '?9?23?*23??'):
        if int(str(i)[0]) % 2 == 0 and int(str(i)[-2]) % 2 != 0 and int(str(i)[-1]) % 2 == 0:
            print(i, i // 1984)"""
# 2902302336 1462854
# 4912342336 2475979
# 6922382336 3489104
# 6932302336 3494104
# 8912332352 4492103
# 8942342336 4507229

# 26 №19599
"""from math import ceil
f = open('files/26_19599.txt')
n = int(f.readline())
data = []
for s in f:
    data.append(list(map(int, list(s.split()))))
for x in data:
    x[0] = x[0] - 1
    for j in range(2, 6):
        x[j] = x[j] - 1
data.sort()

# n power support opponets(3)
for i in range(n):
    if data[i][1] != 0:
        if data[data[i][2]][1] != 0:
            data[data[i][2]][1] += data[i][1]
        for j in range(3, 6):
            if data[data[i][j]][1] != 0:
                if data[i][1] > data[data[i][j]][1]:
                    data[data[i][j]][1] = 0
                    data[i][1] = ceil(data[i][1] - data[i][1] * 1/3)
                if data[i][1] == data[data[i][j]][1]:
                    data[i][1] = data[data[i][j]][1] = 0
                    break
                if data[i][1] < data[data[i][j]][1]:
                    data[i][1] = 0
                    data[data[i][j]][1] = ceil(data[data[i][j]][1] - data[data[i][j]][1] * 1/3)
                    break
            else:
                pass
c_killed = sum(1 for x in data if x[1] == 0)
max_p = max(x[1] for x in data if x[1] != 0)
print(c_killed, max_p)  # 4228 5962"""

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

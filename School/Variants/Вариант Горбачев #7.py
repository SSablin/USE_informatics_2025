# https://kompege.ru/variant?kim=25099988
# 2
print('x y z w F')
from itertools import product

for i in product(range(2), repeat=4):
    x, y, z, w = i
    f = ((not w) or y and x) and (not z) and x
    if f:
        print(x, y, z, w, f)
# x y w z
# 1 1 1 0
# 1 0 0 0
# 1 1 0 0

# 6
from turtle import *

tracer(0)
screensize(5000, 5000)

c = 40
for i in range(2):
    rt(30)
    fd(10 * c)
    rt(150)
    fd(20 * c)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * c, y * c)
        dot(3, 'green')
done()
# 80

# 7
from math import log2, ceil

N = 10_000
i = ceil(log2(N))
I = 1080 * 1920 * i * 30 + 2 * 48 * 8
t = (1238 * 1024 ** 2 * 8) / I
print(int(t))  # 11

# 11
from math import log2, ceil

for l in range(1, 10000):
    N = 10 + 26 + 230
    i = ceil(log2(N))
    if ceil(l * i / 8) * 1365 <= 2 * 1024 ** 2:
        print(l)  # 1365

# 13
from ipaddress import *

net = ip_network('131.159.219.0/255.252.0.0', False)
c = 0
for ip in net.hosts():
    b = format(ip, 'b')
    if b.count('1') % 7 == 0:
        c += 1
print(c)  # 34884


# 14
def si(x, i):
    s = []
    while x > 0:
        s.append(x % i)
        x //= i
    return s[::-1]


mx7 = 0
for x in range(33, 2034):
    s = 78 ** 378 - 5 ** x + 7 ** 61 - (50 + x)
    s19 = si(s, 19)
    if s19.count(7) >= mx7:
        mx7 = s19.count(7)
        print(x)  # 1017

# 15
mx = 0
for a in range(1, 400):
    a /= 4
    for b in range(int(a), 200):
        f = False
        for x in range(1, 200):
            P = 32 <= x <= 70
            Q = 63 <= x <= 108
            A = a <= x <= b
            if (Q <= P) and A:
                f = True
                break
        if not f:
            if (b - a) > mx:
                mx = (b - a)
                print(mx, a, b)
print(mx)
# (70; 108]
# 38

# 16
from sys import setrecursionlimit

setrecursionlimit(1000000)


def f(n):
    if n < 200:
        return n
    if n >= 200:
        return n * f(n - 1)


print((f(120240) - f(120238) // 9) // f(120239))  # 120239

# 23
from math import ceil


def f(x, end):
    if x == end:
        return 1
    if x < end or x == 29:
        return 0
    return f(x - 1, end) + f(x - 3, end) + f(ceil(x / 3), end)


print(f(61, 18) * f(18, 13))  # 13051416

# 24
from re import *

s = open('files/24_горбачев7.txt').readline()
numb = r'(?:0|[1-6][0-6]*)'
reg = rf'{numb}(\+{numb})*(\*{numb})*'
reg = rf'(?=({reg}))'
m = max((x.group(1) for x in finditer(reg, s)), key=len)
print(len(m))  # 37
print(m)


# 25
def R(x):
    s = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sum(s)


print(R(20))
# 42
c = 0
x = 800_000
while c < 6:
    if R(x) % 10 == 2:
        print(x, R(x))
        c += 1
    x -= 1
# 799991 799992
# 799988 1600032
# 799966 1199952
# 799961 799962
# 799956 2099552
# 799948 1407672

# 26
f = open('files/26_горбачев7.txt')
k = int(f.readline())
n = int(f.readline())
data = sorted(list(list(map(int, s.split())) for s in f))
# example
# k = 2
# n = 5
# data = [[30, 60], [40, 1110], [59, 60], [61, 120], [1230, 1440]]

camera = [-1 for _ in range(k)]
ans = [0, 0]
for st, end in data:
    for i in range(k - 1, -1, -1):
        if camera[i] + 1 <= st:
            camera[i] = end
            ans[1] = i + 1
            break
    else:
        ans[0] += 1
print(ans[0], ans[1])  # 419 152

# 27
from math import dist


def anticenter(cl):
    r = []
    for p1 in cl:
        r.append([sum(dist(p1, p2) for p2 in cl), p1])
    return max(r)[1]


f = open('files/27B_горбачев7.txt')
data = list(list(map(float, s.split())) for s in f)
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data.copy():
            if dist(p1, p2) <= 1:
                clusters[-1].append(p2)
                data.remove(p2)
print([len(cl) for cl in clusters])
clusters = [cl for cl in clusters if len(cl) >= 30]
anticentroid = [anticenter(cl) for cl in clusters]

Px = sum(x for x, y in anticentroid) / len(anticentroid) * 10_000
Py = sum(y for x, y in anticentroid) / len(anticentroid) * 10_000
print(Px, Py)
# A: 60025 32513
# B: 60831 40196

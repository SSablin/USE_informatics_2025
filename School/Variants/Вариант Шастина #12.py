# https://kompege.ru/variant?kim=25102234
# 1 №22602
# 13
# 2 №22513
from itertools import product

print('x y z w F')
for s in product(range(2), repeat=4):
    x, y, z, w = s
    F = ((z <= x) and (x <= y)) or (w == (z or x))
    if not F:
        print(x, y, z, w, F)
# wxyz
# 3 №22564
# 131755
# 4 №22513
# 31
# 5 №22456
mn = float('inf')
for i in range(1, 1000):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '11' + n[2:] + '1'
    else:
        if n.count('0') < n.count('1'):
            n += '0'
        else:
            n += '1'
    r = int(n, 2)
    if r > 271:
        mn = min(mn, i)
print(mn)  # 129

# 6 №22589
from turtle import *

tracer(0)
screensize(5000, 5000)
c = 30
lt(90)
rt(30)
for _ in range(18):
    fd(11 * c)
    rt(120)
    fd(11 * c)
    rt(60)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * c, y * c)
        dot(3, 'green')
update()
done()
# 104

# 7 №22598
for i in range(1000):
    S = 2 * 96_000 * (3 * 60 + 33) * i
    S_arch = S * 0.6
    if S_arch <= 25 * 1024 ** 2 * 8:
        print(i)  # 8

# 8 №22417
from itertools import product

c = 0
k = 0
for i in product(sorted('ЦИФЕРБЛАТ'), repeat=5):
    s = ''.join(i)
    c += 1
    if c % 2 != 0:
        if s[0] not in 'ИЕА' and s.count('Ц') == s.count('Ф'):
            k += 1
            print(s, k)  # 7454

# 9 №22546
f = open('files/9_22546.txt')
c = 0
for s in f:
    a = list(map(int, s.split()))
    various = [x for x in a if a.count(x) == 1]
    if various == a and (sorted(a)[0] * sorted(a)[1]) <= sum(sorted(a)[2:]):
        c += 1
        print(a, c)  # 1920

# 10 №22518
# 22

# 11 №22588
from math import ceil, log2

N = 10 + 26 * 2 + 70
i = ceil(log2(N))
s = ceil(18 * i / 8)
D = 100 * 1024 // 2000
print(D - s)
# 33

# 12 №22459
s = '3' * 234
while '33333' in s or '1111' in s:
    if '33333' in s:
        s = s.replace('33333', '111', 1)
    else:
        s = s.replace('111', '33', 1)
f = 1
for x in map(int, s):
    f *= x
print(s, f)  # 243

# 13 №22467
from ipaddress import *

ip = ip_address('192.214.116.184')
c = 0
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    b = f'{net.network_address:b}'
    if b.count('1') % 5 == 0:
        if net[0] < ip < net[-1]:
            c += 1
print(c)  # 5

# 14 №22427
for x in '0123456789ABCD':
    a = int(f'4B3{x}1C7', 14) + int(f'5{x}G83F7', 17)
    if a % 15 == 0:
        print(a // 15)  # 11401190
        break

# 15 №22433
for a in range(1000):
    f = True
    for x in range(1000):
        if not (((x & 117 != 0) and (x & 91 == 0)) <= (not (x & a == 0))):
            f = False
            break
    if f:
        print(a)  # 36
        break
# 16 №22558
f = {}
for n in range(1, 180001):
    if n < 1000:
        f[n] = 66
    else:
        f[n] = f[n - 5] + 100
print(f[180_000] - f[100_000])  # 1600000

# 17 №22468
s = [int(x) for x in open('files/17_22468.txt')]
sr_arif = sum(s) / len(s)
ans = []
for i in range(len(s) - 1):
    if abs(sum(s[i:i + 2])) > sr_arif:
        ans.append(sum(s[i:i + 2]))
print(len(ans), abs(min(ans)))  # 33368 198129


# 18 №22593
# 1755 574

# 19 №22473
def g(s, h):
    if s >= 471 and h == 2:
        return True
    if s < 471 and h == 2:
        return False
    if s >= 471 and h != 2:
        return False
    if h % 2 != 0:
        return g(s + 4, h + 1) or g(s + 7, h + 1) or g(s * 4, h + 1)
    else:
        return g(s + 4, h + 1) and g(s + 7, h + 1) and g(s * 4, h + 1)


for s in range(1, 471):
    if g(s, 0):  # 114, 115, 116, 117
        print(s)  # 4


# 20 №22473
def g(s, h):
    if s >= 471 and h == 3:
        return True
    if s < 471 and h == 3:
        return False
    if s >= 471 and h != 3:
        return False
    if h % 2 != 0:
        return g(s + 4, h + 1) and g(s + 7, h + 1) and g(s * 4, h + 1)
    else:
        return g(s + 4, h + 1) or g(s + 7, h + 1) or g(s * 4, h + 1)


for s in range(1, 471):
    if g(s, 0):
        print(s)  # 29 113

# 21 №22473
sm = []


def g(s, h):
    if s >= 471 and (h == 2 or h == 4):
        return True
    if s < 471 and h == 4:
        return False
    if s >= 471 and h != 2 and h != 4:
        return False
    if h % 2 != 0:
        return g(s + 4, h + 1) or g(s + 7, h + 1) or g(s * 4, h + 1)
    else:
        return g(s + 4, h + 1) and g(s + 7, h + 1) and g(s * 4, h + 1)


for s in range(1, 471):
    if g(s, 0):
        sm.append(s)
print(sm)  # [103, 104, 105, 106, 114, 115, 116, 117]
sm = [103, 104, 105, 106]
print(sm)
print(sum(sm))  # 418


# 22 №22613
# 8

# 23 №22451
def f(x, end):
    if x == end:
        return True
    if x > end or x == 27:
        return False
    if x < end:
        return f(x + 3, end) + f(x + 5, end) + f(x ** 2, end)


print(f(3, 16) * f(16, 51))  # 225

# 24 №22446
s = open('files/24_22446.txt').readline()
l, c = 0, 0
mx = 0
for r in range(2, len(s)):
    if s[r - 2:r + 1] == 'LND':
        c += 1
    while c > 10000:
        if s[l:l + 3] == 'LND':
            c -= 1
        l += 1
    for l1 in range(l, r):
        if s[l1] == s[r]:
            mx = max(mx, r - l1 + 1)
            break
print(mx)  # 830019


# 25 №22430
def d(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sorted(s)


c = 0
x = 456_789
while c < 5:
    div = d(x)
    prime_div = [t for t in div if len(d(t)) == 0]
    if len(prime_div) >= 4:
        M = prime_div[0] + prime_div[1] + prime_div[-1] + prime_div[-2]
        if M % 114 == 39:
            print(x, M)
            c += 1
    x += 1
# 457366 381
# 457512 1749
# 457638 951
# 457722 495
# 457786 1749

# 26 №22605
f = open('files/26_22605.txt')
n = int(f.readline())

# f = ['2 3 10', '1 1 3', '2 3 15', '3 2 20', '1 1 10', '2 3 17', '1 1 6']
# n = 7

data = [list(map(int, s.split())) for s in f]
# x y t
data.sort(reverse=True)
# print(data)
data2 = [[data[0]]]
for i in range(1, n):
    if data[i][:2] == data2[-1][-1][:2]:
        data2[-1].append(data[i])
    else:
        data2.append([data[i]])
# print(data2)
mn = float('inf')
sm_k = 0
for i in range(len(data2)):
    for j in range(len(data2[i]) - 1):
        if data2[i][j][2] - data2[i][j + 1][2] <= mn:
            mn = data2[i][j][2] - data2[i][j + 1][2]
            sm_k = data2[i][j][0] + data2[i][j][1]
            print(data[i][j], sm_k, mn)
print(sm_k, mn)  # 4552 53

# 27 №22623
from math import dist
from random import random
from turtle import *

f = open('files/27B_22623.txt')
data = [list(map(float, s.split())) for s in f]


def dbscan(data, r):
    cl = []
    while data:
        cl.append([data.pop()])
        for p1 in cl[-1]:
            for p2 in data[:]:
                if dist(p1, p2) < r:
                    cl[-1].append(p2)
                    data.remove(p2)
    return cl


def visual(cl, k):
    up()
    tracer(0)
    for c in cl:
        color = random(), random(), random()
        for x, y in c:
            goto(x * k, y * k)
            dot(5, color)
    update()
    done()


def center(c):
    r = []
    for p in c:
        r.append([sum(dist(p, p1) for p1 in c), p])
    return min(r)[1]


def density(c):
    return len(c) / (4 * 4)


cl = dbscan(data, 2)
print([len(c) for c in cl])
# visual(cl, 10)
Ps = sum(density(c) for c in cl) / len(cl)
density_center = [[density(c), center(c)] for c in cl]
Sp = dist(max(density_center)[1], min(density_center)[1])
print(int(Ps * 1000 // 1), int(Sp * 1000 // 1))
# 14125 16165
# 92237 24500

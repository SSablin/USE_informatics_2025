# 2 №21403
"""from itertools import product
print('x y z w F')
for x, y, z, w in product(range(2), repeat=4):
    f = x and (z <= w) and (not y)
    if f:
        print(x, y, z, w, f)
# xwzy"""

# 5 №21404
"""for i in range(300):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    r = int(n, 2)
    if r > 480:
        print(i)  # 176
        break"""

# 6 №21405
"""from turtle import *
tracer(0)
screensize(3000, 3000)
c = 50
lt(90)

rt(30)
for i in range(3):
    rt(150)
    fd(6 * c)
    rt(30)
    fd(12 * c)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*c, y*c)
        dot(3, 'green')
done()
# 30"""

# 7 №21406
"""x = 3840
y = 2160
i = 17
I = x * y * i
x2 = 1280
y2 = 720
i2 = 5
I2 = x2 * y2 * i2
print((I - I2) * 120 / 8 / 1024)
# 1998000"""

# 8 №21407
"""from itertools import product
c = 0
for i in product('ДГИАШЭ', repeat=5):
    s = ''.join(i)
    if s[0] not in 'ИАЭ' and s[-1] not in 'ДГШ':
        c += 1
        print(s)
print(c)  # 1944"""

# 9 №21408
"""c = 0
for s in open('files/9_21408.txt'):
    a = [int(x) for x in s.split()]
    pov = {x for x in a if a.count(x) == 3}
    npov = [x for x in a if a.count(x) == 1]
    if len(pov) == 2 and len(npov) == 1:
        if max(pov) > npov[0]:
            c += 1
            print(c, a, pov, npov)  # 1"""

# 11 №21410
"""num = (33 * 1024 * 1024) // 295_740  # 117
i = (num * 8) // 257  # 3
print(2**i)  # 8"""

# 12 №21411
"""for n in range(4, 10_000):
    s = '3' + '1' * n
    while '31' in s or '211' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '211' in s:
            s = s.replace('211', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '2', 1)
    if sum(int(x) for x in s) == 15:
        print(n)  # 50
        break"""

# 13 №21412
"""from ipaddress import *
net = ip_network('143.168.72.213/255.255.255.240', 0)
for ip in net.hosts():
    print(str(ip).replace('.', ''))
# 14316872222"""

# 14 №21413
"""from string import digits, ascii_uppercase
for x in (digits + ascii_uppercase)[:21]:
    a = int(f'82934{x}2', 21) + int(f'2924{x}{x}7', 21) + int(f'67564{x}8', 21)
    if a % 20 == 0:
        print(a // 20)  # 3
        break"""

# 15 №21414
"""for a in range(10000):
    f = True
    for x in range(10000):
        for y in range(10000):
            if not ((5 < y) or (x > 32) or (x + 2 * y < a)):
                f = False
                break
        if not f:
            break
    if f:
        print(a)  # 43
        break"""

# 16 №21415
"""from sys import setrecursionlimit
setrecursionlimit(10_000)
def f(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + f(n - 2)


print(f(2126) - f(2122))  # 4250"""

# 17 №21416
"""s = [int(x) for x in open('files/17_21416.txt')]
sm = sum(x for x in s if x < 0)

ans = []
for i in range(len(s) - 2):
    if max(s[i:i+3]) * min(s[i:i+3]) > sm:
       ans.append(sum(s[i:i+3]))
print(len(ans), abs(max(ans)))  # 10007 7953"""

# 19 №21418
"""def g(s, h):
    if s <= 87 and h == 2:
        return True
    if s <= 87 and h != 2:
        return False
    if s > 87 and h == 2:
        return False

    if h % 2 != 0:  # Петя
        return g(s - 2, h + 1) or g(s // 2, h + 1)
    else:  # Ваня
        return g(s - 2, h + 1) and g(s // 2, h + 1)


for s in range(89, 500):
    if g(s, 0):
        print(s)  # 176
        break"""

# 20
"""def g(s, h):
    if s <= 87 and h == 3:
        return True
    if s <= 87 and h != 3:
        return False
    if s > 87 and h == 3:
        return False

    if h % 2 != 0:  # Петя
        return g(s - 2, h + 1) and g(s // 2, h + 1)
    else:  # Ваня
        return g(s - 2, h + 1) or g(s // 2, h + 1)


for s in range(89, 500):
    if g(s, 0):
        print(s)  # 178 179"""

# 21
"""def g(s, h):
    if s <= 87 and (h == 4 or h == 2):
        return True
    if s <= 87 and (h != 4 and h != 2):
        return False
    if s > 87 and h == 4:
        return False

    if h % 2 != 0:  # Петя
        return g(s - 2, h + 1) or g(s // 2, h + 1)
    else:  # Ваня
        return g(s - 2, h + 1) and g(s // 2, h + 1)


for s in range(89, 500):
    if g(s, 0):
        print(s)  # 180"""

# 23 №21420
"""def f(x, end):
    if x == end:
        return True
    if x > end or x == 35:
        return False
    if x < end:
        return f(x + 1, end) + f(x + 2, end) + f(x * 2, end)


print(f(7, 13) * f(13, 15) * f(15, 51))
# 174034068"""

# 24 №21421
"""from re import *
s = open('files/24_21421.txt').readline()
expr = findall(f'(?:[1-9, AB][0-9, AB]*)', s)
ans = max([x for x in expr if int(x, 12) % 2 == 0], key=len)
print(len(ans), ans)  # 19"""

# 25 №21422
"""c = 0
while c < 5:
    for x in range(1_125_000, 2_000_000):
        if c < 5:
            for i in range(1, x):
                if x % i == 0 and i % 10 == 7 and i != 7:
                    print(x, i)
                    c += 1
                    break
# 1125003 467
# 1125006 97
# 1125009 17
# 1125011 3187
# 1125012 177"""

# 26 №21424
"""f = open('files/26_21424.txt')
n = int(f.readline())
data = sorted(list(map(int, f.readlines())))

boxes = [0]
for i in range(len(data)):
    if data[i] - boxes[-1] >= 9:
        boxes.append(data[i])
print(boxes)  # 1040
print(len(boxes) - 1)
x = 50
boxes1 = boxes[1:]
while len(boxes1) == 1040:
    x += 1
    boxes = [x]
    for i in range(len(data)):
        if data[i] - boxes[-1] >= 9:
            boxes.append(data[i])
    boxes1 = boxes
print(x - 1)  # 57"""

# 27 №21425
"""from math import dist

clustersA = [[], []]

for s in open('files/27_A_21425.txt'):
    x, y = (float(kl) for kl in s.replace(',', '.').split())
    if x < 15:
        clustersA[0].append([x, y])
    else:
        clustersA[1].append([x, y])

clustersB = [[], [], []]

for s in open('files/27_B_21425.txt'):
    x, y = (float(kl) for kl in s.replace(',', '.').split())
    if x < 0:
        clustersB[0].append([x, y])
    elif y > 0:
        clustersB[1].append([x, y])
    else:
        clustersB[2].append([x, y])


def center(cl):
    r = []
    for p1 in cl:
        r.append([sum(dist(p1, p2) for p2 in cl), p1])
    return min(r)[1]


centerA = [center(cl) for cl in clustersA]
centerB = [center(cl) for cl in clustersB]

pxA = sum(x for x, y in centerA) / 2 * 10_000
pyA = sum(y for x, y in centerA) / 2 * 10_000
print(int(pxA), int(pyA))  # 167990 73043
pxB = sum(x for x, y in centerB) / 3 * 10_000
pyB = sum(y for x, y in centerB) / 3 * 10_000
print(int(pxB), int(pyB))  # 122627 29105"""

# 5 №18287
"""for i in range(1000):
    n = bin(i)[2:]
    if len(n) % 2 == 0:
        n += '1'
    else:
        n = '1' + n + '0'

    r = int(n, 2)
    if r > 666:
        print(r)  # 1536
        break"""

# 6
"""from turtle import *
tracer(0)
screensize(5000, 5000)

c = 30
lt(90)

for i in range(5):
    fd(15 * c)
    lt(90)
    fd(25 * c)
    lt(90)

up()

fd(4 * c)
lt(90)
fd(12 * c)
lt(90)

down()

for i in range(6):
    fd(38 * c)
    rt(90)
    fd(22 * c)
    rt(90)

up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x * c, y * c)
        dot(3, 'green')

exitonclick()
update()"""
# print((13 + 4) * 2)  # 34
# 8 №18260
"""from itertools import product
c = 0
for x in product((str(x) for x in range(12)), repeat=6):
    if x[0] != '0' and sum(1 for i in x if int(i) % 2 == 0) == sum(1 for i in x if int(i) % 2 != 0) and x.count('11') == 1:
        c += 1
        print(c, x)"""

# 9 №18258
"""
f = open('files/9_18258.txt')
c = 0
for s in f:
    c += 1
    a = list(map(int, s.split()))
    ap = [int(x) for x in a if a.count(x) > 1]
    a2 = [1 for x in ap if sum(int(j) for j in str(x)) % 2 == 0]
    if a == sorted(a):
        if sum(a2) > 1:
            print(c, a)  # 6937"""

# 12
"""for n in range(50):
    s = '>' + '0' * 17 + '3' * n + '2' * 17
    while ('>3' in s) or ('>2' in s) or ('>0' in s):
        if '>3' in s:
            s = s.replace('>3', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '3>', 1)
    if int((sum(int(x) for x in s[:-1])) ** 0.5) == (sum(int(x) for x in s[:-1])) ** 0.5:
        print(n)  # 9
        break"""
# 13
"""from ipaddress import *
ip = ip_address('222.190.122.24')
for mask in range(1, 33):
    net = ip_network(f'{ip}/{mask}', 0)
    if '222.190.120.0' == str(net.network_address):
        print(net.num_addresses - 3)  # 2045"""
# 14
"""from string import digits, ascii_uppercase
for p in range(4, 37):
    for s in range(2, 35):
        try:
            if int('R4', p-1) + int('B0', s+2) + int('T3NK4', p) == 23593399:
                print(p * s)  # 780
        except:
            pass"""

"""for a in range(1000):
    f = True
    for x in range(1000):
        if not ((x & 57 == 0) or ((x & 23 == 0) <= (not (x & a == 0)))):
            f = False
            break
    if f:
        print(a)  # 40
        break"""

"""from sys import setrecursionlimit
setrecursionlimit(5000)
def f(n):
    if n < 10:
        return n - 1
    if n >= 10 and n % 2 == 0:
        return 3 * n - 1 + f(n - 3)
    elif n % 2 != 0:
        return 5 * n + 2 + f(n - 4)

print(f(4445) - f(4444))  # 8896"""

# 17 №18257

"""s = [int(x) for x in open('files/17_18257.txt')]

mx = max(s)

ans = []
for i in range(len(s)):
    if ((i + 1) + (i + 2)) % 10 == mx % 10:
        ans.append(abs((s[i] + s[i+1]) - (i + 1) + (i + 2)))

print(len(ans), min(ans))  # 1000 811"""

# 19 №18268
"""from math import ceil


def g(s1, s2, h):
    if s1 + s2 <= 72 and h == 3:
        return True
    if s1 + s2 <= 72 and h != 3:
        return False
    if s1 + s2 > 72 and h == 3:
        return False

    if h % 2 == 0:
        return g(s1 - 3, s2, h + 1) or g(s1, s2 - 3, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2),
                                                                                               h + 1)
    else:
        return g(s1 - 3, s2, h + 1) or g(s1, s2 - 3, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2),
                                                                                               h + 1)


for s2 in range(22, 500):
    if g(50, s2, 1):
        print(s2)  # 94"""

# 20
"""from math import ceil


def g(s1, s2, h):
    if s1 + s2 <= 72 and h == 4:
        return True
    if s1 + s2 <= 72 and h != 4:
        return False
    if s1 + s2 > 72 and h == 4:
        return False

    if h % 2 == 0:
        return g(s1 - 3, s2, h + 1) and g(s1, s2 - 3, h + 1) and g(ceil(s1 / 2), s2, h + 1) and g(s1, ceil(s2 / 2),
                                                                                                  h + 1)
    else:
        return g(s1 - 3, s2, h + 1) or g(s1, s2 - 3, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2),
                                                                                               h + 1)


for s2 in range(22, 1000):
    if g(50, s2, 1):
        print(s2)  # 51 100"""

# 21
"""from math import ceil


def g(s1, s2, h):
    if s1 + s2 <= 72 and (h == 3 or h == 5):
        return True
    if s1 + s2 <= 72 and (h != 3 and h != 5):
        return False
    if s1 + s2 > 72 and h == 5:
        return False

    if h % 2 == 0:
        return g(s1 - 3, s2, h + 1) or g(s1, s2 - 3, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2),
                                                                                               h + 1)
    else:
        return g(s1 - 3, s2, h + 1) and g(s1, s2 - 3, h + 1) and g(ceil(s1 / 2), s2, h + 1) and g(s1, ceil(s2 / 2),
                                                                                                  h + 1)


for s2 in range(22, 500):
    if g(50, s2, 1):
        print(s2)  # 103"""

# 23 №18267
"""def f(x, end):
    if x == end:
        return True
    if x > end:
        return False
    if x < end:
        return f(x + 2, end) + f(x + 5, end) + f(x ** 2, end)


print(f(5, 25) * f(25, 30) * f(30, 32))  # 24"""

# 24
# регулярки
"""from re import findall
s = open('files/24_18285.txt').readline().strip()

expr = findall('(?:0|[1-9]\d*)(?:[*+](?:0|[1-9]\d*))*', s)
ans = (max((str(x) for x in expr), key=len)).replace('+', '*')

ans = set(ans.split('*'))

print(len(ans), ans)  # 44"""

# 25 №18298
"""from fnmatch import fnmatch

for i in range(1996, 10 ** 10, 1996):
    if fnmatch(str(i), '1592*6?8') and all(int(x) % 2 == 0 for x in str(i)[4:-3]):
        print(i, i // 1996)"""
# 1592464688 797828
# 1592484648 797838

# 26 №18228

f = open('files/26_18228.txt')
n, r = f.readline().split()  # кол-во балок для покупки # длина одной платформы
# 9876 # 40000400004
data = []
for i in range(len(n)):
    s = f.readline()
    data.append(list(map(int, s.split())))


# 2
"""print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (((not x) and y and z and (not w)) or
                     ((not x) and y and (not z) and w) or
                     (x and y and z and (not w)))
                if f:
                    print(x, y, z, w, f)"""

# 5
"""def tr(x, i):
    s = ''
    while x > 0:
        s += str(x % i)
        x //= i
    return s[::-1]

mx_r = 0
for i in range(1, 1000):
    n = tr(i, 7)
    if n.count('3') % 2 == 0:
        n = '3' + n + n[0]
    else:
        n = '6' + n + n[-1]
    r = int(n, 7)
    if r < 16777:
        mx_r = max(mx_r, r)
print(mx_r)   # 16733"""

# 6
"""from turtle import *
tracer(0)
screensize(5000, 5000)
c = 50

for i in range(4):
    lt(45)
    fd(5 * c)
    lt(45)
    fd(6 * c)
up()

for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*c, y*c)
        dot(3, 'green')

done()
# 145"""

# 8
"""from itertools import product
c = 0
for x in product('0123456789ABC', repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        if all(s.count(i) == 1 for i in s):
            if all(s.count(f'{a}{b}') == 0 for a in '02468AC' for b in '02468AC'):
                if all(s.count(f'{a}{b}') == 0 for a in '13579B' for b in '13579B'):
                    c += 1
                    print(s)
print(c)  # 10440"""
# 9
"""c = 0
for s in open('files/9_горбачев6.txt'):
    a = list(map(int, s.split()))
    pov = [x for x in a if a.count(x) > 1]
    nepov = [x for x in a if a.count(x) == 1]
    if len(pov) == 3 or min(a) in pov:
        c += 1
        print(a)
print(c)  # 437"""

# 10
# 165

# 12
"""res = []
for a in range(1, 100):
    for b in range(1, 100):
        for c in range(1, 100):
            s = '7' * a + '8' * b + '9' * c
            while '78' in s or '98' in s or '999' in s:
                if '78' in s:
                    s = s.replace('78', '8', 1)
                if '98' in s:
                    s = s.replace('98', '7', 1)
                if '999' in s:
                    s = s.replace('999', '9', 1)
            if sum(int(x) for x in s) == 801:
                res.append(a+b+c)
print(min(res))  # 101"""
# 13
"""from ipaddress import *
for a in range(256):
    net = ip_network(f'135.{a}.170.5/255.255.0.0', 0)
    if all((format(ip, 'b')[:16].count('1') > 10) for ip in net):
        print(a)  # 127"""

# 14
"""def tr(x, i):
    s = []
    while x > 0:
        s.append(x % i)
        x //= i
    return s[::-1]


x = 9 * 57 ** 2024 + 14 * 13 ** 3059 - 87 * 67 ** 1111 + 2027
x_36 = tr(x, 36)
print(x_36)
b_20 = [int(x) for x in x_36 if x > 20]
print(len(b_20))  # 931"""

# 15
"""def f(x):
    P = 3 <= x <= 83
    Q = 62 <= x <= 131
    A = a1 <= x <= a2
    return (not Q) <= (((not A) and P) <= Q)

ox = [i/4 for i in range(1*4, 133*4)]
res = []

for a1 in ox:
    for a2 in ox:
        if all(f(x) == 1 for x in ox):
            res.append(a2 - a1)
print(min(res))  # 59"""

# 16
"""from functools import lru_cache
@lru_cache(None)
def f(n):
    if n < 52:
        return n
    if n >= 52:
        return 3 * f(n - 2) - n

for n in range(15200):
    f(n)

print(f(15127) // f(15099))  # 4782968"""

# 17
"""s = [int(x) for x in open('files/17_горбачев6.txt')]

mn_7 = float('inf')
for x in s:
    if x % 7 == 0 and abs(x) % 10 == 7:
        mn_7 = min(mn_7, x)

ans = []
for i in range(len(s) - 1):
    if len(str(abs(s[i]))) == 3 or len(str(abs(s[i + 1]))) == 3:
        if (s[i] + s[i + 1]) > mn_7:
            ans.append(s[i] ** 2 + s[i+1] ** 2)
print(len(ans), max(ans))  # 3174 9955651250"""


# 19
"""def g(s1, s2, h, p):
    if s1 + s2 >= 132 and h == 2:
        return True
    if s1 + s2 >= 132 and h != 2:
        return False
    if s1 + s2 < 132 and h == 2:
        return False
    if p < 1:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p) or
                    g(s1 * 3, s2, h + 1, 1) or g(s1, s2 * 3, h + 1, 1))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p) and
                    g(s1 * 3, s2, h + 1, 1) and g(s1, s2 * 3, h + 1, 1))
    else:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p))


for s in range(1, 101):
    if g(31, s, 0, 0):
        print(s)  # 33"""

# 20
"""def g(s1, s2, h, p):
    if s1 + s2 >= 132 and h == 3:
        return True
    if s1 + s2 >= 132 and h != 3:
        return False
    if s1 + s2 < 132 and h == 3:
        return False
    if p < 1:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p) and
                    g(s1 * 3, s2, h + 1, 1) and g(s1, s2 * 3, h + 1, 1))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p) or
                    g(s1 * 3, s2, h + 1, 1) or g(s1, s2 * 3, h + 1, 1))
    else:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p))


for s in range(100, 0, -1):
    if g(31, s, 0, 0):
        print(s)  # 32 31"""

# 21
"""def g(s1, s2, h, p):
    if s1 + s2 >= 132 and (h == 2 or h == 4):
        return True
    if s1 + s2 >= 132 and (h != 2 and h != 4):
        return False
    if s1 + s2 < 132 and h == 4:
        return False
    if p < 1:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p) or
                    g(s1 * 3, s2, h + 1, 1) or g(s1, s2 * 3, h + 1, 1))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p) and
                    g(s1 * 3, s2, h + 1, 1) and g(s1, s2 * 3, h + 1, 1))
    else:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p))


for s in range(1, 101):
    if g(31, s, 0, 0):
        print(s)  # 29"""


# 23
"""def f(x, end):
    if x == end:
        return True
    elif x > end or x == 0:
        return False
    else:
        if x < 0:
            return f(x + 3, end) + f(x + 4, end) + f(abs(x), end)
        else:
            return f(x + 3, end) + f(x + 4, end)


print(f(-21, -8) * f(-8, 35))  # 9024"""

# 24
"""from re import *
s = open('files/24_горбачев6.txt').readline()
expr = findall('(?:[1-9, AB]+)(?:[-.+*][1-9, AB]+)+', s)
ans = max(expr, key=len)
print(len(ans), ans)   # 53"""

# 25
"""from fnmatch import fnmatch
for i in range(10**7, 0, -1):
    if fnmatch(str(i), '89?45*75'):
        print(i, i // 25)
# 8994575 359783
# 8984575 359383
# 8974575 358983
# 8964575 358583
# 8954575 358183
# 8944575 357783
# 8934575 357383
# 8924575 356983
# 8914575 356583"""

# 26
"""Система отслеживания безбилетников ежеминутно фиксирует вход и выход пассажиров
электрички (в минутах, прошедших от начала суток). Считается, что в моменты фиксации
входа и выхода пассажир находится в электричке. Нулевая минута соответствует моменту
открытия дверей на первой станции поезда, который катается целые сутки без перерыва.
Аналитик транспортной компании проверяет данные системы наблюдения за прошедшие
сутки, и выявляет момент времени, в которые число пассажиров, находящихся в поезде,
было максимальным. Назовём такой момент времени часом пик.
Входной файл содержит время входа и выхода каждого пассажира электрички. Определите
число пассажиров в час пик и момент времени, когда начался час пик.
Входные данные
В первой строке входного файла находится натуральное число N (N < 10000) - общее
количество пассажиров поезда.
Следующие N строк содержат пары чисел, обозначающих соответственно время входа и
время выхода пассажира (все числа натуральные, не превышающие 1440).
Запишите в ответе два натуральных числа: сначала найденное количество пассажиров в
час пик, затем минуту начала часа пик."""
"""f = open('files/26_горбачев6.txt')
# f = open('files/26_горбачев6_exaple.txt')
n = int(f.readline())
enter = []
exit = []
pas = []
for i in range(n):
    x, y = map(int, f.readline().split())
    enter.append(x)
    exit.append(y)
mx = 0
k = 0
for i in range(0, 1440):
    if i in enter:
        k += enter.count(i)
    if i in exit:
        k -= exit.count(i)
    mx = max(mx, k)
    if k == 445:
        print(i)
    pas.append([i, k])

print(mx)
print(pas)
# 445, 1057"""

# 27
"""def dist(p1, p2):
    return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))


def density(cl):
    res = []
    for p1 in cl:
        c = 0
        for p2 in cl:
            if dist(p1, p2) < 1:
                c += 1
        res.append(c)
    return sum(res) / len(res)


data = list(list(map(float, s.replace(',', '.').split())) for s in open('files/27A_горбачев6.txt'))
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data.copy():
            if dist(p1, p2) <= 0.5:
                clusters[-1].append(p2)
                data.remove(p2)

# from turtle import *
# tracer(0)
# screensize(3000, 3000)
# up()
# colors = ['red', 'green', 'blue'] + ['black'] * 10
# for cl, color in zip(clusters, colors):
#     for x, y in cl:
#         goto(x * 100, y * 100)
#         dot(10, color)
# done()

clusters = [cl for cl in clusters if len(cl) >= 30]
print([len(cl) for cl in clusters])
density_cl = [density(cl) for cl in clusters]
print(density_cl)
print(int(max(density_cl) * 1000), int((sum(density_cl) / len(density_cl)) * 1000))
# A: 35954 32067
# B: 2361060 2235322"""

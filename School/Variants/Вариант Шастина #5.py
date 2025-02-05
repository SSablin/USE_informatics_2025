# 2
"""print('x y w z F')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                f = ((x == (y <= (z or x))) and w)
                if f:
                    print(x, y, w, z)"""
# 5
"""mn = float('inf')
for i in range(300):
    n = bin(i)[2:]
    if n.count('1') % 2 == 0:
        n = '10' + n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'
    r = int(n, 2)
    if r > 171:
        mn = min(mn, i)
print(mn)  # 64"""

# 6
"""from turtle import *
tracer(0)
screensize(5000, 5000)
c = 30
lt(90)
for i in range(4):
    fd(16 * c)
    lt(90)
    fd(20 * c)
    lt(90)
up()
fd(4 * c)
lt(90)
fd(8 * c)
rt(180)
down()
for i in range(3):
    fd(35 * c)
    lt(90)
    fd(6 * c)
    lt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'green')
exitonclick()
update()"""
# print(((16 + 20) * 2) + (27 * 2))  # 126
# 8
"""from itertools import product
gl = 'АИ'
c = 0
for x in product(sorted(set('ПАВСИКАКИЙ')), repeat=6):
    s = ''.join(x)
    if sum(s.count(x + y) for x in gl for y in gl) > 0:
        c += 1
        print(c, s)
        if s == 'КАКААА':
            print(c)  # 23611
            break"""
# 9 № 18118
"""def peremnogit(pov):
    s = ''
    for x in pov:
        s += str(x) + '*'
    return s[:-1]


c = 0
f = open('9_18364.txt')
for s in f:
    a = [int(x) for x in s.split()]
    pov = [int(x) for x in a if a.count(x) > 1]
    nepov = [int(x) for x in a if a.count(x) == 1]
    if len(pov) > 0:
        if sum(nepov) * 3 <= eval(peremnogit(pov)):
            c += 1
            print(a, c)  # 2766
            print(pov, nepov)"""

# 12
"""ans = set()
for n in range(3, 10_000):
    s = '7' + '6' * n
    while ('766' in s) or ('667' in s):
        if '766' in s:
            s = s.replace('766', '67', 1)
        if '667' in s:
            s = s.replace('667', '7', 1)
    ans.add(s)
print(len(ans))  # 4"""

# 13
"""from ipaddress import *
for a in range(256):
    f = True
    for ip in ip_network(f'192.214.{a}.184/255.255.255.224', 0):
        b = f'{ip:b}'
        if not (b.count('1') > 15):
            f = False
            break
    if f:
        print(a)  # 127
        break"""

# 14

"""def r7(x):
    s = ''
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    return s


for x in range(100):
    p = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    p7 = r7(p)
    if p7.count('6') == 49:
        print(x)  # 26
        break"""

# 15
"""def cif(x, y):
    if (x % 10) == (y % 10):
        return True
    return False

for a in range(300):
    f = True
    for x in range(300):
        if not ((not cif(x, 5) and cif(x, 4)) <= (x > (a - 11))):
            f = False
            break
    if f:
        print(a)  # 14"""

# 16
"""from sys import setrecursionlimit
setrecursionlimit(3_000)

def f(n):
    if n > 3000:
        return n
    if n <= 3000:
        return (2 * n + 4) * f(n + 2)


a = f(20) // f(28)
print(sum(map(int, str(a))))  # 21"""
# 17
"""s = [int(x) for x in open('files/17_18368.txt')]

m7 = float('inf')
for x in s:
    if abs(x) % 10 == 7:
        m7 = min(m7, x)

ans = []
for i in range(len(s)):
    if sum(1 for x in s[i:i + 3] if len(str(abs(x))) == 5) > 0:
        if abs(s[i] * s[i + 1] * s[i + 2]) % abs(m7) == 0:
            ans.append(s[i] * s[i + 1] * s[i + 2])
            print(s[i], s[i+1], s[i+2])
print(len(ans), max(ans))  # 3 54248777901150"""

# 19
"""def g(s, h):
    if s >= 313 and h == 3:
        return True
    if s >= 313 and h != 3:
        return False
    if s < 313 and h == 3:
        return False

    if h % 2 == 0:
        return g(s + 2, h + 1) or g(s + 3, h + 1) or g(s * 3, h + 1)
    else:
        return g(s + 2, h + 1) and g(s + 3, h + 1) and g(s * 3, h + 1)


for s in range(1, 313):
    if g(s, 1):
        print(s)  # 103 + 104 = 207"""

# 20
"""def g(s, h):
    if s >= 313 and h == 4:
        return True
    if s >= 313 and h != 4:
        return False
    if s < 313 and h == 4:
        return False

    if h % 2 != 0:
        return g(s + 2, h + 1) or g(s + 3, h + 1) or g(s * 3, h + 1)
    else:
        return g(s + 2, h + 1) and g(s + 3, h + 1) and g(s * 3, h + 1)


for s in range(1, 313):
    if g(s, 1):
        print(s)  # 100 102"""

# 21
"""def g(s, h):
    if s >= 313 and (h == 3 or h == 5):
        return True
    if s >= 313 and (h != 3 and h != 5):
        return False
    if s < 313 and h == 5:
        return False

    if h % 2 == 0:
        return g(s + 2, h + 1) or g(s + 3, h + 1) or g(s * 3, h + 1)
    else:
        return g(s + 2, h + 1) and g(s + 3, h + 1) and g(s * 3, h + 1)


for s in range(1, 313):
    if g(s, 1):
        print(s)  # 98 + 99 = 197"""

# 23
"""def f(x, end):
    if x > end:
        return False
    if x == end:
        return True
    if x < end:
        return f(x + 3, end) + f(x + max(int(x) for x in str(x)), end)


print(f(10, 24) * f(24, 41))  # 36"""

# 24
"""s = open('files/24_18284.txt').readline().strip()
s = "REVVVLAAORRVEARRLBOLRVER"
min_l = float('inf')
pos = {let: [i for i in range(len(s)) if s[i] == let] for let in 'LOVE'}
# Создаём словарь со списками индексов для L, O, V, E в s
print(pos)  # {'L': [5, 16, 19], 'O': [8, 18], 'V': [2, 3, 4, 11, 21], 'E': [1, 12, 22]}
ind = {let: 0 for let in 'LOVE'}  # Индексы для текущих позиций в pos['L'], pos['O'], pos['V'], pos['E']
print(ind)  # {'L': 0, 'O': 0, 'V': 0, 'E': 0}
for left in range(len(pos['L'])):  # Перебираем все позиции для 'L'
    ind['L'] = left  # Устанавливаем текущий индекс для 'L'
    # Пока указатель текущего символа (например, 'O') не находится правее предыдущего (например, 'L'),
    # двигаем указатель вперёд
    for last, curr in zip('LOV', 'OVE'):  # составляет пары символов, перечисленных в последовательности
        while ind[curr] + 1 < len(pos[curr]) and pos[curr][ind[curr]] < pos[last][ind[last]]:
            ind[curr] += 1
    # После этого проверяем, что все символы идут в правильном порядке
    if all(pos[curr][ind[curr]] > pos[last][ind[last]] for last, curr in zip('LOV', 'OVE')):
        # Вычисляем длину текущей подстроки
        # Если длина меньше текущей минимальной, обновляем
        min_l = min(min_l, pos['E'][ind['E']] - pos['L'][ind['L']] + 1)
print(min_l)  # 2000031"""

"""f = open('files/24_18284.txt')
s = f.readline()

b_l = b_lo = b_lov = -1
m = 10 ** 8

for i in range(len(s)):
    if s[i] == 'L':
        b_l = i
    if s[i] == 'O':
        b_lo = b_l
    if s[i] == 'V':
        b_lov = b_lo
    if s[i] == 'E' and b_lov != -1:
        m = min(m, i - b_lov + 1)

print(m)"""

# 25
"""def div(x):
    s = {1}
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sum(s) // len(s)


c = 0
for n in range(770_000, 1, -1):
    a = div(n)
    if a % 100 == 12 and c < 5:
        print(n, a)
        c += 1
    elif c >= 5:
        break
# 769995 25612
# 769923 18312
# 769916 35712
# 769700 27112
# 769583 2912"""

# 26
"""
f = open('files/26_18541.txt')
n, m = map(int, f.readline().split())
w = sorted([int(f.readline()) for i in range(n)], reverse=True)
w_max = sorted([int(f.readline()) for i in range(m)], reverse=True)
i = s = 0
count = [0] * len(w)
for x in w_max:
    while x < w[i]:
        i += 1
    s += w[i]
    count[i] += 1

print(s // len(w_max), w[count.index(max(count))])  # 49989 65113"""

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

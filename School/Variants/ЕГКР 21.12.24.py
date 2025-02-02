# 6 №19238
"""from turtle import *
tracer(0)
screensize(2000,2000)

lt(90)
c = 30
for i in range(8):
    fd(16 * c)
    rt(90)
    fd(22 * c)
    rt(90)

up()

fd(5 * c)
rt(90)
fd(5 * c)
lt(90)

down()

for i in range(8):
    fd(52 * c)
    rt(90)
    fd(77 * c)
    rt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'green')

exitonclick()
update()"""
# print(17 * 11)  # 187


# 9 №19241
"""k = 0

for s in open('files/9_19241.txt'):
    a = [int(x) for x in s.split()]
    k += 1
    a3 = [x for x in a if a.count(x) == 3]
    a1 = [x for x in a if a.count(x) == 1]
    if len(a3) == 6 and len(a1) == 1 and sum(a3)/len(a3) < a1[0]:
        print(k)  # 17975"""

# 11 №19243
"""from math import log2, ceil

for kod in range(2, 1000):
    char = ceil(log2(kod))
    num = ceil(char * 377 / 8)
    if 23155 * num > 5536 * 1024:
        print(kod)  # 33
        break"""

# 17 №19249
"""s = [int(i) for i in open('files/17_19249.txt')]

m = -float('inf')
for i in s:
    if len(str(abs(i))) == 5 and abs(i) % 100 == 43:
        m = max(m, i)
print(m)  # 98143


def tr(s):
    c = 0
    for a in s:
        if len(str(abs(a))) == 5 and str(a)[-2:] == '43':
            return True
    return False


ans = []
for i in range(len(s) - 2):
    if tr(s[i:i + 3]) and (s[i] ** 2 + s[i + 1] ** 2 + s[i + 2] ** 2) <= m ** 2:
        ans.append(s[i] ** 2 + s[i + 1] ** 2 + s[i + 2] ** 2)
        print(s[i], s[i+1], s[i+2])
print(len(ans), min(ans))  # 92 838850571"""

# Кабанов
"""a = [int(x) for x in open('files/17_19249.txt')]


def ch(x): return 10_000 <= abs(x) < 100_000 and abs(x) % 100 == 43


mx = max(x for x in a if ch(x))  # 98143
ans = []

for x, y, z in zip(a, a[1:], a[2:]):
    if (ch(x) or ch(y) or ch(z)) and x ** 2 + y ** 2 + z ** 2 <= mx ** 2:
        ans.append(x ** 2 + y ** 2 + z ** 2)

print(len(ans), min(ans))  # 92 838850571"""

# SS feat Кабанов
"""s = [int(i) for i in open('files/17_19249.txt')]


def ch(x): return 10_000 <= abs(x) < 100_000 and abs(x) % 100 == 43


m = max(x for x in s if ch(x))
ans = []
for i in range(len(s) - 2):
    if (ch(s[i]) or ch(s[i + 1]) or ch(s[i + 2])) and (s[i] ** 2 + s[i + 1] ** 2 + s[i + 2] ** 2) <= m ** 2:
        ans.append(s[i] ** 2 + s[i + 1] ** 2 + s[i + 2] ** 2)
print(len(ans), min(ans))  # 92 838850571"""

# 24 № 19254
"""Текстовый файл состоит из символов F, G, Q, R, S и W. 
Определите в прилагаемом файле максимальное количество идущих подряд символов, 
среди которых подстрока FSRQ встречается ровно 80 раз.
Для выполнения этого задания следует написать программу."""
# Кабанов
"""s = open('files/24_19254.txt').readline().rstrip()

l = 0
m = 0
k = 0
sub = ''

for r in range(3, len(s)):
    if s[r - 3] + s[r - 2] + s[r - 1] + s[r] == 'FSRQ':
        k += 1
    while k > 80:
        if s[l] + s[l + 1] + s[l + 2] + s[l + 3] == 'FSRQ':
            k -= 1
        l += 1
    if k == 80:
        m = max(m, r - l + 1)
print(m)  # 2379"""

# Ермаков
"""s = open('files/24_19254.txt').readline().rstrip()
sp = []
a = 0
for i in range(s.count('FSRQ')):
    sp.append(s.index('FSRQ', a))
    a = s.index('FSRQ', a) + 1
ans = max(sp[80] + 3, len(s) - sp[-81] - 1)
for i in range(1, len(sp) - 82):
    ans = max(ans, sp[i + 81] - sp[i] + 2)
print(ans)  # 2379"""

# Родя
"""s = open('files/24_егкрдек.txt').readline()
s = s.replace('FGSW', ' ').split()
max_sm = -float('inf')
for i in range(len(s) - 85):
    sm = sum(len(kusok) for kusok in s[i: i+86])
    if sm > max_sm:
        max_sm = sm
        ans_i = i
print(ans_i, len(s), max_sm + 85 * 4 + 6)  # 1447"""
# строка с которой начинается по середине =>
# с боков стоит пробел =>
# + по 3 буквы в начале и в конце

# SS feat Родя
"""s = open('files/24_19254.txt').readline()
s = s.replace('FSRQ', ' ').split()
max_sm = -float('inf')
for i in range(len(s) - 80):
    sm = sum(len(kusok) for kusok in s[i: i+81])
    if sm > max_sm:
        max_sm = sm
        ans_i = i
print(ans_i, len(s), max_sm + 80 * 4 + 6)  # 2379"""

# 27 №19257
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



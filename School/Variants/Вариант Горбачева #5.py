# 2
"""print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x or (not y)) <= (not (y <= z))) and w
                if f:
                    print(x, y, z, w, f)"""
# x y z w f
# 0 1 0 1 1
# 0 1 1 1 1
# 1 1 0 1 1
# 5
"""for i in range(35):
    n = bin(i)[2:]
    if i % 3 == 0:
        n = '101' + str(n)[3:]
    else:
        n = n[:-4] + '111'
    r = int(n, 2)
    if r > 30:
        print(r)  # 41"""

# 8
"""from itertools import product
c = 0
for x in product('WSDA', repeat=5):
    c += 1
    s = ''.join(x)
    if 'DD' in s and s.count('S') >= 1 and s[-1] != 'W':
        print(s, c)  # 27"""

# 9
"""c = 0
for s in open('files/9_горбачев5.txt'):
    c += 1
    a = list(map(int, s.split()))
    povtor = [a.count(x) for x in a]
    chet = [x for x in a if x % 2 == 0]
    nechet = [x for x in a if x % 2 != 0]
    if povtor.count(2) == 6 and sum(chet) < sum(nechet):
        print(c)  # 47
        break"""

# 12
"""ans = []
for n in range(1000):
    s = '7' + '0' * n
    while ('700' in s) or ('100' in s) or ('000' in s):
        if '700' in s:
            s = s.replace('700', '01', 1)
        if '100' in s:
            s = s.replace('100', '07', 1)
        if '000' in s:
            s = s.replace('000', '1', 1)
    if s.count('7') == 7:
        ans.append(n)
print(sum(ans))  # 144"""

# 13
"""c = 0
from ipaddress import *
ip = ip_address('222.119.45.0')
net = ip_network(f'{ip}/255.255.224.0', 0)
for ip in net:
    b = format(ip, 'b')
    if b.count('0') % 3 == 0:
        c += 1
print(c)  # 2731"""

# 14
"""c = 0
def r7(x):
    s = ''
    while x > 0:
        s += str(x % 7)
        x //= 7
    return s[::-1]


for x in range(1, 1001):
    s = 5 ** x + 31 ** 31 - 46 ** 17 - x
    if 100 < r7(s).count('6') < 1000:
        c += 1
print(c)  # 145"""

# 15
"""c = 0
for a in range(300):
    f = False
    for x in range(300):
        for y in range(300):
            if (x < (a + 2)) and (y < (a - 3)) and ((3 * x + y) > 66):
                f = True
                break
        if f:
            break
    if not f:
        c += 1
        print(a)
print(c)  # 17"""

# 16
"""def f(n):
    if n <= 8:
        return n
    if n > 8 and n % 2 == 0:
        return 7 + n * f(n - 2)
    elif n % 2 != 0:
        return 3 * n * f(n - 1)


print(f(31) / 11 + f(27) / 6)  # 8282759544174515"""

# 17
"""s = [int(x) for x in open('files/17_горбачев5.txt')]
mx = 0
for x in s:
    if abs(x) % 100 == 33 and len(str(abs(x))) == 3:
        mx = max(mx, x)


def f(s):
    for x in s:
        if len(str(abs(x))) == 5 and abs(x) % 100 == 61:
            return True
    return False


ans = []
for i in range(len(s)):
    if f(s[i:i + 3]) and sum(s[i:i + 3]) >= mx:
        ans.append(sum(s[i:i + 3]))
print(len(ans), max(ans))  # 154 237633"""

# 19
"""def g(s, h):
    if s <= 13 and h == 3:
        return 1
    if s > 13 and h == 3:
        return 0
    if s <= 13 and h != 3:
        return 0
    if h % 2 == 0:
        return g(s - 3, h + 1) or g(s - 5, h + 1) or g(s // 4, h + 1)
    else:
        return g(s - 3, h + 1) or g(s - 5, h + 1) or g(s // 4, h + 1)


for s in range(14, 1000):
    if g(s, 1):
        print(s)  # 223"""

# 20
"""def g(s, h):
    if s <= 13 and h == 4:
        return 1
    if s > 13 and h == 4:
        return 0
    if s <= 13 and h != 4:
        return 0
    if h % 2 == 0:
        return g(s - 3, h + 1) and g(s - 5, h + 1) and g(s // 4, h + 1)
    else:
        return g(s - 3, h + 1) or g(s - 5, h + 1) or g(s // 4, h + 1)


for s in range(14, 1000):
    if g(s, 1):
        print(s)  # 59 60"""

# 21
"""def g(s, h):
    if s <= 13 and (h == 3 or h == 5):
        return 1
    if s > 13 and h == 5:
        return 0
    if s <= 13 and (h != 5 and h != 3):
        return 0
    if h % 2 == 0:
        return g(s - 3, h + 1) or g(s - 5, h + 1) or g(s // 4, h + 1)
    else:
        return g(s - 3, h + 1) and g(s - 5, h + 1) and g(s // 4, h + 1)


for s in range(14, 1000):
    if g(s, 1):
        print(s)  # 238"""

# 23
"""Задание 23 .
Исполнитель преобразует число на экране. У исполнителя есть три команды, которые
обозначены латинскими буквами:
А. Вычесть 2
В. Вычесть З
С. Найти целую часть от деления на 2
Сколько существует программ, которые преобразуют исходное число 176 в число 23 и
при этом содержат не более двух команд В?"""

"""def f(x, end, b):
    if x < end:
        return 0
    if x == end:
        return 1
    if x > end:
        if b < 2:
            return f(x - 2, end, b) + f(x - 3, end, b+1) + f(x // 2, end, b)
        else:
            return f(x - 2, end, b) + f(x // 2, end, b)


print(f(176, 23, 0))  # 113980"""

# 24
"""Задание 24 .
Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения).
Определите максимальное количество символов в непрерывной последовательности,
являющейся корректным арифметическим выражением с целыми неотрицательными
числами (без знака), значение которого равно 100. В этом выражении никакие два
знака арифметических операций не стоят рядом, порядок действий определяется по
правилам математики. В записи чисел отсутствуют незначащие (ведущие) нули.
В ответе укажите количество символов."""

"""s = open('files/24_горбачев5.txt').readline().strip()
for i in ('++', '**', '*+', '+*'):
    s = s.replace(i, ' ')

m = ''
for c in s.split():
    if len(c) > len(m):
        for i in range(len(c) - 1):
            if c[i] not in '*+' and c[i] + c[i + 1] not in (f'0{i}' for i in range(10)):
                sub = ''
                for j in range(i, len(c)):
                    sub += c[j]
                    if sub[-1] not in '*+' and eval(sub) == 100:
                        m = max(m, sub, key=len)
print(len(m), m)  # 80"""

# 25
"""def div(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    if len(s) > 0:
        return min(s) + max(s)
    else:
        return 0


c = 0
for i in range(900_000):
    m = str(div(i))
    if m[0] == m[-1] == '7':
        if c < 7:
            print(i, m)
            c += 1
        else:
            break"""

# 26
"""f = open('files/26_горбачев5.txt')
N, M, K = map(int, f.readline().split())
mx = 0
s = [M + 1] * (K + 1)

for i in f:
    r, m = map(int, i.split())
    s[m] = min(s[m], r)

for i in range(1, K - 3):
    x = min(s[i], s[i + 1], s[i + 2], s[i + 3])
    mx = max(mx, x)

print(mx - 1)

for i in range(1, K - 3):
    if min(s[i], s[i + 1], s[i + 2], s[i + 3]) == mx:
        print(i, i+1, i+2, i+3)"""
# 9717 5198

# 27
"""from math import dist

data = [tuple(map(float, s.replace(',', '.').split())) for s in open('files/27B_горбачев5.txt')]

# DBSCAN
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data.copy():
            if dist(p1, p2) <= 1:
                clusters[-1].append(p2)
                data.remove(p2)
clusters = [cl for cl in clusters if len(cl) > 30]
print([len(cl) for cl in clusters])


def centroid(cl):
    r = []
    for p1 in cl:
        r.append([sum(dist(p1, p2) for p2 in cl), p1])
    return min(r)[1]


centr = [centroid(cl) for cl in clusters]
print(int(sum(x for x, y in centr) / len(centr) * 10000), int(sum(y for x, y in centr) / len(centr) * 10000))"""
# A: 15615 19452
# B: 2415 3237

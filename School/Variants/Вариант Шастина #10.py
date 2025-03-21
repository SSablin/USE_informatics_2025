# 8
"""from itertools import product
c = -1
f = False
for i in product('АЕИКМСЧ', repeat=5):
    s = ''.join(i)
    if s == 'МАСИК':
        f = True
    if s == 'ЧЕЧИК':
        break
    if f:
        c += 1
        print(c, s)  # 5193"""

# 9
"""c = 0
for s in open('files/9_шастин10.txt'):
    a = list(map(int, s.split()))
    if ((all(x % 5 != 0 for x in a) and not all(len(str(x)) == 2 for x in a)) or
            (not all(x % 5 != 0 for x in a) and all(len(str(x)) == 2 for x in a))):
            c += 1
            print(c, a)  # 305"""

# 12
"""s = '4' * 222
c = 0
while '4444' in s or '222' in s:
    if '4444' in s:
        s = s.replace('4444', '2', 1)
        c += 1
    else:
        s = s.replace('222', '44', 1)
        c += 1
print(c)  # 86"""

# 13
"""Для узла с IР-адресом 221.142.14.0 адрес подсети равен 221.142.0.0. Сколько
существует различных возможных значений маски сети, если известно, что в этой сети
не менее 8000 узлов? Ответ запишите в виде десятичного числа."""
"""from ipaddress import *
ip = ip_address('221.142.14.0')
c = 0
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if net.num_addresses >= 8000 and str(net.network_address) == '221.142.0.0':
        c += 1
print(c)  # 5"""

# 14
"""def i3(x):
    s = ''
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]


for a in range(1, 100000):
    x = 3 ** 10 + 3 ** 7 + 3 ** 3 + 2 - a
    x3 = i3(x)
    if (sum(1 for x in list(map(int, x3)) if x == 0) == 
            sum(1 for x in list(map(int, x3)) if x == 1) == 
            sum(1 for x in list(map(int, x3)) if x == 2)):
        print(a)  # 41960
        break"""

# 15
"""for a in range(1, 300):
    f = True
    for x in range(1, 300):
        if not (((x & a) == 0) <= (((x & 77) == 0) and ((x & 44) == 0))):
            f = False
            break
    if f:
        print(a)  # 109
        break"""

# 16
"""from sys import setrecursionlimit
setrecursionlimit(60_000)
def f(n):
    if n < 222:
        return 111
    else:
        return 2 * (n + 4) + f(n - 3)


print(f(55555) - f(55543))  # 444436

sp = [0, ]
for i in range(1, 60_000):
    if i < 222:
        sp.append(111)
    else:
        sp.append(2 * (i + 4) + sp[i - 3])
print(sp[55555] - sp[55543])  # 444436"""

# 17
"""s = [int(x) for x in open('files/17_шастин10.txt')]
mn_123 = min(x for x in s if abs(x) % 1000 == 123 and x == abs(x))

ans = []
for i in range(len(s) - 1):
    if (max(s[i:i + 2]) - min(s[i:i + 2])) <= mn_123:
        ans.append(max(s[i:i + 2]) - min(s[i:i + 2]))
print(len(ans), max(ans))  # 1293 13117"""

# 23
"""diap = [x for x in range(5, 38) if x % 11 == 0]
print(diap)


def f(x, end):
    if x == end:
        return True
    if x > end:
        return False
    if x < end:
        return f(x + 2, end) + f(x + 3, end) + f(x + 5, end)


print(f(5, 11) * f(11, 22) * f(22, 33) * f(33, 37))  # 512"""

# 25
"""from fnmatch import fnmatch

for i in range(4321, 10**9, 4321):
    if fnmatch(str(i), '34*56?7'):
        if str(eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))[-1] == '0':
            print(i, eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))"""



# 15 №21503
mn = float('inf')
for a in range(1, 100):
    for i in range(a, 400):
        b = i / 4
        f = True
        for x in range(1, 100):
            A = a <= x <= b
            P = 10 <= x <= 40
            Q = 20 <= x <= 50
            if not (P <= ((Q and (not A)) <= (not P))):
                f = False
                break
        if f and (b - a) < mn:
            mn = (b - a)
            print(mn, a, b)  # 20

# 16 №21504
f = [0]
for n in range(1, 2026):
    if n == 1:
        f.append(1)
    else:
        f.append((n + 1) * f[n - 1])
print(((f[2025] // 2026) + f[2024]) // f[2023])  # 4050


# 23 №21510
def f(x, end):
    if x == end:
        return True
    if x < end or x == 15:
        return False
    if x > end:
        return f(x - 2, end) + f(x - 5, end) + f(x // 3, end)


print(f(50, 35) * f(35, 20) * f(20, 8))  # 98

# 24 №21509
from re import *

s = open('files/24_21509.txt').readline()
num = r'(0|[7-9]\d*)'
reg = rf'{num}([-*]{num})*'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)  # 249


# 25 №21511
def Qf(x):
    s = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)
    return sum(s)


def natural(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


c = 0
x = 1_000_000
while c < 5:
    Q = Qf(x)
    if Q != 0 and natural(Q):
        print(x, Q)
        c += 1
    x += 1
# 1000020 2201387
# 1000054 653641
# 1000056 1500143
# 1000066 532093
# 1000078 504289
# 26 №21512
f = open('files/26_21512.txt')
n, m, k = map(int, f.readline().split())

# f = ['1 2', '2 3', '3 4', '4 5', '5 6', '6 7', '1 7', '2 8']
# n, m, k = 8, 6, 9  # кол-во (занятых, рядов, мест)

mn_ryad = [m + 1] * (k + 1)
for s in f:
    ryad, mesto = map(int, s.split())
    mn_ryad[mesto] = min(mn_ryad[mesto], ryad)

m_r = []
m_m = 0
for i in range(1, k - 1):
    r = min(mn_ryad[i], mn_ryad[i + 1], mn_ryad[i + 2]) - 1
    if r == 1804:
        print(i)
        m_m = i
    m_r.append(r)
print(max(m_r), m_m)  # 1804 4434

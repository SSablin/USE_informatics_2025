# Тип 15 №45249
"""
def D(n, m):
    if n % m == 0:
        return True
    return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if (D(x, 3) <= (not(D(x, 5)))) or (x + A >= 90):
            k += 1
    if k == 1000:
        print(A)
        break
"""

# № 17634 Основная волна 19.06.24 (Уровень: Базовый)
"""
Amax = -10**10
for A in range(1, 300):
    k = 0
    for x in range(1, 301):
        for y in range(1, 301):
            if (x + y <= 30) or (y <= x + 2) or (y >= A):
                k += 1
    if k == 300*300:
        if Amax < A:
            Amax = A
print(Amax)
"""

# № 16381 ЕГКР 27.04.24 (Уровень: Базовый)
"""
def D(n, m):
    if n % m == 0:
        return True
    return False

for A in range(1, 1000):
    k = 0
    for x in range(1, 1001):
        if (not(D(x, A))) <= (D(x, 28) <= (not(D(x, 49)))):
            k += 1
    if k == 1000:
        print(A)
"""

# 15 № 34535
"""print('a p q r f')
for a in range(2):
    for p in range(2):
        for q in range(2):v
            for r in range(2):
                f = (a or p) or (q <= r)
                if not f:
                    print(a, p, q, r, f)"""

"""print('A P Q F')
for a in range(2):
    for p in range(2):
        for q in range(2):
            f = (not a) <= (p <= (not q))
            if not f:
                print(a, p, q, f)"""

"""print('A P Q F')
for a in range(2):
    for p in range(2):
        for q in range(2):
            f = (not a) <= ((p and q) <= a)
            if not f:
                print(a, p, q, f)"""

"""mx = 0
for b in range(1, 101):
    for i in range(b, 401):
        a = i / 4
        f = True
        for x in range(1, 101):
            if not (((a <= x <= b) <= (43 <= x <= 49)) or (44 <= x <= 53)):
                f = False
                break
        if f and (b - a) > mx:
            mx = (b - a)
            print(mx)  # 10"""

# ЕГКР 19.04
"""P = list(range(66, 75 + 1))
Q = list(range(72, 85 + 1))
A = []
for x in range(0, 200):
    if not ((not (x in A)) <= ((x in P) == (x in Q))):
        A.append(x)
print(A)
print(A[-1] - A[0])  # 19"""

"""m = float('inf')
P = [i for i in range(66, 75)]
Q = [i for i in range(72, 85)]
for Amin in range(1, 101):
    for Amax in range(Amin + 1, 101):
        check = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(1, 101):
            f = (not (x in A)) <= ((x in P) == (x in Q))
            if not f:
                check = 0
                break
        if check == 1:
            m = min(m, Amax - Amin)
            print(m)
print(m)  # 19"""

"""mn = float('inf')
for b in range(1, 101):
    for i in range(b, 401):
        a = i / 4
        f = True
        for x in range(1, 101):
            if not (not (a <= x <= b)) <= ((66 <= x <= 75) == (72 <= x <= 85)):
                f = False
                break
        if f and (b - a) < mn:
            mn = (b - a)
print(mn)  # 19"""

# №20961
"""P = list(range(15, 142 + 1))
Q = list(range(38, 167 + 1))
A = []
for x in range(0, 200):
    if not ((x in Q) <= (((x not in A) and (x in P)) <= (x not in Q))):
        A.append(x)
print(A)
print(A[-1] - A[0])  # 104"""

# №19980
"""mi = float('inf')
ma = float('-inf')
for x in range(0, 1000 * 4 + 1):
    x = x / 4
    P = 52 <= x <= 105
    Q = 0 <= x <= 53
    if (((not P) and (not Q)) <= (x * x > 303601)) == 0:
        mi = min(mi, x)
        ma = max(ma, x)
print(ma - mi)  # 445.75, округляем к 446"""

# №18930
"""mn = float('inf')
for b in range(0, 350 + 1):
    for i in range(b + 1, 350 * 4 + 1):
        a = i / 4
        f = True
        for x in range(1, 350 + 1):
            if not (((160 <= x <= 250) <= (10 <= x <= 150)) or ((not (a < x < b)) <= (240 <= x <= 300))):
                f = False
                break
        if f and (b - a) < mn:
            mn = (b - a)
            print(mn)  # 80"""

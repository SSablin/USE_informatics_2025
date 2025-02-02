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


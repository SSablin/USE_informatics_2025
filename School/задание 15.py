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

# ЕГКР 19.04 В1
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

"""def f(x):
    P = 66 <= x <= 75
    Q = 72 <= x <= 85
    A = a1 <= x <= a2
    return (not A) <= (P == Q)
ox = [y for x in (66, 75, 72, 85) for y in (x, x+0.01, x-0.01)]

m = []
for a1 in ox:
      for a2 in ox:
          if a2 > a1 and all(f(x)==1 for x in ox):
              m.append(a2-a1)
print(min(m)) # 19"""



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


# ЕГКР 19.04 В2
# Кабанов
"""def f(x):
    B = 36 <= x <= 75
    C = 60 <= x <= 110
    A = a1 <= x <= a2
    return (not A) <= (B==C)
ox = [y for x in (36, 75, 60, 110) for y in (x, x+0.01, x-0.01)]

m = []
for a1 in ox:
      for a2 in ox:
          if a2 > a1 and all(f(x)==1 for x in ox):
              m.append(a2-a1)
print(min(m)) # 74"""

# №21710
"""mn = float('inf')
for a1 in range(1, 400):
    for a2 in range(a1, 1600):
        a2 /= 4
        f = True
        for x in range(1, 200):
            A = a1 <= x <= a2
            B = 36 <= x <= 75
            C = 60 <= x <= 110
            if not ((not A) <= (B == C)):
                f = False
                break
        if f:
            mn = min(mn, a2 - a1)
            print(mn, a1, a2)  # 74"""

# №20961
"""mn = float('inf')
for a1 in range(1, 400):
    for a2 in range(a1, 1600):
        a2 /= 4
        f = False
        for x in range(1, 400):
            A = a1 <= x <= a2
            P = 15 <= x <= 142
            Q = 38 <= x <= 167
            if not (Q <= ((not A) and P)) <= (not Q):
                f = True
                break
        if not f:
            if (a2 - a1) < mn:
                mn = a2 - a1
                print(mn, a1, a2)  # 104"""

"""for x in [k * 0.25 for k in range(-10000, 10001)]:
    a = 0
    p = 15 <= x <= 142
    q = 38 <= x <= 167
    f = not(q <= (((not a) and p) <= (not q)))
    if f != 0:
        print(x)
print(142 - 38)  # 104"""

# https://3.shkolkovo.online/catalog/7517
# 49372
"""mn = float('inf')
for a1 in range(1, 800):
    for a2 in range(a1+1, 800):
        a2 /= 4
        f = True
        for x in range(1, 200):
            P = 55 <= x <= 100
            Q = 66 <= x <= 129
            A = a1 <= x <= a2
            if not (P <= (((Q and (not A)) <= (not P)))):
                f = False
                break
        if f:
            mn = min(mn, a2 - a1)
print(mn)  # 34"""

# 6012

"""mx = 0
for a1 in range(1, 400):
    for a2 in range(a1 + 1, 800):
        a2 /= 4
        f = True
        for x in range(1, 400):
            P = 15 <= x <= 50
            Q = 35 <= x <= 60
            A = a1 <= x <= a2
            if not (((not A) <= P) <= (A <= Q)):
                f = False
                break
        if f:
            mx = max(mx, a2 - a1)
            print(mx)
print(mx)  # 25"""

# 6743
"""mn = float('inf')
for a1 in range(1, 400):
    for a2 in range(a1+1, 800):
        a2 /= 4
        f = True
        for x in range(1, 400):
            P = 10 <= x <= 17
            Q = 15 <= x <= 25
            A = a1 <= x <= a2
            if not (P <= ((Q and (not A)) <= (not P))):
                f = False
                break
        if f:
            mn = min(mn, a2 - a1)
            print(mn)  # 2"""

# 6745
"""mn = float('inf')
for a1 in range(1, 400):
    for a2 in range(a1+1, 800):
        a2 /= 4
        f = True
        for x in range(1, 400):
            P = 10 <= x <= 50
            Q = 30 <= x <= 65
            A = a1 <= x <= a2
            if not ((not A) <= ((P and Q) <= A)):
                f = False
                break
        if f:
            mn = min(mn, a2 - a1)
            print(mn)  # 20"""
# 6746
"""mx = 0
for a1 in range(1, 400):
    for a2 in range(a1+1, 800):
        a2 /= 4
        f = True
        for x in range(1, 400):
            P = 15 <= x <= 50
            Q = 35 <= x <= 60
            A = a1 <= x <= a2
            if not (((not A) <= P) <= (A <= Q)):
                f = False
                break
        if f:
            mx = max(mx, a2 - a1)
            print(mx)  # 25"""
"""p = [i for i in range(15, 51)]  # задаем отрезок p
q = [i for i in range(35, 61)]  # задаем отрезок q
mx = 0
for a1 in range(1, 100):  # перебираем начало отрезка а
    for a2 in range(a1 + 1, 101):  # перебираем конец отрезка а
        c = 0  # флаг, который будет показывать при всех ли х для текущего отрезка а выражение было истинным
        a = [i for i in range(a1, a2)]  # формируем отрезок а
        for x in range(1, 500):  # перебираем значения x
            # если при текущем x выражение ложно
            if (((x not in a) <= (x in p)) <= ((x in a) <= (x in q))) == False:
                c = 1  # меняем значение флага
                # и сбрасываем цикл, переходим к следующему отрезку а,
                # так как для данного отрезка а выражение не тождественно истинно
                break
        if c == 0:  # если значение флага не менялось, значит, при любом х при данном отрезке а выражение было истинным
            mx = max(len(a) - 1, mx)  # вычисляем максимальную длину отрезка
print(mx)  # 25"""

# 15 горбачев7
"""mx = 0
for a in range(1, 400):
    a /= 4
    for b in range(int(a), 200):
        f = False
        for x in range(1, 200):
            P = 32 <= x <= 70
            Q = 63 <= x <= 108
            A = a <= x <= b
            if (Q <= P) and A:
                f = True
                break
        if not f:
            if (b - a) > mx:
                mx = (b - a)
                print(mx, a, b)
print(mx)
# (70; 108]
# 38"""

# № 18372 (Уровень: Базовый)

"""def d(n):
    m = {1}
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            m.add(i)
            m.add(n // i)
    return sum(m) // len(m)

c = 0
x = 770_000
while c < 5:
    x -= 1
    A = d(x)
    if A % 100 == 12:
        c += 1
        print(x, A)"""


# 769995 25612
# 769923 18312
# 769916 35712
# 769700 27112
# 769583 2912

"""def div(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        # if x % i == 0: d |= {i, x // i}
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    return sorted(d)


for n in range(112_500_000, 112_550_000):
    d = div(n)
    if len(d) >= 2:
        m = d[-1] + d[-2]
        if m % 10000 == 1214:
            print(n)"""
# 112508413
# 112520369
# 112523549
# 112534952


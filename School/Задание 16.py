'''ЕСЛИ МЫ  ВОЗВРАЩАЕМ ПРЕДЫДУЩИЙ ЭЛЕМЕНТ, ТО НУЖНО НАЧИНАТЬ С НАЧАЛА
for i in range(0, 10**10, 1):
ЕСЛИ МЫ ВОЗВРАЩАЕМ СЛЕДУЮЩИЙ ЭЛЕМЕНТ, ТО НУЖНО НАЧИНАТЬ С КОНЦА
for i in range(10**10, 0, -1)'''


#  № 13299
'''
nmax = -10**10

from functools import lru_cache
@lru_cache(None)

def f(n):
    if n <= 3:
        return 1
    if n % 3 == 0 and n > 3:
        return f(n/3) + 4*n
    if n % 3 != 0 and n > 3:
        return n * n * n - 26
for n in range(1000):
    if f(n) < 300:
        nmax = max(nmax, n)
print(nmax) #36
'''
#  № 12779
#  paint
'''
#№ 11948 (Уровень: Средний)
def f(n):
    return g(n-1)

def g(n):
    if n < 10:
        return n
    return g(n-2) + 1

count = 0
for n in range(1, 100+1):
    x = f(n)
    if x > 0:
        if int(x**0.5)**2 == x:
            count += 1
print(count)
'''

#  № 10718 (Уровень: Средний)
'''

from functools import lru_cache
@lru_cache(None)

def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * f(n-2) - f(n-1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * f(n-1) + f(n-2) - 2


print(f(170))'''

# 13.10.24
#  17974
"""NQ 77974 (Уровень: Базовый)
(Л. Шастин) Алгоритм вычисления значения функции F(n), где n - целое число, задан следующими соотношениями:
F(n) = 4**4, если n < 5;
F(n) = 4 * F(n — 4) + 4, если n > 4.
Чему равно значение выражения F(4048)/F(4036)?
"""
'''sp = [0] * 4050

for i in range(1, 4050, 1):
    if i < 5:
        sp[i] = 4**4
    if i > 4:
        sp[i] = 4 * sp[i - 4] + 4

print(sp[4048] // sp[4036])  #  64'''

#  77755
#  Ermakov
'''№ 77755 (Уровень: Базовый)
(Л. Шастин). Алгоритм вычисления значения функции F(n), где n — целое число, задан следующими соотношениями:
F(n) = n ** n при п > 400;
F(n) = n + 6 + F(n + 12), если n <= 400.
Чему равно значение выражения F(72) — F(108)?
'''
'''sp = [0] * 413

for i in range(412, 71, -1):
    if i > 400:
        sp[i] = i ** i
    else:
        sp[i] = i + 6 + sp[i + 12]

print(sp[72] - sp[108])  #  270
'''
#  17679
'''17679 Пересдача 04.07.24 (Уровень: Базовый)
Алгоритм вычисления значения функции F(n), где n — натуральное число,
задан следующими соотношениями:
F(n) = 1 при n = 1;
F(n) = (n - 1) * F(n - 1), если n > 1.
Чему равно значение выражения (F(2024)/7 — F(2023))/F(2022)?'''

'''from sys import setrecursionlimit
setrecursionlimit(2030)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return(n + 1) * f(n - 1)

print((f(2024) - 3 * f(2023)) // f(2022))  #  4092528
'''
'''
sp = [0] * 2030

for i in range(2030):
    if i == 1:
        sp[i] = 1
    if i > 1:
        sp[i] = (i + 1) * sp[i - 1]

print((sp[2024] - 3 * sp[2023]) // sp[2022])  #  4092528
'''

# 20490
"""m = 0
for x in range(1, 2006):
    c1=0
    c4=0
    a = 4 ** 163 * 5 + 12 ** 62 - x
    while a > 0:
        if a % 5 == 1:
            c1+=1
        elif a % 5 == 4:
            c4+=1
        a = a // 5
    if c1 < c4:
        m = max(m, x)
print(m)  # 2000"""

# 16
"""def f(n):
    if n > 2000:
        return 16
    else:
        return 2 * f(n + 3)


print(f(50) / f(110))  # 1048576"""

# 17557
"""from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n * f(n - 1)

for i in range(2025):
    f(i)

print((f(2024) // 16 - f(2023)) / f(2022))"""

"""f = [0]
for n in range(1, 2025):
    if n == 1:
        f.append(1)
    if n > 1:
        f.append(2 * n * f[n - 1])
print((f[2024] // 16 - f[2023]) / f[2022])"""

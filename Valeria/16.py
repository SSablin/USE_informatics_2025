'''ЕСЛИ МЫ  ВОЗВРАЩАЕМ ПРЕДЫДУЩИЙ ЭЛЕМЕНТ, ТО НУЖНО НАЧИНАТЬ С НАЧАЛА
for i in range(0, 10**10, 1):
ЕСЛИ МЫ ВОЗВРАЩАЕМ СЛЕДУЮЩИЙ ЭЛЕМЕНТ, ТО НУЖНО НАЧИНАТЬ С КОНЦА
for i in range(10**10, 0, -1)'''


'''def f(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + f(n - 1)
    if n > 1 and n % 2 == 1:
        return 3 * f(n - 2)


print(f(25))'''
'''
sp = [0] * 26

for i in range(1, 26, 1):
    if i == 1:
        sp[i] = 1
    if i % 2 == 0:
        sp[i] = i + sp[i - 1]
    if i > 1 and i % 2 == 1:
        sp[i] = 3 * sp[i - 2]

print(sp[25])
'''

'''
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n > 2:
        return f(n - 1) * n + f(n - 2) * (n - 1)


print(f(8))'''

'''
def f(n):
    if n <= 2:
        return 0
    if n > 2:
        return g(n - 2)


def g(n):
    if n <= 1:
        return 0
    if n > 1:
        return f(n - 1) + n


print(f(8))
'''

# SS
'''from sys import setrecursionlimit
setrecursionlimit(1901)


def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 2 * f(n - 1)


print(f(1900) // 2**1890)
'''
# Valeria
'''
from functools import lru_cache
@lru_cache(None)


def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 2 * f(n - 1)


for i in range(2, 1900):
    f(i)
print(f(1900) // 2**1890)
'''
'''
from sys import setrecursionlimit
setrecursionlimit(3000)


def f(n):
    if n <= 2:
        return 1
    if n > 2:
        return n * f(n - 2)


print(f(3000) // f(2996))'''

'''
sp = [0] * 2024

for i in range(1, 2024, 1):
    if i == 1:
        sp[i] = 2
    if i == 2:
        sp[i] = 2
    if i > 2:
        sp[i] = i * (i - 1) + sp[i - 1] + sp[i - 2]

print(sp[2023] - sp[2021] - 2 * sp[2020] - sp[2019])
'''


# ручной метод
# print((2023 * 2022) + (2022 * 2021) + (2021 * 2020))
'''
from sys import setrecursionlimit
setrecursionlimit(2030)


def f(n):
    if n >= 2025:
        return n
    if n < 2025:
        return n + f(n + 2)


print(f(2020) - f(2023))
'''

'''
sp = [0] * 1001
c = 0

for i in range(1000, 0, -1):
    if i > 25:
        sp[i] = 2 * i * i * i + 1
    if i <= 25:
        sp[i] = sp[i + 2] + 2 * sp[i + 3]

for i in range(1, 1001):
    if sp[i] % 11 == 0:
        c += 1

print(c) # 91


# Чтобы исправить первый вариант, вам нужно заполнять массив sp в правильном порядке, например, с конца:
# Теперь значения в массиве sp будут вычисляться корректно, и вы получите правильный ответ.

c = 0

def f(n):
    if n > 25:
        return 2 * n * n * n + 1
    if n <= 25:
        return f(n + 2) + 2 * f(n + 3)


for i in range(1, 1001):
    if f(i) % 11 == 0:
        c += 1

print(c) # 91
'''

'''ЕСЛИ МЫ  ВОЗВРАЩАЕМ ПРЕДЫДУЩИЙ ЭЛЕМЕНТ, ТО НУЖНО НАЧИНАТЬ С НАЧАЛА
for i in range(0, 10**10, 1):
ЕСЛИ МЫ ВОЗВРАЩАЕМ СЛЕДУЮЩИЙ ЭЛЕМЕНТ, ТО НУЖНО НАЧИНАТЬ С КОНЦА
for i in range(10**10, 0, -1)'''

'''
sp = [0] * 2001
for i in range(2000, 0, -1):
    sp[i] = i
    print(i)
print(sp)'''

# 4651
'''
sp = [0] * 21

for i in range(1, 20):
    if i == 1:
        sp[i] = 0
    if i == 2:
        sp[i] = 1
    if i == 3:
        sp[i] = 1
    if i > 3:
        sp[i] = sp[i - 3] + sp[i - 2] + sp[i - 1]

print(sp[11])  # 149
'''
# 6925
'''
sp = [0] * 15

for i in range(1, 15):
    if i == 1:
        sp[i] = 1
    if i == 2:
        sp[i] = 2
    if i == 3:
        sp[i] = 3
    if i > 3:
        sp[i] = sp[i - 3] * i

print(sp[11])  # 880
'''
# 37151
'''
sp = [0] * 50

for i in range(1, 50):
    if i <= 1:
        sp[i] = 0
    if i > 1 and i % 2 == 1:
        sp[i] = sp[i - 1] + 3*i**2
    if i > 1 and i % 2 == 0:
        sp[i] = i//2 + sp[i - 1] + 2

print(sp[49])  # 62820
'''
# 61362
'''
sp = [0] * 1005

for i in range(1004, 1, -1):
    if i >= 1000:
        sp[i] = 1000
    if i < 1000 and i % 2 == 1:
        sp[i] = i * sp[i + 1]
    if i < 1000 and i % 2 == 0:
        sp[i] = i * (sp[i + 1] // 2)

print(sp[998] // sp[1001])  # 498501
'''
# 7273
'''
sp = [0] * 5

for i in range(1, 5):
    if i == 1:
        sp[i] = 1
    if i > 1:
        sp[i] = sp[i - 1] * (2 * i + 1)

print(sp[4])  # 315
'''


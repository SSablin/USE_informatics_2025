"""s = open('files/24_1.txt').readline()

sub = ''
m = ''
for i in range(len(s)):
    if s[i] == 'B':
        sub = ''
        for j in range(i, len(s)):
            if s[j] == 'B':
                sub += s[j]
                m = max(sub, m, key=len)
            else:
                break
print(m, len(m))  # 11"""

"""s = open('files/24_2.txt').readline()
m = ''
sub = ''
for i in range(len(s) - 1):
    if s[i] <= s[i+1]:
        sub += s[i + 1]
        m = max(sub, m, key=len)
    else:
        sub = 'X'
print(m, len(m))"""

"""s = open('files/24_3.txt').readline()
l = '13579'

m = ''
for i in range(len(s)):
    sub = s[i]
    for j in range(i, len(s) - 1):
        if s[j] in l and s[j + 1] in l and s[j] <= s[j + 1]:
            sub += s[j + 1]
            if len(sub) > len(m):
                m = sub
        else:
            break

print(m, len(m))"""

"""s = open('files/24_5.txt').readline()

while 'PP' in s: s = s.replace('PP', 'P P')

m = ''
for c in s.split():
    if len(c) > len(m):
        m = max(m, c, key=len)
print(m, len(m))  # 188"""

"""s = open('files/24_8.txt').readline()
s = s.replace('XYZ', 'A')

k = 0
m = 0
for i in range(len(s)-2):
    if s[i] == 'A':
        k += 1
        m = max(m, k)
    else:
        k = 0
print(m*3)  # 66"""

# №27691
"""s = open('files/zadanie24_1.txt').readline()
sub = ''
m = ''
for i in range(len(s) - 1):
    if s[i] == 'A' and s[i+1] == 'A':
        sub += s[i]
    else:
        sub += s[i]
        m = max(sub, m, key=len)
        sub = ''
print(m, len(m))  # 7"""

# 27694
# Подобрал
"""s = open('files/zadanie24_1.txt').readline()

m = ''
sub = ''
for i in range(1, len(s) - 1, 2):
    if s[i] + s[i+1] == 'AB':
        sub += s[i] + s[i+1]
    else:
        # sub += s[i]
        m = max(sub, m, key=len)
        sub = ''
print(m, len(m))  # 24"""

# 27688
"""s = open('files/24_demo.txt').readline()

sub = ''
m = ''
for i in range(len(s)):
    if s[i] == 'Z':
        sub += s[i]
    else:
        m = max(sub, m, key=len)
        sub = ''
print(m, len(m))  # 7"""

# 64909

# UVWXYZ

"""s = open('files/24_64909.txt').readline().strip()
d = {'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}
l = 0
maxi = 0
for i in range(len(s)):
    if s[i] in 'UVWXYZ':
        d[s[i]].append(i)
        if len(d[s[i]]) > 100:
            if d[s[i]][0] + 1 > l:
                l = d[s[i]][0] + 1
            del d[s[i]][0]
    maxi = max(maxi, i - l + 1)
print(maxi)"""

# 55820

"""s = open('files/24_55820.txt').readline().strip()
c = 1
m = 0

for i in range(len(s) - 2):
    if s[i] in 'QRS' and s[i + 1] in 'QRS':
        m = max(m, c)
        c = 1
    else:
        c += 1

m = max(m, c)
print(m)  # 544"""

# 27698

"""s = open('files/24_27698.txt').readline().strip()
s = s.replace('L', ' ')
s = s.replace('D', ' ')
m = ''
for c in s.split():
    if len(c) > len(m):
        m = c
print(m, len(m))"""

# 27699
# s = open('files/24_27699.txt')


# 39253
"""Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). 
Определите максимальное количество идущих подряд символов, среди которых не более одной буквы D."""
"""s = open('files/24_39253.txt').readline().split('D')
m = 0
for i in range(len(s) - 1):
    m = max(m, len(s[i]) + len(s[i + 1]) + 1)
print(m)  # 354"""

"""
f = open('files/24_39253.txt')
s = f.readline()
k = []
mx = 0
for i in range(len(s)):
    if s[i] == 'D':
        k.append(i) 
for j in range(len(k) - 2):
    c = k[j + 2] - k[j] - 1
    mx = max(mx ,c)
print(mx)  # 354"""

# 59849
"""Текстовый файл состоит не более чем из 10**6 символов латинского алфавита. 
Необходимо найти самую длинную подстроку, 
содержащую символы из алфавита 26-ричной системы счисления. 
В ответ записать длину последовательности символов, 
которая может являться числом в 26-ричной системе счисления."""

# 59849
"""from string import ascii_uppercase

s = open('files/24_59849.txt').readline().strip()
r26 = ascii_uppercase[:16]

for f in ascii_uppercase[16:]:
    s = s.replace(f, ' ')

m = 0
for c in s.split():
    m = max(m, len(c))
print(m)  # 41"""

# 27689

"""Текстовый файл состоит не более чем из 10**6 символов X, Y и Z. 
Определите максимальную длину цепочки вида XYZXYZXYZ... 
(составленной из фрагментов XYZ, последний фрагмент может быть неполным)."""

"""
s = open('files/24_27689.txt').readline().strip()
s = s.replace('XYZ', '*')

sub = ''
m = ''
for i in range(len(s)):
    if s[i] == '*':
        sub += 'XYZ'
    elif s[i] == 'X':
        sub += s[i]
        m = max(m, sub, key=len)
        sub = ''
    else:
        m = max(m, sub, key=len)
        sub = ''
print(m, len(m))  # 13"""

"""f = open('files/24_27689.txt').readline()
k = m = 0
for i in range(len(f)):
    if (f[i] == 'X' and k % 3 == 0) or (f[i] == 'Y' and k % 3 == 1) or (f[i] == 'Z' and k % 3 == 2):
        k += 1
        m = max(m, k)
    elif f[i] == 'X':
        k = 1
    else:
        k = 0
print(m)  # 13"""

"""from re import findall

s = open('files/24_27689.txt').readline().strip()

expr = findall('(?:XYZ)+(?:XY|X)', s)
ans = max(expr, key=len)
print(ans, len(ans))  # 13"""

"""Текстовый файл состоит из символов А, В, С, D, Е, F и G.
Определите в прилагаемом файле максимальное количество
идущих подряд символов
(длину непрерывной подпоследовательности), среди которых символ А встречается не
более 350 раз.
Для выполнения этого задания следует написать программу."""
"""s = open('files/24var02.txt').readline()

l = 0
m = 0
k = 0

for r in range(len(s)):
    if s[r] == 'A':
        k += 1
    while k > 350:
        if s[l] == 'A':
            k -= 1
        l += 1
    if k <= 350:
        m = max(m, r - l + 1)
print(m)  # 88024"""

"""Текстовый файл 24-157.txt состоит не более чем из 10**6 символов и содержит только
заглавные буквы латинского алфавита (ABC...Z). Определите символ, который чаще всего
встречается в файле между двумя одинаковыми символами. Например, в тексте
ССВААВАВСВС есть комбинации АВА, ВАВ, ВСВ и СВС. Чаще всего — 2 раза — между двумя
одинаковыми символами стоит В, в ответе для этого случая надо написать В2 (без
пробелов и других разделителей). Если таких символов несколько, выведите тот, который
стоит раньше в алфавите."""
"""
from string import ascii_uppercase

s = open('files/24-157.txt').readline()
ans = []
for i in range(len(s) - 2):
    if s[i] == s[i+2]:
        ans.append(s[i+1])

counts = [[letter, ans.count(letter)] for letter in ascii_uppercase]

# Находим элемент с максимальным count
max_letter, max_count = max(counts, key=lambda x: x[1])

print(max_letter, max_count)  # W 1608"""

# 19254

"""s = open('files/24_19254.txt').readline()

l = 0
m = 0
k = 0

for r in range(len(s) - 3):
    if s[r:r+4] == 'FSRQ':
        k += 1

while k > 80:
    if s[r:r + 4] == 'FSRQ':
        l -= 1"""

"""(Д. Бахтиев) Текстовый файл состоит не более чем из 10**7 латинских символов из набора А, В, С, D, Е, F, G, Н.
Определите подстроку наибольшей длины, начинающуюся и заканчивающуюся подстрокой вида «Согласная + Согласная
+ Гласная» и не содержащую внутри себя другие подстроки такого вида. В ответе укажите одно число наибольшую длину
такой подстроки.
для выполнения этого задания следует написать программу."""

"""s = open('files/24_18186.txt').readline()
gl = 'AE'
so = 'BCDFGH'

m = ''
for i in range(len(s) - 2):
    if s[i] in so and s[i+1] in so and s[i+2] in gl:
        sub = s[i:i+3]
        for j in range(i+3, len(s) - 2):
            sub += s[j]
            if s[j] in so and s[j+1] in so and s[j+2] in gl:
                sub += s[j+1] + s[j+2]
                m = max(m, sub, key=len)
                break

print(m, len(m))  # 64"""

# 18536 Сергей Горбачев
"""s = open('files/24_18536.txt').readline().strip()

while '-' in s: s = s.replace('-', '*')
while '**' in s: s = s.replace('**', ' ')
for n in '6789': s = s.replace(n, '6')

m = ''
for c in s.split():
    if len(c) > len(m):
        for i in range(len(c) - 1):
            if c[i:i+2] not in ('01', '00'):
                sub = ''
                for j in range(i, len(c)):
                    if c[j:j+3] not in ('*06', '*00', '*0*'):
                        sub += c[j]
                    else:
                        break
                if sub and sub[0] not in '*-':
                    if len(sub) > len(m):
                        m = sub
print(len(m), m)  # 128"""

"""s = open('files/24_18536.txt').readline().strip()

from re import *

expr = findall('(?:[6-9][0, 6-9]*)(?:[-*](?:[6-9][0, 6-9]*))*', s)

ans = max((str(x) for x in expr), key=len)
print(len(ans), ans)  # 128"""

# №59789
"""Текстовый файл состоит не более чем из 10^6 символов латинского алфавита. 
Определите длину самой длинной непрерывной подпоследовательности, 
где символ Y встречается не более 100 раз. 
Для выполнения этого задания следует написать программу."""

"""s = open('files/24_59789.txt').readline()

l = 0
k = 0
m = 0

for r in range(len(s)):
    if s[r] == 'Y':
        k += 1

    while k > 100:
        if s[l] == 'Y':
            k -= 1
        l += 1

    if k <= 100:
        m = max(m, r - l + 1)

print(m)  # 169"""

# №57431
"""Текстовый файл состоит из символов, 
обозначающих прописные буквы латинского алфавита.
Определите максимальное количество идущих подряд символов, 
среди которых никакие две буквы из набора букв A, B и C (с учетом повторений) не записаны подряд.
Для выполнения этого задания следует написать программу."""
# №57431
# V1
"""from itertools import product

s = open('files/24_57431.txt').readline()
sl = [''.join(x) for x in product('ABC', repeat=2)]
print(sl)  # ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']

m = ''
sub = ''
for i in range(len(s) - 1):
    if s[i] + s[i+1] not in sl:
        sub += s[i]
    else:
        sub += s[i]
        m = max(m, sub, key=len)
        sub = ''
print(len(m), m)  # 84
for w in sl:
    print(w, m.count(w))"""

# V2
"""from itertools import product

s = open('files/24_57431.txt').readline()
sl = [''.join(x) for x in product('ABC', repeat=2)]
print(sl)  # ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']

for w in sl:
    while w in s:
        s = s.replace(w, f'{w[0]} {w[-1]}')

mx = max(s.split(), key=len)
print(len(mx), mx)  # 84
for w in sl:
    print(w, mx.count(w))"""

# Решу егэ
"""s = open('files/24_57431.txt').read().strip()
s = s.replace('A', '*')
s = s.replace('B', '*')
s = s.replace('C', '*')
maxi = 1
count = 1
for i in range(1, len(s)):
    if s[i-1]+s[i] != '**':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)  # 84"""


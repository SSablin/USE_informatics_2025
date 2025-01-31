# 8
'''k = 0
for x1 in 'АБВГ':
    for x2 in 'АБВГ':
        for x3 in 'АБВГ':
            for x4 in 'АБВГ':
                for x5 in 'АБВГ':
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count('А') == 1:
                        k += 1
print(k)'''
'''
k = 0
bykv = 'ЕСАУЛ'
for x1 in bykv:
    for x2 in bykv:
        for x3 in bykv:
            for x4 in bykv:
                for x5 in bykv:
                    s = x1 + x2 + x3 + x4 + x5
                    if s.count(x1) == 1 and  \
                            s.count(x2) == 1 and \
                            s.count(x3) == 1 and \
                            s.count(x4) == 1 and \
                            s.count(x5) == 1:
                        if s.count('ЕА') == 0 and \
                                s.count('АЕ') == 0 and \
                                s.count('ЕУ') == 0 and \
                                s.count('УЕ') == 0 and \
                                s.count('АУ') == 0 and \
                                s.count('УА') == 0:
                                k += 1

print(k)'''

'''
k = 0
b = 'БЕЛКА'
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                if s.count('Б') == 1:
                    k += 1
print(k)'''

'''
b = 'КАТЕР'
k = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s[0] == 'Р' and s[-1] == 'К':
                            k += 1
print(k)'''
'''
b = 'КБЛА'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if s.count('К') == 1 and \
                            s.count('Б') == 1 and \
                            s.count('Л') == 1 and \
                            s.count('А') == 3:
                            if s.count('АА') == 0:
                                    c += 1
print(c)'''
'''
b = 'ЕГЭ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            if x1 == 'Э' or x1 == 'Е':
                s = x1 + x2 + x3
                c += 1

print(c)'''
'''
b = 'СОЛВЕЙ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        if x1 != 'Й' and x6 != 'Й' and s.count('ЙЕ') == 0 and s.count('ЕЙ') == 0 and s.count('Й') <= 1:
                            c += 1

print(c)'''
'''
b = '01234567'
c = 0
for x1 in '1234567':
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        for x7 in b:
                            s = x1 + x2 + x3 + x4 +x5 + x6 + x7
                            if s.count(x1) == 1 and s.count(x2) == 1 and s.count(x3) == 1 and s.count(x4) == 1 and s.count(x5) == 1 and s.count(x6) == 1 and s.count(x7) == 1:
                                if int(x1) % 2 == 0 and int(x2) % 2 != 0 and int(x3) % 2 == 0 and int(x4) % 2 != 0 and int(x5) % 2 == 0 and int(x6) % 2 != 0 and int(x7) % 2 == 0:
                                    c += 1
                                if int(x1) % 2 != 0 and int(x2) % 2 == 0 and int(x3) % 2 != 0 and int(x4) % 2 == 0 and int(x5) % 2 != 0 and int(x6) % 2 == 0 and int(x7) % 2 != 0:
                                    c += 1


print(c)'''
'''
b = 'АЕИО'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                c += 1
                if c == 248:
                    print(s)'''
'''b = 'ИКНОТ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                c += 1
                if x1 == 'О':
                    break
print(c)'''

#№ 17799 (Уровень: Средний)
'''
b = 'AГЕМНРТУ'
c = 0
max_c = -10**10
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                c += 1
                if s in b and x1 != x2 != x3 != x4:
                    if c > max_c:
                        max_c = c
print(max_c) #2424
'''


#№ 17671 Передача 04.07.24 (Уровень: Базовый)
'''
b = 'АЙЛМ'
c = 0
max_c = -10**10
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    s = x1 + x2 + x3 + x4 + x5
                    c += 1
                    if s.count('М') == 0 and \
                        s.count('Л') == 0 and \
                        s.count('ЙЙ') == 0:
                        if c > max_c:
                            max_c = c
print(max_c)'''

#№ 17862 Демоверсия 2025 (Уровень: Базовый)
'''b = '0123456789AB'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    s = x1 + x2 + x3 + x4 + x5
                    if x1 != '0' and \
                        s.count('7') == 1 and \
                        s.count('9') + s.count('A') + s.count('B') <= 3:
                        c += 1
print(c)'''

#№ 18049 (Уровень: Базовый)
'''
b = '012345678'
n = '0246'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        for x7 in b:
                            s = x1 + x2 + x3 + x4 + x5 + x6 + x7
                            if not(x1 in n) and not(x5 == x6 == x7):
                                c += 1
print(c)'''

#ДЗ номера 8
#10
'''
b = 'МУЖЧИНА'
c = 1
ans = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    for x6 in b:
                        k = 0
                        s = x1 + x2 + x3 + x4 + x5 + x6
                        for i in s:
                            if s.count(i) == 1:
                                k += 1
                        if x1 != 'Ч' and \
                                (s.count('Ж') == 1) and \
                                (s.count('М') < 2) and \
                                (s.count('У') < 2) and \
                                (s.count('Ч') < 2) and \
                                (s.count('И') < 2) and \
                                (s.count('Н') < 2) and \
                                (s.count('А') < 2):
                            c += 1
                            if c % 2 != 0:
                                ans += 1
print(ans)
'''

#11
'''
b = sorted('АЛГОРИТМ')
c = 0
k = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if x1 != 'Г' and s.count('И') >= 2:
                        if k % 2 != 0:
                            c += 1
print(c)
'''
#6
'''
b = 'МЕТРО'
sogl = 'МТР'
glas = 'ЕО'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                if x1 in sogl and x4 in glas:
                    c += 1
print(c)'''
'''
b = 'ГАФНИЙ'
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                if x1 != 'Й' and (s.count('А') + s.count('И') >= 1):
                    c += 1
print(c)'''

'''
c = 0
b = '01234567'
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                if x1 != '0':
                    f = 0
                    for i in range(0, 8):
                        if s.count(str(i)) == 1:
                            f += 1
                    if f == 2:
                        f = 0
                        for j in range(0, 8):
                            if s.count(str(j) * 2) == 1:
                                f += 1
                        if f == 1:
                            c += 1
                            print(c, s)
print(c)'''

# Урок 29.09.24
'''
c = 0
c_max = 0
b = ('АЙЛМ')
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    s = x1 + x2 + x3 + x4 + x5
                    c += 1
                    if s.count('М') == 0 and s.count('Л') == 0 and s.count('ЙЙ') == 0:
                        c_max = max(c_max, c)

print(c_max)
'''
'''
c = 0
k = 0
b = sorted('ФЛАМИНГО')

for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                for x5 in b:
                    s = x1 + x2 + x3 + x4 + x5
                    k += 1
                    if x1 != 'Н' and s.count('О') <= 1 and k % 2 != 0:
                        c += 1
print(c)
'''
'''from itertools import *

c = 0
k = 0
for i in product(sorted('ФЛАМИНГО'), repeat=5):
    s = ''.join(i)
    k += 1
    if s[0] != 'Н' and s.count('О') <= 1 and k % 2 != 0:
        c += 1
print(c)'''

#14225
'''
b = sorted("ABCDEXZ")
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                if (x1 in "XZ") and (x2 in "XZ") and (x3 in "ABCDE") and (x4 in "ABCDE"):
                    c += 1
print(c)'''

#39237
'''
b = sorted("АВТОР")
c = 0
for x1 in b:
    for x2 in b:
        for x3 in b:
            for x4 in b:
                s = x1 + x2 + x3 + x4
                c += 1
                if s == "ТАРА":
                    print(c)
'''
"""from string import *
for x in (digits+ascii_uppercase)[:25]:
    a = int(f'1{x}2{x}3{x}4{x}5', 25) + int(f'2{x}024', 25) + int(f'1{x}099', 25)
    if a % 24 == 0:
        print(a // 24)  # 6260270029"""



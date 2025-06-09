#  16
'''
from sys import *
setrecursionlimit(2500)

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (n - 1) * f(n - 1)

print((f(2024) + 2 * f(2023))/f(2022))'''

#  13
'''
from itertools import product

c = 0
for i in product('01', repeat=11):
    s = ''.join(i)
    if s.count('1') != 2 and s.count('1') != 7:
        c += 1
print(c)'''

'''
sp = [0, 1]
for i in range(2, 2025):
    sp.append((i - 1) * sp[i - 1])
print((sp[2024] + 2 * sp[2023]) // sp[2022])
'''

#  15
'''
for p in range(2):
    for q in range(2):
        for a in range(2):
            print(p, q, a, (p <= ((q and not(a)) <= (not(p)))))
'''

#  14
#  2)
'''a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2*25**4 - 2025
s = ''
while a != 0:
    s += str(a % 25)
    a = a // 25
s += str(a)
print(s)'''

'''a = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2*25**4 - 2025
c = 0
while a > 0:
    if a % 25 == 0:
        c += 1
    a //= 25
print(c)'''
'''
max = -10**10
for x in range(10):
    a1 = '98897' + str(x) + '21'
    a2 = '2' + str(x) + '923'
    a = int(a1) + int(a2)
    #print(a)
    x = ''
    if a % 18 == 0:
        #print(a)
        # перевести в 10-ричную
        for i in range(len(str(a))):
            #print(a)
            b = (str(a)[::-1])
            print(b)
            x += str(b[i] * i)[::-1]
            print(x)
            
'''

#  24
'''import re

f = open('files/demo_2025_24.txt').readline()
example = '0006789*00*789*-789*789'
res = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))*', example)
print(res)
res_max = [len(x) for x in res]
print(max(res_max))

'''

#  25
'''
from fnmatch import *

for n in range(1917, 10 ** 10 + 1, 1917):
    if fnmatch(str(n), '3?12?14*5'):
        print(n, n // 1917)

'''

#  5 59827
'''
def v3(x):
    r = ''
    while x > 0:
        r = str(x % 3) + r
        x //= 3
    return r

max_r = 0

for n in range(1, 100):
    r = v3(n)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + v3((n % 3) * 5)
    r = int(r, 3)
    if r <= 173:
        max_r = max(max_r, r)
print(max_r)'''

#  5 29113
'''8 битная запись числа N'''
'''
for n in range(128, 256):
    r = bin(n)[2:]
    if len(r) < 8:
        r = (8 - len(r)) * '0' + r
    res = ''
    for i in r:
        if i == '1':
            res += '0'
        else:
            res += '1'
    res = n - int(res, 2)
    if res == 185:
        print(n)
'''

# 2
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x and y and (not (z))) == (y or z or not(w)))
                if F == True:
                    print(x, y, z, w, F)
'''
'''
x y z w F
x y z w F
0 0 0 1 True
1 0 0 1 True
#           1 1 0 0 True
1 1 0 1 True
'''
# wyzx
# 1101
# 1000
# 1001

# № 13091 (Уровень: Средний)
'''
for i in range(1, 200):
    n = format(i, 'b')
    n += format((int(n) % 4), 'b')

    r = int(n, 2)
    print(r) 
'''
# № 17859 Демоверсия 2025 (Уровень: Базовый)
'''
r_max = -10**10
for i in range(1, 13):
    n = format(i, 'b')
    if i % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'

    r = int(n, 2)
    if r > r_max:
        r_max = r
print(r_max) #109

# № 17765 (Уровень: Базовый)
min_r = 10**10
for i in range(1, 200):
    n = format(i, 'b')
    if n.count('1') % 2 == 0:
        n += '11'
    else:
        n += '01'

    r = int(n, 2)
    if 61 < r < min_r:
        min_r = r
print(min_r) # 63

# № 17668 Пересдача 04.07.24 (Уровень: Базовый)
min_r = 10**10
for i in range(28, 200):
    n = format(i, 'b')
    if n.count('1') % 2 == 0:
        n = '10'+ n[2:] + '0'
    else:
        n = '11' + n[2:] + '1'

    r = int(n, 2)
    if r < min_r and i > 27:
        min_r = r
print(min_r)

# № 17624 Основная волна 19.06.24 (Уровень: Базовый)
min_r = 10**10
for i in range(1, 200):
    n = format(i, 'b')
    n += str(n.count('1') % 2)
    n += str(n.count('1') % 2)

    r = int(n, 2)
    if r > 75 and r < min_r:
        min_r = r
print(min_r)

# № 17546 Основная волна 08.06.24 (Уровень: Базовый)
max_r = -10**10
for i in range(1, 200):
    n = format(i, 'b')
    if int(n) % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'

    r = int(n, 2)
    if r > min_r and i <= 12:
        min_r = r
print(min_r)
'''
# № 16252 Джобс 03.05.24 (Уровень: Средний)
'''
def v3(x):
    v = ''
    while x != 0:
        v += str(x % 2)
        x //= 2
    v += str(x)
    return v[::-1]
print(v3(14))
'''
'''

for i in range(500, 2000):
    r = bin(i)[2:]
    while r[0] == '1':
        r = r[1:]

    res = i - int(r, 2)
    print(res)'''
'''
def F(n):
    if n <= 400:
        return n + 6 + F(n + 12)
    if n > 400:
        return n**n
print(F(72) - F(108), '1')

#1538
#270
sp = [0] * 413
for i in range(412, 71, -1):
    if i > 400:
        sp[i] = i ** i
    else:
        sp[i] = i + 6 + sp[i + 12]

#print(sp[72] - sp[108])'''

# №24 № 17878
'''
import re # регулярные выражения

f = open('files/24_17878.txt').readline()
example = '0006789*00*789*-789*789'
res = re.findall(r'(?:0|[6-9][06-9]*)(?:[-*](?:0|[6-9][06-9]*))+', example)
print(res)
res_max = [len(x) for x in res]
print(max(res_max))
'''
'''
f = open('files/24_17756.txt').readline()
print(f[:40])
f = f.replace('++', '+ +')
print(f[:40])
f = f.replace('**', '* *')
print(f[:40])
f = f.replace('*+', '* +')
print(f[:40])
f = f.replace('+*', '+ *')
print(f[:40])

res = f.split(' ')
print(res[:10])
res_max = [len(x) for x in res]
print(max(res_max))'''
# 24 17756

'''from itertools import product

f = open('files/24_17756.txt').readline()
c = [''.join(x) for x in product('+*-/', repeat=2)]
for i in c:
    f = f.replace(i, (i[0] + ' ' + i[1]))

res = f.split(' ')

res_max = [len(x) for x in res]

print(max(res_max))
'''
#  № 16388 ЕГКР 27.04.24 (Уровень: Базовый)
'''Текстовый файл состоит из символов K, L, M и N. 
В прилагаемом файле определите максимальное количество символов в непрерывной подпоследовательности,
состоящей из идущих подряд групп символов KLMN в указанном порядке, 
при этом в начале и в конце искомой последовательности группа символов KLMN может быть неполной.
Искомая последовательность должна содержать не менее одной полной группы символов KLMN. 
Например, условию задачи удовлетворяют: MNKLMNKLMNK, или NKLMNKLMNKL, или KLMNKLMNKLM и т.п.
Для выполнения этого задания следует написать программу.'''
'''
from itertools import product

f = open('files/24_16388.txt').readline()
k = m = 0
for i in range(len(f)):
    if f[i:i+2] in 'KLMN':
        k += 1
        m = max(k, m)
    else:
        k = 0
print(m)
'''
# № 18049 (Уровень: Базовый)
'''
from itertools import product
c = 0
#t = ['000', '111', '222', '333', '444', '555', '666', '777', '888']

for i in product('012345678', repeat=7):
    s = ''.join(i)
    if (s[0] not in '0246') and not(s[-1] == s[-2] and s[-2]== s[-3]): #(s[-3:] not in t):
        c += 1

print(c)
'''
#  17862
'''
from itertools import product
c = 0
for i in product('0123456789AB', repeat=5):
    s = ''.join(i)
    #print(s)
    if s[0] != '0' and s.count('7') == 1 and s.count('9') + s.count('A') + s.count('B') <= 3:
        c += 1
print(c)

from itertools import *
c = 0
for x in product ('0123456789ab', repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('7') == 1 and s.count('9') + s.count('a') + s.count('b') <= 3:
        c += 1
print(c)'''

#  10799
'''
s1 = 'КРБЛК'
s2 = 'ОАИ'
ans = set()

for c1 in s1:
    for c2 in s2:
        for c3 in s1:
            for c4 in s2:
                for c5 in s1:
                    for c6 in s2:
                        s = c1 + c2 + c3 + c4 + c5 + c6
                        mn = set(s)
                        if len(mn) == len(s):
                            ans.add(s)
                            print(s)
print(len(ans))'''

#  17685 24
#  Алексей Кабанов
'''
s = open('files/24_17685.txt').readline()

s = s.replace('++', ' ').replace('+*', ' ').replace('*+', ' ').replace('**', ' ')
#print(s[:500])

m = 0
for c in s.split(' '):
    if len(c) > m:
        for i in range(len(c)):
            if c[i] not in '*+':
                sub = ''
                for j in range(i, len(c)):
                    sub += c[j]
                    try:
                        if c[j] not in '*+' and eval(sub) == 0:  #eval = выполнение команды из строки
                            m = max(m, len(sub))
                    except:
                        pass
print(m)
'''
# SS
'''
import re

f = open('files/24_17685.txt').readline()
example = '0006789*1*1*00*785555555555559*+789*789'
res = re.findall(r'(?:0|[1-9][0-9]*)(?:[+*](?:0|[1-9][0-9]*))+', f)

m = 0
for c in res:
    if len(c) > m:
        for i in range(len(c)): #  с помощью первого цикла мы пробегаем по всему отрезку
            sub = ''
            for j in range(i, len(c)): #с помощью второго мы пробегаем во отрезку, убирая знаки с левого края
                sub += c[j]
                try:
                    if eval(sub) == 0:
                        m = max(m, len(sub))
                except:
                    pass
print(m)
'''
# AlexMath
'''
import re

s = open('files/24_17685.txt').readline().strip()

nn = r'[1-9]\d*'
zn = rf'(?:{nn}\*|0\*)*0(?:\*{nn}|\*0)*'
sum_prod = rf'{zn}(?:\+{zn})*'

arr = re.findall(f'{sum_prod}', s)

arr_len = [len(x) for x in arr]

print(max(arr_len))

import re  # Импортируем модуль re для работы с регулярными выражениями

# Открываем файл и читаем первую строку, удаляя лишние пробелы и символы новой строки
s = open('files/24_17685.txt').readline().strip()

# Определяем регулярное выражение для чисел, которые могут быть в выражении
nn = r'[1-9]\d*'  # Число, начинающееся с цифры от 1 до 9, за которой могут следовать другие цифры

# Определяем регулярное выражение для последовательностей умножения, заканчивающихся на 0
zn = rf'(?:{nn}\*|0\*)*0(?:\*{nn}|\*0)*'
# Это выражение ищет последовательности вида:
# - Число, за которым следует знак умножения, повторяющийся 0 или более раз
# - Затем обязательно идет 0
# - После 0 может идти знак умножения, за которым следует число или 0, повторяющийся 0 или более раз

# Определяем регулярное выражение для последовательностей сложения и умножения
sum_prod = rf'{zn}(?:\+{zn})*'
# Это выражение ищет последовательности вида:
# - Последовательность умножения, заканчивающаяся на 0
# - Затем может идти знак сложения, за которым следует такая же последовательность умножения, повторяющаяся 0 или более раз

# Ищем все совпадения с регулярным выражением в строке s
arr = re.findall(f'{sum_prod}', s)

# Создаем список длин найденных совпадений
arr_len = [len(x) for x in arr]

# Выводим максимальную длину найденных совпадений
print(max(arr_len))
'''
'''
def v3(x): # троичная чистема счисления (сам)
    s = ''
    while x > 2:
        s += str(x % 3)
        x = x // 3
    s += str(x)
    s = s[::-1]
    return s

a = 3
print(v3(a))
'''
#  № 18045 (Уровень: Базовый)
'''
(Л. Шастин) В файле содержится последовательность натуральных чисел. 
Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно. 
Определите количество пар последовательности, 
в которых сумма последних цифр элементов равна количеству двузначных чисел в последовательности. 
В ответе запишите количество найденных пар, затем минимальную из сумм элементов таких пар. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
Файлы к заданию:17.txt'''
'''
f = open('files/17_18045.txt')  # Открываем файл с данными
sp = []  # Создаем список для хранения чисел из файла
k2 = 0  # Счетчик двузначных чисел
ans1 = 0  # Счетчик пар, удовлетворяющих условию
ans2 = 10 ** 10  # Переменная для хранения минимальной суммы пары (изначально установлена в очень большое число)

for i in f:  # Читаем числа из файла и добавляем их в список sp
    sp.append(int(i))
    if int(i) // 100 == 0:  # Если число является двузначным (т.е. меньше 100), увеличиваем счетчик k2
        k2 += 1

for i in range(len(sp) - 1):  # Проходим по списку sp и проверяем каждую пару соседних элементов
    if sp[i] % 10 + sp[i + 1] % 10 == k2:  # Проверяем, равна ли сумма последних цифр элементов количеству двузначных чисел (k2)
        ans1 += 1  # Если условие выполняется, увеличиваем счетчик ans1
        if sp[i] + sp[i + 1] < ans2:  # Проверяем, является ли сумма элементов пары меньше текущего значения ans2
            ans2 = sp[i] + sp[i + 1]  # Если да, обновляем ans2

# Выводим количество найденных пар (ans1) и минимальную сумму пары (ans2)
print(ans1)  # 243
print(ans2)  # 3614
'''

# № 17873 Демоверсия 2025 (Уровень: Базовый)
'''	
В файле содержится последовательность натуральных чисел.
Её элементы могут принимать целые значения от 1 до 100 000 включительно. 
Определите количество пар последовательности, 
в которых остаток от деления хотя бы одного из элементов на 16 равен минимальному элементу последовательности. 
В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар. 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
Файлы к заданию:17.txt'''
'''
f = open('files/17_17873.txt')
sp = []
k1 = 0
k2 = -10 ** 10
for i in f:
    sp.append(int(i))
min_i = min(sp)  # 8

for i in range(len(sp) - 1):
    if sp[i] % 16 == min_i or sp[i + 1] % 16 == min_i:
        k1 += 1
        k2 = max(k2, sp[i] + sp[i + 1])

print(k1, k2)  # 1214 176024
'''
# № 5 17859
"""for i in range(1, 12):
        n = bin(i)[:-2]
        print(i, n)
        if int(n) % 2 == 0:
            n = '10' + n
        else:
            n = '1' + n + '01'

        r = int(n, 2)
        print(r)
"""
# 8 № 15320 Досрочная волна 2024 (Уровень: Базовый)
'''
from itertools import product
c = 0
for i in product(sorted("ПАРУС"), repeat=5):
    c += 1
    s = "".join(i)
    if s.count("АА") == 0 and s.count("У") <= 1:
        print(c)
        break
'''
# 15 № 17871 Демоверсия 2025 (Уровень: Базовый)
'''
def F(a, b, x):
    if a <= x <= b:
        return True
    return False

d = 10**10

for a in range(1, 100):
    for b in range(a, 100):
        k = 0
        for i in range(2, 200):
            x = i/2
            if (F(15, 40, x) <= ((F(21, 63, x) and (not(F(a, b, x)))) <= (not (F(15, 40, x))))):
                k += 1
        if k == 99+99:
            d = min(d, b-a)
print(d)'''
# 17 №17535
'''
f = open('files/24_17535.txt').readline() #f = 'ACDACDA' #f = 'AAACDAAACDAAAAAAAACDAAAAAAAA'
cd = []
icd = 0

for i in range(f.count('CD')):
    cd.append(f.index('CD', icd))
    icd = f.index('CD', icd) + 1
#print(len(cd)) #print(cd) #print(cd[0]) #print(f[74+1])

maxlen = max(cd[160] + 1, len(f) - cd[-161] - 1)
for i in range(len(cd) - 162):
    maxlen = max(maxlen, cd[i + 161] - cd[i])

print(maxlen) #9712
'''
# № 17866 Демоверсия 2025 (Уровень: Базовый)
'''
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 81 идущей подряд цифре 1? В ответе запишите полученную строку.
НАЧАЛО
  ПОКА нашлось (11111) ИЛИ нашлось (888)
    ЕСЛИ нашлось (11111)
      ТО заменить (11111, 88)
      ИНАЧЕ заменить (888, 8)
    КОНЕЦ ЕСЛИ
  КОНЕЦ ПОКА
КОНЕЦ'''
'''
s = '1' * 81
while ('11111' in s) or ('888' in s):
    if '11111' in s:
        s = s.replace('11111', '88', 1)
    else:
        s = s.replace('888', '8', 1)
print(s)
'''
# № 18032 (Уровень: Базовый)
#  SS
'''for i in range(1000, 10000):
    s = 0
    for j in range(1, 10000): #  может быть больше чисел и тогда не сработает
        if i % j == 0:
            s += j
    if str(s)[-2:] == '23':
        print(i, s)
'''
#  Ermakov
'''
def div(x):
    summa = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            summa.add(i)
            summa.add(x // i)
    return summa

for n in range(1000, 10000):
    s = div(n)
    summa = sum(s)  # Вычисляем сумму делителей
    if summa % 100 == 23:
        print(n, summa)
'''
#  deepseek
'''
def div(x):
    summa = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            summa += i
            if i != x // i:  # Добавляем парный делитель, если он не равен i
                summa += x // i
    return summa

for n in range(1000, 10000):
    s = div(n)
    if s % 100 == 23:
        print(n, s)
'''

# 15 № 17634 Основная волна 19.06.24 (Уровень: Базовый)
'''for a in range(1, 100):
    k = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if (x + y <= 30) or (y <= x + 2) or (y >= a):
                k += 1
    if k == 100*100:
        print(a)'''
# 15 № 17871 Демоверсия 2025 (Уровень: Базовый)

'''
print('P Q A F')
for P in range(2):
    for Q in range(2):
        for A in range(2):
            F = P <= ((Q and not A) <= (not P))
            if not F:
                print(P, Q, A, F)
'''

# 15 № 17678 Пересдача 04.07.24 (Уровень: Базовый)
'''
for a in range(1, 100):
    k = 0
    for x in range(0, 100):
        for y in range(0, 100):
            if (x + y <= 24) or (y <= x - 2) or (y >= a):
                k += 1
    if k == 100**2:
        print(a)
'''
# 15 № 17556 Основная волна 08.06.24 (Уровень: Базовый)

'''def f(n, m):
    if n % m == 0:
        return True
    return False


for a in range(300, 1, -1):
    k = 0
    for x in range(1, 301):
        for n in range(70, 91):
            for m in range(70, 91):
                if f(x, a) or (f(n, m) <= (not(f(x, 22)))):
                    k += 1
    if k == 300*20*20:
        print(a)
'''
'''
def f(x):
    return (x % a == 0) or ((70 <= x <= 90) <= (x % 22 != 0))


for a in range(100, 1 ,-1):
    if all(f(x) == 1 for x in range(1, 10000)):
        print(a)
        break'''

# 13 № 17767 (Уровень: Базовый)
# 1110 1100 00000000
'''
from ipaddress import *

network = ip_network(f'228.172.224.0/255.255.240.0', 0)
ans = 0

for ip in network:
    x = f'{ip:b}'
    if x.count('1') % 5 != 0:
        ans += 1
print(ans)

ans = 0
for i in range(2**12):
    if (bin(i).count('1') + 4 + 4 + 3) % 5 != 0:
        ans += 1

print(ans)
'''

# 2
"""for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not((not x) or y) or (y == z) or (not w))
                if not f:
                    print(x, y, z, w, f)"""
# 0 0 1 1 False
# 0 1 0 1 False
# 1 1 0 1 False
# wzyx

# 5
"""r_mx = 0
for i in range(500):
    n = oct(i)[2:]
    if int(n) % 2 == 0:
        for num in '1357':
            n = n.replace(num, '2')
    else:
        n = n.replace(n[0], '3').replace(n[-1], '3')
    r = int(n, 8)
    if r < 300:
        r_mx = max(r_mx, r)
print(r_mx)  # 294"""
# 6
"""from turtle import *
screensize(5000, 5000)
# tracer(0)
lt(90)
c = 20
for i in range(777):
    fd(25 * c)
    lt(90)
    fd(34 * c)
    lt(90)

up()

fd(12 * c)
lt(90)
fd(17 * c)
rt(90)

down()

for i in range(1996):
    fd(25 * c)
    lt(90)
    fd(17 * c)
    lt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'red')

exitonclick()
update()"""

# 7
"""from math import log2
print(log2(65536))  # 16
s = 1920 * 1080 * 16
print(s)
print(512 - 52)  # 460
for i in range(52, 460):
    if 460 % i == 0:
        print(i)  # 92
print((92 * s) / 8 / 1024 / 1024)  # 364"""

# 13 №20220
"""from ipaddress import *
ip = ip_address('111.233.75.16')
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if str(net.network_address) == '111.233.75.0':
        print(net.num_addresses)  # 256"""

# 14 №19898
"""def r7(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s


mx0 = []
for x in range(1, 10_000):
    s = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    s7 = r7(s, 7)
    mx0.append(s7.count('0'))
print(max(mx0))  # 203
for x in range(1, 10_000):
    s = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    s7 = r7(s, 7)
    if s7.count('0') == 203:
        print(x)  # 9604"""

# 15 №19899
"""def mod(m, n):
    return m % n


for a in range(1, 300):
    f = True
    for x in range(1, 300):
        if not ((a + 2 * x) > (400 - a) and ((mod(a, 100) + mod(120, a)) > 140)):
            f = False
    if f:
        print(a)  # 221
        break"""

# 16 №20071
"""def f(n):
    if n > 2000:
        return 16
    if n <= 2000:
        return 2 * f(n + 3)


sp = [int(x) for x in str(int(f(50) / f(110)))]
ans = 1
for x in sp:
    if x != 0:
        ans *= x
print(ans)  # 6720"""

# 17 №19900

"""
s = [int(x) for x in open('files/17_19900.txt')]

znach4 = []
for x in s:
    if len(str(abs(x))) == 4:
        znach4.append(x)
znach4 = sum(znach4)


def znach3(sp):
    c = 0
    for x in sp:
        if len(str(abs(x))) == 3:
            c += 1
    if c == 2:
        return True
    return False


ans = []
for i in range(len(s) - 2):
    if znach3(s[i:i + 3]):
        if (s[i] * s[i + 1] * s[i + 2]) > znach4:
            ans.append(s[i] * s[i + 1] * s[i + 2])
print(len(ans), abs(min(ans)))  # 566 1462000"""

# 24
# №19884
# re - не верно
"""from re import findall
s = open('files/24_19884.txt').readline()
expr = findall(f'(?:0|[6-9]+)(?:[*-]0|(?:[*-][6-9][0, 6-9]))', s)
print(expr)
print(len(expr))  # 584675"""

"""s = open('files/24_19884.txt').readline().strip()
s = s.replace('-', '*').replace('6', '7').replace('8', '7').replace('9', '7').replace('**', '* *').replace('**', '* *')

while '*00' in s:
    s = s.replace('*00', '*0 *0')
s = s.replace('*07', '*0 7')
count = 0
for x in s.split():
    sub = x.strip('*')
    cnt = sub.count('7') + sub.count('0')
    for t in sub.split('*'):
        cnt -= len(t)
        for i in range(len(t)):
            if t[i] == '7' or i == len(t) - 1:
                count += cnt
print(count)  # 30460483"""

# 26
# №20161
"""f = open('files/26_20161.txt')
n = int(f.readline())
data = sorted(list(map(int, s.split())) for s in f)  # стоимость, номер категории
data_even = sorted([x[0] for x in data if x[1] % 2 == 0])
data_odd = sorted([x[0] for x in data if x[1] % 2 == 1], reverse=True)
count_even_30 = int(0.7 * len(data_even))
discount_even = []
discount_odd = []
for i in range(len(data_even)):
    if i < count_even_30:
        new_price = data_even[i] * 0.7
        if round(new_price) - new_price < 0.0001:
            discount_even.append(round(new_price))
        else:
            discount_even.append(int(new_price))
    else:
        new_price = data_even[i] * 0.8
        if round(new_price) - new_price < 0.0001:
            discount_even.append(round(new_price))
        else:
            discount_even.append(int(new_price))

count_odd = int(0.25 * len(data_odd))
for i in range(len(data_odd)):
    if i < count_odd:
        new_price = data_odd[i] * 0.85
        if round(new_price) - new_price < 0.0001:
            discount_odd.append(round(new_price))
        else:
            discount_odd.append(int(new_price))
    else:
        discount_odd.append(data_odd[i])
ans1 = sum(discount_even) + sum(discount_odd)
ans2 = abs((sum(data_even) - sum(discount_even)) - (sum(data_odd) - sum(discount_odd)))
print(ans1, ans2)  # 4151899 464997"""

# 27 №20168
"""from math import dist


def get_centroid(c):
    r = []
    for p in c:
        r += [(sum(dist(p, p1) for p1 in c), p)]
    return min(r)[1]


a = [tuple(map(float, x.split())) for x in open('files/27_B_20168.txt')]
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a[:]:
            if dist(p1, p2) < 1:
                c[-1] += [p2]
                a.remove(p2)
print(len(c))
cs = [kl for kl in c if len(kl) >= 20]
cl = min(cs, key=len)
print(get_centroid(cl))
# A: 352342 343732
# B: 6446 857780"""

"""f = open('files/26_20910.txt')
N, M, K = [int(x) for x in f.readline().split()]
print(N, M, K)
min_ryad = [M + 1] * (K + 1)
for s in f:
    ryad, mesto = [int(x) for x in s.split()]
    min_ryad[mesto] = min(min_ryad[mesto], ryad)
m = []
for mesto in range(1, K):
    r = min(min_ryad[mesto], min_ryad[mesto + 1]) - 1
    if r == 21028:
        print(mesto, mesto + 1)  # 6660 6661
    m.append(r)
print(m)
print(max(m))  # 21028"""

# № 17643
"""f = open('files/26_17643.txt')
n = int(f.readline())

# f = ('10 100 1', '3 10 0', '10 100 0', '2 10 1', '10 100 0', '3 10 1', '11 100 0', '1 200 0')
# n = 8

data = [list(map(int, s.split())) for s in f]
data.sort(key=lambda x: x[1], reverse=True)
# ID cost status

middle_price = sum(x[1] for x in data) / len(data)
expensive = [x for x in data if x[1] > middle_price]
sailed_expensive_id = [x for x in expensive if x[2] == 0]
# 1
most_sailed_id = max(sailed_expensive_id.count(x) for x in sailed_expensive_id)
most_sailed = [x for x in sailed_expensive_id if sailed_expensive_id.count(x) == most_sailed_id]

# 2
mx_cost = max(x[1] for x in most_sailed)
most_sailed = [x for x in most_sailed if x[1] == mx_cost]
# 3
nt_sailed_id = [x[0] for x in data if x[0] == 0]
most_sailed = min([nt_sailed_id.count(x[0]), x] for x in most_sailed)[1]
print(most_sailed)
sm_most_sailed = most_sailed[1] * data.count(most_sailed)
c_most_sailed = len([x for x in data if x[0] == most_sailed[0] and x[2] == 1])
print(sm_most_sailed, c_most_sailed)  # 43656 36"""

# 26 №20396
"""
f = open('files/26_20396.txt')
n, m, k = map(int, f.readline().split())

# f = ['1 1', '6 6', '5 5', '6 7', '4 4', '2 2', '3 3']
# n, m, k = 7, 7, 8
# m - ряды, k - места
mn_ryad = [m + 1] * (k + 1)
for s in f:
    ryad, mesto = map(int, s.split())
    mn_ryad[mesto] = min(mn_ryad[mesto], ryad)


mx_r = []
mx_m = []
for i in range(1, k):
    r = min(mn_ryad[i], mn_ryad[i+1]) - 1
    if r == 88888:
        mx_m.append(i+1)
    mx_r.append(r)
print(max(mx_r), max(mx_m))  # 88888 68111"""

# 26 №21512
"""f = open('files/26_21512.txt')
n, m, k = map(int, f.readline().split())

# f = ['1 2', '2 3', '3 4', '4 5', '5 6', '6 7', '1 7', '2 8']
# n, m, k = 8, 6, 9  # кол-во (занятых, рядов, мест)

mn_ryad = [m + 1] * (k + 1)
for s in f:
    ryad, mesto = map(int, s.split())
    mn_ryad[mesto] = min(mn_ryad[mesto], ryad)

m_r = []
m_m = 0
for i in range(1, k-1):
    r = min(mn_ryad[i], mn_ryad[i+1], mn_ryad[i+2]) - 1
    if r == 1804:
        print(i)
        m_m = i
    m_r.append(r)
print(max(m_r), m_m)  # 1804 4434"""

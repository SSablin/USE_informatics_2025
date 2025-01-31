"""Полещенков советует: вариант от С. Горбачёва Вариант #4
Приближено по смыслу к ЕГЭ. Интересные задачи"""

# 2
"""print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not((x or y) <= w) or not(z and (not (y and w)))
                if not f:
                    print(x, y, z, w, f)"""
# x y z w F
# 0 0 1 0 False
# 0 0 1 1 False
# 1 0 1 1 False


# 5
"""На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число R следующим образом.
1. Строится пятеричная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:
а) если число чётно, то к этой записи слева дописывается З, а справа остаток от деления числа на 5;
б) если число нечётно, то к этой записи справа дописывается 4, а слева остаток от деления числа на 4.
Полученная таким образом запись является пятеричной записью искомого числа R.
З. Результат переводится в десятичную систему и выводится на экран.
Например, для исходного числа 6 = 115 результатом является число 31115 = 406, а для исходного числа 13 = 235 это число 12345 = 194
Укажите максимальное число R, которое может быть результатом данного алгоритма, при условии, что N не больше 15.
В ответе запишите это число в десятичной системе счисления."""

"""def pt(i):
    s = ''
    while i > 0:
        s = str(i % 5) + s
        i //= 5
    return s

r_max = 0
for i in range(1, 16):
    n = pt(i)
    if i % 2 == 0:
        n = '3' + n + str(i % 5)
    else:
        n = str(i % 4) + n + '4'
    r = int(n, 5)
    r_max = max(r_max, r)
print(r_max)  # 454"""

# 6

"""from turtle import *
tracer(0)
screensize(2000, 2000)

c = 10

lt(90)
for i in range(2):
    fd(77*c)
    rt(90)
    fd(101*c)
    rt(90)

up()

fd(29*c)
lt(90)
fd(44*c)
rt(90)

down()

for i in range(7):
    fd(88*c)
    rt(90)
    fd(75*c)
    rt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'green')

exitonclick()
update()  # 1410"""

# 8
"""Определите количество семеричных семизначных чисел, которые не начинаются с цифр З или 5, 
не оканчиваются чётными цифрами, а также содержат не более одного нуля."""

"""from itertools import product
c = 0
for i in product('0123456', repeat=7):
    s = ''.join(i)
    if s[0] not in '035' and s[-1] not in '0246' and s.count('0') <= 1:
        c += 1
        print(s, c)
print(c)  # 171072"""

# 9
"""Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
Определите сумму номеров строк таблицы, содержащих числа, для которых выполнены оба условия:
- в строке только одно чётное число повторяется трижды, остальные числа нечётные и различные;
- квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех её неповторяющихся чисел.
В ответе запишите только число."""
"""c = 0
id = []
for s in open('files/9_горбачев4.txt'):
    a = [int(x) for x in s.split()]
    c += 1
    chet = set()
    nchet = set()
    for x in a:
        if x % 2 == 0 and a.count(x) == 3:
            chet.add(x)
        if x % 2 != 0 and a.count(x) == 1:
            nchet.add(x)
    if len(chet) == 1 and len(nchet) == 3:
        if (sum(chet)*3)**2 > (sum(nchet))**2:
            print(a, c, chet, nchet)
            id.append(c)
print(sum(id))  # 266374"""

# 12
"""m = 0
for n in range(3, 101):
    s = '9' + n * '6'
    while '96' in s or '366' in s or '666' in s:
        if '96' in s:
            s = s.replace('96', '6', 1)
        if '366' in s:
            s = s.replace('366', '69', 1)
        if '666' in s:
            s = s.replace('666', '3', 1)
    sm = sum(int(x) for x in s)
    m = max(sm, m)
print(m)  # 57"""

# 13
"""from ipaddress import *
mask = ip_network('140.116.194.0/255.255.240.0', 0)
c = 0
for ip in mask:
    b = f'{ip:b}'
    if b[7] == b[7+8] == b[7+8+8] == b[7+8+8+8] == '0':
        c += 1
print(c)  # 1024"""

# 14
"""x = 9 * 123 ** 2053 + 5 * 23 ** 3146 + 91 * 47 ** 5533 + 4099
s = ''
b15 = []
while x > 0:
    if x % 23 > 15:
        b15.append(x % 23)
    x //= 23
print(len(b15))  # 2086"""

# 16
"""from functools import lru_cache
@lru_cache(None)

def f(n):
    if n < 100:
        return n
    if n >= 100:
        return n + f(n - 2)

for n in range(66_667):
    f(n)
print(f(66666)//f(777))  # 7461"""

# 17
"""В файле содержится последовательность натуральных чисел.
Её элементы могут принимать целые значения от 1 до 100 000 включительно. Определите количество пар
последовательности, в которых оба элемента положительные или оба элемента отрицательные, а модуль разности этих
элементов не больше количества чётных чисел последовательности. В ответе запишите количество найденных пар, затем
минимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента
последовательности."""

"""s = [int(x) for x in open('files/17_горбачев4.txt')]

c_ch = sum(1 for x in s if x % 2 == 0)

ans = []
for i in range(len(s) - 1):
    if (s[i] < 0 and s[i+1] < 0) or (s[i] > 0 and s[i+1] > 0):
        if abs(s[i] - s[i + 1]) <= c_ch:
            ans.append(s[i] + s[i+1])
print(len(ans), min(ans))  # 1093 1639"""

# 19
"""
def game(s1, s2, h):
    if s1 + s2 <= 63 and h == 3:
        return True
    if s1 + s2 <= 63 and h != 3:
        return False
    if s1 + s2 > 63 and h == 3:
        return False

    if h % 2 == 0:  # Петя
        return game(s1 - 1, s2, h + 1) or game(s1, s2 - 1, h + 1) or game(s1 // 3, s2, h + 1) or game(s1, s2 // 3, h + 1)
    else:  # Ваня
        return game(s1 - 1, s2, h + 1) and game(s1, s2 - 1, h + 1) and game(s1 // 3, s2, h + 1) and game(s1, s2 // 3, h + 1)


for s in range(7, 100):
    if game(57, s, 1):
        print(s)  # 45"""

# 20

"""def game(s1, s2, h):
    if s1 + s2 <= 63 and h == 4:
        return True
    if s1 + s2 <= 63 and h != 4:
        return False
    if s1 + s2 > 63 and h == 4:
        return False

    if h % 2 == 0:  # Петя
        return game(s1 - 1, s2, h + 1) and game(s1, s2 - 1, h + 1) and game(s1 // 3, s2, h + 1) and game(s1, s2 // 3,
                                                                                                         h + 1)
    else:  # Ваня
        return game(s1 - 1, s2, h + 1) or game(s1, s2 - 1, h + 1) or game(s1 // 3, s2, h + 1) or game(s1, s2 // 3,
                                                                                                      h + 1)


for s in range(7, 1000):
    if game(57, s, 1):
        print(s)  # 46 135"""


# 21

"""def game(s1, s2, h):
    if s1 + s2 <= 63 and (h == 3 or h == 5):
        return True
    if s1 + s2 <= 63 and (h != 5 and h != 3):
        return False
    if s1 + s2 > 63 and h == 5:
        return False

    if h % 2 == 0:  # Петя
        return game(s1 - 1, s2, h + 1) or game(s1, s2 - 1, h + 1) or game(s1 // 3, s2, h + 1) or game(s1, s2 // 3,
                                                                                                      h + 1)
    else:  # Ваня
        return game(s1 - 1, s2, h + 1) and game(s1, s2 - 1, h + 1) and game(s1 // 3, s2, h + 1) and game(s1, s2 // 3,
                                                                                                         h + 1)


for s in range(7, 10000):
    if game(57, s, 1):
        print(s)  # 138"""

# 23

"""def f(x, end):
    if x in end:
        return 1
    if x > max(end) or x == 23:
        return 0
    if x < min(end):
        return f(x + 3, end) + f(x + 4, end) + f(x * 2, end)


print(f(11, [50, 51, 52, 53, 54]))  # 3254"""

# 24
"""Текстовый файл состоит из десятичных цифр, знаков «+» и «*» (сложения и умножения). 
Определите максимальное количество символов в непрерывной
последовательности, которая является корректным арифметическим выражением 
с целыми неотрицательными числами.
В этом выражении никакие два знака арифметических операций не стоят рядом, 
в записи чисел отсутствуют незначащие (ведущие) нули и число 0 не имеет знака."""

"""from re import *
s = open('files/24_горбачев4.txt').readline()

sp = findall('(?:0|[1-9]\d*)(?:[*+](?:0|[1-9]\d*))+', s)
ans = max((x for x in sp), key=len)
print(ans, len(ans))  # 189"""

"""s = open('files/24_горбачев4.txt').readline().replace('+', '*')
for n in '23456789': s = s.replace(n, ' ')
while '**' in s: s = s.replace('**', ' ')

m = ''
for c in s.split():
    if len(c) > len(m):
        for i in range(len(c)):
            if c[i] not in '*':
                sub = ''
                for j in range(i, len(c)):
                    if c[j] + c[j + 1] not in ('01', '00'):
                        sub += c[j]
                        m = max(m, sub, key=len)
                    else:
                        break
print(m, len(m))  # 189
"""

# 25

"""from fnmatch import fnmatch
c = 0
for i in range(111, 10**8, 111):
    if fnmatch(str(i), '3*4?5*6?') and i % 2 == 0:
        c += 1
print(c)  # 142"""

# 27
"""clastersA = [[], [], []]
for s in open('files/27A__горбачев4.txt'):
    x, y = [float(x) for x in s.split()]
    if x < 0 and y > 0:
        clastersA[0].append([x, y])
    elif x < 0 and y < 0:
        clastersA[1].append([x, y])
    else:
        clastersA[2].append([x, y])
print([len(kl) for kl in clastersA])  # [33, 33, 33]

clastersB = [[], [], [], []]
for s in open('files/27B_горбачев4.txt'):
    x, y = [float(x) for x in s.split()]
    if x < 0 and y > 0:
        clastersB[0].append([x, y])
    elif x < 0 and y < 0:
        clastersB[1].append([x, y])
    elif x > 0 and y > 0:
        clastersB[2].append([x, y])
    else:
        clastersB[3].append([x, y])
print([len(kl) for kl in clastersB])  # [2700, 2300, 2000, 2999]


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(kl) for kl in clastersA]
centerB = [center(kl) for kl in clastersB]
print(centerA, centerB)


pxA = sum(x for x, y in centerA) / len(clastersA) * 100_000
pyA = sum(y for x, y in centerA) / len(clastersA) * 100_000
print(int(abs(pxA)), int(abs(pyA)))  # 188628 100151

pxB = sum(x for x, y in centerB) / len(clastersB) * 100_000
pyB = sum(y for x, y in centerB) / len(clastersB) * 100_000
print(int(abs(pxB)), int(abs(pyB)))  # 162079 80428"""

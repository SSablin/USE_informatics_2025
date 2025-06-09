# Задача 2 #88112
from itertools import product
print('x y z w')
for i in product(range(2), repeat=4):
    x, y, z, w = i
    f = (x <= w) and ((not z) or y) and (y <= x)
    if f:
        print(x, y, z, w)
        # x w z y

# Задача 5 #72428
def i3(i):
    s = ''
    while i > 0:
        s += str(i % 3)
        i //= 3
    return s[::-1]

r_mn = float('inf')
for i in range(1, 1000):
    n = i3(i)
    if (n.count('1') + n.count('2')) % 2 == 0:
        n += '0'
    else:
        n += '1'
    if (n.count('1') + n.count('2')) % 2 == 0:
        n += '0'
    else:
        n += '1'
    r = int(n, 3)
    if r > 337:
        r_mn = min(r_mn, r)
print(r_mn)  # 345

# Задача 6 #88124
# считаем только в отрицательных координатах
# Сколько точек с неположтельными координатами
# черепаха направлена по направлению оси ординат
from turtle import *
screensize(5000, 5000)
tracer(0)
lt(90)
c = 30

rt(60)
for i in range(20):
    bk(5 * c)
    rt(240)
    fd(11 * c)
    lt(60)
up()
for x in range(-10, 1):
    for y in range(-10, 1):
        goto(x*c, y*c)
        dot(4, 'green')
done()  # 13

# Задача 7 #63915
t = (81 * 1024**2 * 8) / (4 * 36000 * 24)  # 196 секунд
print(t // 60)  # 3

# Задача 8 #62658
from itertools import product
c = 0
for i in product(sorted('КОФЕ'), repeat=5):
    s = ''.join(i)
    c += 1
    if s == 'ФЕФКО':
        print(c)  # 823

# Задача 9 #86050
f = open('файлы пробник №3/9.txt')
c = 0
for s in f:
    a = list(map(int, s.split()))
    if (((all(a[i] % 2 == 0 for i in range(0, 7, 2)) and all(a[i] % 2 != 0 for i in range(1, 6, 2))) or
        (all(a[i] % 2 != 0 for i in range(0, 7, 2)) and all(a[i] % 2 == 0 for i in range(1, 6, 2)))) and
        (sum(x for x in a if x % 2 == 0) > sum(x for x in a if x % 2 != 0))):
        c += 1
        print(a, c)
print(c)  # 137

# Задача 11 #113820
S = 12 * 1024 // 1536
i = 8 * 8 // 16
print(i)  # 4

# Задача 12 #85898
for n in range(11, 1050):
    s = '6' + '0' * n
    while '666' in s or '000' in s:
        if '666' in s:
            s = s.replace('666', '00', 1)
        else:
            s = s.replace('000', '6', 1)
    if s.count('0') == 0 and len(s) > 1:
        print(n)  # 1046

# Задача 13 #105566
from ipaddress import *
ip = ip_address('44.249.80.224')
net = ip_network(f'{ip}/255.255.255.252', 0)
c = 0
for ip in net.hosts():
    b = f'{ip:b}'
    if b.count('1') > 14:
        print(b, ip)
        c += 1
# узлы
# -широковещательный
print(c)  # 2

# Задача 14 #85899
from string import digits, ascii_uppercase
for x in (digits+ascii_uppercase)[:17]:
    a = int(f'370{x}102', 17) + int(f'8{x}3719', 17)
    if a % 11 == 0:
        print(a // 11)  # 8633247

# Задача 15 #57877
def DEL(n, m):
    if n % m == 0:
        return True
    return False


mn = float('inf')
for a in range(1, 60):
    for b in range(a, 60):
        f = True
        for x in range(1, 60):
            A = a <= x <= b
            B = 36 <= x <= 51
            D = DEL(x, 5)
            if not (A or (B <= (not D))):
                f = False
                break
        if f and (b - a) < mn:
            mn = (b - a)
            print(mn, a, b)  # 10

# Задача 16 #72484
f = {}
for n in range(2025):
    if n == 0:
        f[n] = 0
    if n > 0 and n % 2 == 0:
        f[n] = f[n/2] + 2
    elif n % 2 != 0:
        f[n] = 3 + f[n-1]
print(f)
for n in range(2025):
    if f[n] == 21:
        print(n)  # 67
        break

# Задача 17 #72534
s = [int(x) for x in open('файлы пробник №3/17.txt')]
ans = []
for i in range(len(s)-1):
    for j in range(i+1,  len(s)):
        if (s[i] * s[j] % 2 == 0) and ((s[i] % 13 == 0) or s[j] % 13 == 0):
            ans.append(s[i] + s[j])
print(len(ans), max(ans))  # 5495352 19971

# БУ:
# Задача 19 #29366
def f(a):
    if a >= 45:
        return 0
    if a * 3 > 112:
        n = [f(a + 2)]
    else:
        n = [f(a + 2), f(a * 3)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)


for s in range(1, 46):
    if f(s * 3) == 1 or f(s + 2) == 1:
        print(s)  # 42
# Задача 20 #29367
def f(a):
    if a >= 45:
        return 0
    if a * 3 > 112:
        n = [f(a + 2)]
    else:
        n = [f(a + 2), f(a * 3)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)


for s in range(1, 46):
    if f(s) == 2:
        print(s)  # 3
# Задача 21 #29368
def f(a):
    if a >= 45:
        return 0
    if a * 3 > 112:
        n = [f(a + 2)]
    else:
        n = [f(a + 2), f(a * 3)]
    t = [i for i in n if i <= 0]
    if t:
        return -max(t) + 1
    else:
        return -max(n)


for s in range(1, 46):
    if f(s) == 3:
        print(s)  # 4

# Задача 19 #29366
# 44
# Задача 20 #29367
def g(s, h):
    if 45 <= s <= 112 and h == 3:
        return True
    if ((s > 112 and (h == 1 or h == 3)) or
            (s < 45 and h == 3)):
        return False
    if 45 <= s <= 112 and h != 3:
        return False
    if s > 112 and h == 2:
        return True

    if h % 2 != 0:
        return g(s + 2, h + 1) and g(s * 3, h + 1)
    else:
        return g(s + 2, h + 1) or g(s * 3, h + 1)


for s in range(1, 45):
    if g(s, 0):
        print(s)  # 3

# Задача 21 #29368
def g(s, h):
    if 45 <= s <= 112 and (h == 1 or h == 3 or h == 5):
        return True
    if ((s > 112 and (h == 1 or h == 3 or h == 5)) or
            (s < 45 and h == 5)):
        return False
    if 45 <= s <= 112 and h != 1 and h != 3 and h != 5:
        return False
    if s > 112 and (h == 2 or h == 4):
        return True
    if h % 2 != 0:
        return g(s + 2, h + 1) and g(s * 3, h + 1)
    else:
        return g(s + 2, h + 1) or g(s * 3, h + 1)


for s in range(1, 45):
    if g(s, 0):
        print(s)  # 4

# Задача 23 #84016
def f(x, end, c):
    if x == end:
        return True
    if x > end:
        return False
    if x < end:
        if c:
            return f(x * 3, end, False)
        else:
            return f(x + 1, end, False) + f(x * 2, end, True) + f(x * 3, end, False)

print(f(8, 123, False))  # 111

# Задача 24 # 113807
from re import finditer
s = open('файлы пробник №3/24.txt').readline()
num_h = r'[1-9]*\d*[02468]'
num_n = r'[1-9]*\d*[13579]'
reg = rf'{num_h},{num_n}'
m = max((x.group() for x in finditer(reg, s)), key=len)
print(len(m), m)  # 46

# БУ:
# Задача 25 #88288
from fnmatch import fnmatch
for i in range(2004, 10**10, 2004):
    s = str(i)
    if fnmatch(s, '*123*321?'):
        t = s.find('123')
        nc = [j in '13579' for j in s[:t]]
        if all(nc):
            print(i, i // 2004)
# 123853212 61803
# 1230063216 613804
# 1231063212 614303
# 1235073216 616304
# 1236073212 616803
# Задача 25 #88288
from re import fullmatch
for i in range(2004, 10**10, 2004):
    if fullmatch('[02468]*123\d*321\d', str(i)):
        print(i, i // 2004)
# 123853212 61803
# 1230063216 613804
# 1231063212 614303
# 1235073216 616304
# 1236073212 616803

# Задача 26 #119551
"""Входной файл содержит сведения о заявках на бронирование помещения для проведения консультаций. Каждая
заявка содержит время начала и окончания консультации (в минутах от начала суток), а также сумму, которую
готовы заплатить за проведение консультации. Два мероприятия можно провести, если время окончания одного
меньше или равно времени начала другого.
Определите максимальную сумму оплаты, которую можно получить за день, а также общую длительность всех
выбранных консультаций.
Входные данные:
В первой строке входного файла — натуральное число N (1 <= N <= 1000) —количество заявок. В каждой из
следующих строк записаны три числа: время начала и окончания консультации (в минутах от начала суток, от
1 до 1440) и сумма оплаты.
Выходные данные:
Два числа через пробел: максимальную сумму оплаты за день и суммарную длительность всех выбранных
консультаций."""

f = open('файлы пробник №3/26.txt')
n = int(f.readline())

# f = ['10 60 5', '60 100 6', '110 150 7', '160 200 8', '100 180 15']
# n = 5

a = [list(map(int, s.split())) for s in f]
a.sort(key=lambda x: x[1])  # по времени окончания
# набор мероприятий, которые можно провести перед x
print(a[:10])
p = [i[2] for i in a]  # стоимость мероприятия + всех перед ним
tm = [i[1] - i[0] + 1 for i in a]
print(p)
print(tm)
for i in range(1, n):
    for j in range(i):
        if a[j][1] <= a[i][0]:
            if p[j] + a[i][2] > p[i]:
                p[i] = p[j] + a[i][2]
                tm[i] = tm[j] + a[i][1] - a[i][0] + 1
mx = max(p)
print(mx)  # 629
for i in range(n):
    if p[i] == mx:
        print(tm[i])  # 983


# Задача 27 #106031
# shkolkovo:
from math import *


def dbscan(a, r):
    cl = []  # Инициализируем список для хранения кластеров
    while a:  # Пока есть элементы в входном массиве ’a’
        # Создаем новый кластер и добавляем в него первый элемент из ’a’
        cl.append([a.pop(0)])
        for i in cl[-1]:  # Проходим по элементам последнего кластера
            # Проверяем каждый элемент ’j’ в оставшихся элементах ’a’
            for j in a[:]:
                # Если расстояние между ’i’ и ’j’ меньше радиуса ’r’
                if dist(i, j) < r:
                    cl[-1].append(j)  # Добавляем ’j’ в текущий кластер
                    a.remove(j)  # Удаляем ’j’ из списка ’a’, чтобы не проверять еще раз
    return cl


f = open("файлы пробник №3/27A.txt")
s = f.readline()
a = [list(map(float, i.replace(",", ".").split())) for i in f]
cl = dbscan(a, 0.65)
cl_total = []
for i in cl:
    if len(i) > 10: cl_total.append(i)

t = 0.01
ans = []
for i in cl_total:  # Проходим по каждому элементу в списке cl_total
    found_star = dbscan(i, t)  # Применяем алгоритм DBSCAN
    tr_stars = []  # Список для тройных звездных систем
    mx_starsys = []  # Список для хранения звездной системы с максимальным расстоянием
    # Проходим по каждому кластеру, найденному алгоритмом DBSCAN
    for j in found_star:
        if len(j) == 3:  # Проверяем, состоит ли кластер из трех звезд
            d1 = dist(j[0], j[1])
            d2 = dist(j[0], j[2])
            d3 = dist(j[1], j[2])
            if ((d1 ** 2 < d2**2 + d3**2) and (d2**2 < d1**2 + d3**2) and (d3**2 < d1**2 + d2**2) and
                    (max(d1, d2, d3) <= t)):
                tr_stars.append(j)
    mx_per = 0  # Переменная для хранения максимального длины стороны
    for j in tr_stars:  # Проходим по всем найденным тройным системам
        # Вычисляем периметр
        d1 = dist(j[0], j[1])
        d2 = dist(j[0], j[2])
        d3 = dist(j[1], j[2])
        if d1 + d2 + d3 > mx_per:
            mx_per = d1 + d2 + d3  # Обновляем максимальное расстояние
            mx_starsys = j  # Сохраняем текущую звездную систему как систему с максимальным расстоянием
    ans.append(mx_starsys)
print(ans)

# Рассчитываем среднее значение
res_X = 0
res_Y = 0
for i in ans:
    res_X += (i[0][0] + i[1][0] + i[2][0])
    res_Y += (i[0][1] + i[1][1] + i[2][1])

print(int(res_X / (len(ans) * 3) * 10000))
print(int(res_Y / (len(ans) * 3) * 10000))
# A:
# 1126
# 7830
# B:
# 28802
# 36021

# БУ:
from math import *


def dbscan(a, r):
    cl = []  # Инициализируем список для хранения кластеров
    while a:  # Пока есть элементы в входном массиве ’a’
        # Создаем новый кластер и добавляем в него первый элемент из ’a’
        cl.append([a.pop(0)])
        for i in cl[-1]:  # Проходим по элементам последнего кластера
            # Проверяем каждый элемент ’j’ в оставшихся элементах ’a’
            for j in a[:]:
                # Если расстояние между ’i’ и ’j’ меньше радиуса ’r’
                if dist(i, j) < r:
                    cl[-1].append(j)  # Добавляем ’j’ в текущий кластер
                    a.remove(j)  # Удаляем ’j’ из списка ’a’, чтобы не проверять еще раз
    return cl


f = open("файлы пробник №3/27.txt")
s = f.readline()
a = [list(map(float, i.replace(",", ".").split())) for i in f]
cl = dbscan(a, 0.65)
cl_total = [i for i in cl if len(i) > 10]
px = py = 0
t = 0.01
for i in cl_total:
    stars = dbscan(i, t)
    max_p = 0
    tr_sys = []
    for j in stars:
        if len(j) == 3:
            x = dist(j[0], j[1])
            y = dist(j[0], j[2])
            z = dist(j[1], j[2])
            mx = max(x, y, z)
            mn = min(x, y, z)
            md = x + y + z - mn - mx
            if mx <= t and mx ** 2 < mn ** 2 + md ** 2:
                if x + y + z > max_p:
                    max_p = x + y + z
                    tr_sys = j
    print(tr_sys)
    px += tr_sys[0][0] + tr_sys[1][0] + tr_sys[2][0]
    py += tr_sys[0][1] + tr_sys[1][1] + tr_sys[2][1]

print(int(px / (len(cl_total) * 3) * 10000), int(py / (len(cl_total) * 3) * 10000))

# 8
"""from itertools import product
c = -1
f = False
for i in product('АЕИКМСЧ', repeat=5):
    s = ''.join(i)
    if s == 'МАСИК':
        f = True
    if s == 'ЧЕЧИК':
        break
    if f:
        c += 1
        print(c, s)  # 5193"""

# 9
"""c = 0
for s in open('files/9_шастин10.txt'):
    a = list(map(int, s.split()))
    if ((all(x % 5 != 0 for x in a) and not all(len(str(x)) == 2 for x in a)) or
            (not all(x % 5 != 0 for x in a) and all(len(str(x)) == 2 for x in a))):
            c += 1
            print(c, a)  # 305"""

# 12
"""s = '4' * 222
c = 0
while '4444' in s or '222' in s:
    if '4444' in s:
        s = s.replace('4444', '2', 1)
        c += 1
    else:
        s = s.replace('222', '44', 1)
        c += 1
print(c)  # 86"""

# 13
"""Для узла с IР-адресом 221.142.14.0 адрес подсети равен 221.142.0.0. Сколько
существует различных возможных значений маски сети, если известно, что в этой сети
не менее 8000 узлов? Ответ запишите в виде десятичного числа."""
"""from ipaddress import *
ip = ip_address('221.142.14.0')
c = 0
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if net.num_addresses >= 8000 and str(net.network_address) == '221.142.0.0':
        c += 1
print(c)  # 5"""

# 14
"""def i3(x):
    s = ''
    while x > 0:
        s += str(x % 3)
        x //= 3
    return s[::-1]


for a in range(1, 100000):
    x = 3 ** 10 + 3 ** 7 + 3 ** 3 + 2 - a
    x3 = i3(x)
    if (sum(1 for x in list(map(int, x3)) if x == 0) == 
            sum(1 for x in list(map(int, x3)) if x == 1) == 
            sum(1 for x in list(map(int, x3)) if x == 2)):
        print(a)  # 41960
        break"""

# 15
"""for a in range(1, 300):
    f = True
    for x in range(1, 300):
        if not (((x & a) == 0) <= (((x & 77) == 0) and ((x & 44) == 0))):
            f = False
            break
    if f:
        print(a)  # 109
        break"""

# 16
"""from sys import setrecursionlimit
setrecursionlimit(60_000)
def f(n):
    if n < 222:
        return 111
    else:
        return 2 * (n + 4) + f(n - 3)


print(f(55555) - f(55543))  # 444436

sp = [0, ]
for i in range(1, 60_000):
    if i < 222:
        sp.append(111)
    else:
        sp.append(2 * (i + 4) + sp[i - 3])
print(sp[55555] - sp[55543])  # 444436"""

# 17
"""s = [int(x) for x in open('files/17_шастин10.txt')]
mn_123 = min(x for x in s if abs(x) % 1000 == 123 and x == abs(x))

ans = []
for i in range(len(s) - 1):
    if (max(s[i:i + 2]) - min(s[i:i + 2])) <= mn_123:
        ans.append(max(s[i:i + 2]) - min(s[i:i + 2]))
print(len(ans), max(ans))  # 1293 13117"""

# 23
"""diap = [x for x in range(5, 38) if x % 11 == 0]
print(diap)


def f(x, end):
    if x == end:
        return True
    if x > end:
        return False
    if x < end:
        return f(x + 2, end) + f(x + 3, end) + f(x + 5, end)


print(f(5, 11) * f(11, 22) * f(22, 33) * f(33, 37))  # 512"""
# 24
"""Текстовый файл состоит не более, чем из 7 200 000 прописных символов латинского алфавита. 
Назовем «перетройкой» такие две одинаковые непрерывные строковые подпоследовательности
длины З, которые пересекаются в одной букве (т.е. начало одной тройки совпадает с концом другой). 
Определите в прилагаемом файле минимальное количество идущих подряд символов, среди которых
встречается не менее 170 «перетроек».
Например, в строке ABCBCBCBDDDHAHAHEF есть 4 «перетройки»: ВСВСВСВ - в этой подстроке З «перетройки», 
НАНАН - в этой подстроке 1 «перетройка».
для выполнения этого задания следует написать программу."""

# Два указателя
"""s = open('files/24_шастин10.txt').readline().rstrip()
m = float('inf')
c = 0
l = 0
for r in range(4, len(s)):
    if s[r - 4: r - 1] == s[r - 2: r + 1]:
        c += 1
    while c >= 170:
        m = min(m, r - l + 1)
        if s[l: l + 3] == s[l + 2: l + 5]:
            c -= 1
        l += 1
print(m)  # 2545440"""
# Сохранение индекса
"""s = open('files/24_шастин10.txt').readline().rstrip()
pos = []
m = float('inf')
for i in range(4, len(s)):
    if s[i - 4: i - 1] == s[i - 2: i + 1]:
        pos.append(i - 4)
    if len(pos) >= 170:
        m = min(m, i - pos[-170] + 1)
print(m)  # 2545440"""

# 25
"""from fnmatch import fnmatch

for i in range(4321, 10**9, 4321):
    if fnmatch(str(i), '34*56?7'):
        if str(eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))[-1] == '0':
            print(i, eval((''.join(f'{x}*' for x in map(int, str(i))))[:-1]))"""

# 26
"""(Д. Бахтиев) На складе есть К стеллажей для хранения грузов. Все стеллажи пронумерованы, начиная с
единицы. Каждый стеллаж представляет собой двумерную сетку размером М х N, где М — количество
рядов, а N — количество полок в каждом ряду. Каждая ячейка стеллажа может хранить только один груз.
Известно время, в которое каждый груз поступит на склад, и время, до которого его нужно хранить. При
поступлении груза его необходимо разместить в свободную ячейку стеллажа с наименьшим номером,
начиная с первого ряда и первой полки. Если в текущем стеллаже свободных ячеек нет, груз размещается
в следующем стеллаже с наименьшим номером. для размещения или извлечения груза из ячейки
требуется 1 минута. Со следующей минуты ячейка становится доступной для нового груза.
Если груз поступил, но свободных ячеек на всех стеллажах нет
— он не может быть размещён и
отправляется на другой склад.
Если одновременно на склад поступило несколько грузов, то они обслуживаются в порядке возрастания
времени завершения хранения.
Определите, сколько всего грузов будет размещено на складе за 24 часа, и номер ряда первого стеллажа,
на котором побывало наименьшее количество грузов. Если таких рядов несколько, укажите номер
наименьшего из них."""
"""f = open('files/26_шастин10.txt')
k, m, n = map(int, f.readline().split())
g = int(f.readline())
data = sorted([list(map(int, f.readline().split())) for _ in range(g)])
storage = [[[-1] * n for _ in range(m)] for _ in range(k)]
statist = [[0] * m for _ in range(k)]
for st, en in data:
    status = 1
    for shelf in range(k):
        for row in range(m):
            for place in range(n):
                if status and storage[shelf][row][place] < st:
                    storage[shelf][row][place] = en
                    statist[shelf][row] += 1
                    status = 0

print(sum([sum(row) for row in statist]), statist[0].index(min(statist[0])) + 1)  # 8380 18"""

# 27
"""(Л. Шастин) Ведущие агрономы компании «Царство кленового сиропа» изучают качество земли в большом
кленовом саду. Перед ними стоит задача — проанализировать различные участки сада и сделать выводы о
наиболее плодородных местах для дальнейшей посадки новых деревьев, что позволит возрастить объемы
производства кленового сиропа. По итогам сбора информации имеется отчёт — набор данных, включающий
записи о позициях в саду, отмеченных агрономами. Каждая позиция характеризуется двумя вещественными
координатами, отражающими ее положение в декартовой системе координат. Специалисты включили в
отчет позиции двух видов: плодородные и неплодородные. Чтобы минимизировать количество
неприжившихся саженцев кленовых деревьев, решено, что нельзя сажать новые деревья в областях,
близлежащих к неплодородным позициям. Такие запретные области определяются как окружности с
радиусом R1 5, центрами которых являются неплодородные позиции. В конце концов необходимо
выделить области, подходящие для посадки, которые характеризуются как окружности с радиусом R2 7
с центрами, которые определяются ранее выделенными плодородными позициями. Среди таких областей
нужно найти оптимальную: такую, внутри которой находится наибольшее количество плодородных позиций
(разумеется, находящихся вне запретных областей). А если оптимальных областей несколько, выбрать
область с наибольшей суммой координат."""
"""from math import dist

f = open('files/27A_шастин10.txt')
n, k = [int(x) for x in f.readline().split()]
pl = [[float(x) for x in f.readline().split()] for _ in range(n)]
npl = [[float(x) for x in f.readline().split()] for _ in range(k)]
for zp in npl:
    for i in range(n):
        if pl[i] != -1 and dist(zp, pl[i]) <= 5:
            pl[i] = -1
pl = [p for p in pl if p != -1]
res = []
for p1 in pl:
    cnt = 0
    for p2 in pl:
        if dist(p1, p2) <= 7:
            cnt += 1
    res.append([cnt, sum(p1), p1])
x, y = sorted(res)[-1][-1]
print(x * 10**9, y * 10 ** 9)"""

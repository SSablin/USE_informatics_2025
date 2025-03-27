# 18967
"""f = open('files/26_18967.txt')
n, k = [int(x) for x in f.readline().split()]
# n - общее кол-во мест, к - кол-во людей, которых нужно посмотреть
data = [[int(x) for x in s.split()] for s in f]
# ID, time, M - кол-во номерков
data.sort(key=lambda x: (x[1], x[0]))
# сортируем по времени подхода, если в одно время(совпадение), то по ID
visited = set()  # уже посетили
left = set()  # приходили, но покинули кинотеатр
top_top = time = 0
for i in range(len(data)):  # перебираем клиентов
    if data[i][0] not in visited:
        if n - data[i][2] >= 0:  # если есть место
            n -= data[i][2]
        else:
            top_top += data[i][2]
            left.add(data[i][0])
    else:
        if data[i][0] not in left:
            n += data[i][2]
    visited.add(data[i][0])  # отмечаем, что клиент обслужен
    if n == 0:  # не осталось свободного места в гардеробе
        time += data[i + 1][1] - data[i][1]
print(top_top, time)  # 5190 294"""

# 26
# https://youtu.be/GYogg6TOxts?si=7eP6AqZvgah2ATYu&t=4059
"""f = open('files/26_18492.txt')
n = int(f.readline())
data = [list(map(int, x.split())) for x in f]
timeline = [0] * 1441
for num, st, en in data:
    for mnt in range(st, en):
        timeline[mnt] += 1
pick = max(timeline)
intervals = []
end = 1
while end < 1441:
    if timeline[end] == pick and timeline[end - 1] < pick:
        start = end
        while timeline[end] == pick:
            end += 1
        intervals.append((end - start, sum(nm for nm, st, en in data if start <= st < end or st <= start < en)))
    end += 1
print(len(intervals), max(intervals)[1])  # 11 27785627"""

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

# 19890
"""f = open('files/26.3_19890.txt')
n, m = map(int, f.readline().split())
sp = []

for i in f:
    sp.append(int(i))

sp.sort()

for i in range(310, 321):
    if i in sp:
        ny = sp.index(i)
        break

cy = 0
my = 0
cp = 0

for i in range(ny, len(sp)):
    if my + sp[i] <= m and sp[i] <= 320:
        my += sp[i]
        cy += 1
        cp = sp[i]
    if m - my <= 0 or sp[ny] > 320:
        break

for i in range(ny):
    if my + sp[i] <= m:
        my += sp[i]
        cy += 1
        cp = sp[i]
    else:
        break

if (m - my + cp) in sp:
    my += m - my

print(cy, my)"""

# 26 №19599
"""from math import ceil
f = open('files/26_19599.txt')
n = int(f.readline())
data = []
for s in f:
    data.append(list(map(int, list(s.split()))))
for x in data:
    x[0] = x[0] - 1
    for j in range(2, 6):
        x[j] = x[j] - 1
data.sort()

# n power support opponets(3)
for i in range(n):
    if data[i][1] != 0:
        if data[data[i][2]][1] != 0:
            data[data[i][2]][1] += data[i][1]
        for j in range(3, 6):
            if data[data[i][j]][1] != 0:
                if data[i][1] > data[data[i][j]][1]:
                    data[data[i][j]][1] = 0
                    data[i][1] = ceil(data[i][1] - data[i][1] * 1/3)
                if data[i][1] == data[data[i][j]][1]:
                    data[i][1] = data[data[i][j]][1] = 0
                    break
                if data[i][1] < data[data[i][j]][1]:
                    data[i][1] = 0
                    data[data[i][j]][1] = ceil(data[data[i][j]][1] - data[data[i][j]][1] * 1/3)
                    break
            else:
                pass
c_killed = sum(1 for x in data if x[1] == 0)
max_p = max(x[1] for x in data if x[1] != 0)
print(c_killed, max_p)  # 4228 5962"""

# 26_горбачев5
"""
f = open('files/26_горбачев5.txt')
N, M, K = map(int, f.readline().split())
mx = 0
s = [M + 1] * (K + 1)

for i in f:
    r, m = map(int, i.split())
    s[m] = min(s[m], r)

for i in range(1, K - 3):
    x = min(s[i], s[i + 1], s[i + 2], s[i + 3])
    mx = max(mx, x)

print(mx - 1)

for i in range(1, K - 3):
    if min(s[i], s[i + 1], s[i + 2], s[i + 3]) == mx:
        print(i, i+1, i+2, i+3)"""
# 9717 5198

# 26 шастин10
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

"""
№ 20910 Апробация 05.03.25 (Уровень: Средний)
При онлайн-покупке билета на концерт известно, какие места в зале уже заняты.
Необходимо купить два билета на такие соседние места в одном ряду,
чтобы перед ними все кресла с такими же номерами были свободны, а ряд находился как можно дальше от сцены.
Если в этом ряду таких пар мест несколько, найдите пару с наименьшими номерами.
В ответе запишите два целых числа: искомый номер ряда и наименьший номер места в найденной паре.
Нумерация рядов и мест ведётся с 1. Гарантируется, что хотя бы одна такая пара в зале есть.
Входные данные
В первой строке входного файла находятся три числа: N – количество занятых мест в зале (целое положительное число,
не превышающее 10 000), M – количество рядов (целое положительное число, не превышающее 100 000) и
K – количество мест в каждом ряду (целое положительное число, не превышающее 100 000).
В следующих N строках находятся пары натуральных чисел: номер ряда и номер места занятого кресла соответственно
(первое число не превышает значения M, а второе – K).
Выходные данные
Два целых положительных числа: наибольший номер ряда и наименьший номер места в найденной паре кресел.
Типовой пример организации данных во входном файле
n m k
7 7 8
1 1
6 6
5 5
6 7
4 4
2 2
3 3
При таких исходных данных ответом является пара чисел 5 и 6. Условию задачи удовлетворяют места 6 и 7 в ряду 5:
перед креслами 6 и 7 нет занятых мест и это первая из двух возможных пар в этом ряду.
В рядах 6 и 7 искомую пару найти нельзя."""

# SS
# Очень Долго
"""f = open('files/26_20910.txt')
n, m, k = map(int, f.readline().split())
data = sorted([list(map(int, x.split())) for x in f])
for i in range(len(data)):
    data[i][0] -= 1
    data[i][1] -= 1
hall = [[0 for _ in range(k)] for _ in range(m)]
for riad, place in data:
    hall[riad][place] = 1
places = [0 for _ in range(k)]
ans = [[0, 0], [0, 0]]
for i in range(m):
    for j in range(k-1):
        if places[j] + places[j+1] == 0 and hall[i][j] + hall[i][j+1] == 0:
            ans[0] = [i+1, j+1]
            ans[1] = [i+1, j+2]
            break
    for j in range(k):
        if hall[i][j] == 1:
            places[j] += 1
print(ans)"""

# Кабанов
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

# №9756

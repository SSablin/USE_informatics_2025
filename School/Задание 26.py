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


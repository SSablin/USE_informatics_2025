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
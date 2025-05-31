# https://youtu.be/qxz7-O-2ujw?si=rjoTH3LsqD2hXx53&t=5630
f = open('files/26/26var05.txt')
n = int(f.readline())

# f = ('20 120', '90 20', '147 43', '150 30', '120 20')
# n = 5
data = []
for s in f:
    st, t = map(int, s.split())
    data.append([st, st + t])
data.sort(key=lambda x: x[1])
print(data)

k = 1  # max кол-во мероприятий (1 - уже взяли 1е мероприятие)
m = 0  # max перерыв между двумя последними мероприятиями
a, b = data[0][0], data[0][1]  # [время начала, время окончания] последнего мероприятия
for i in data[1:]:
    if i[0] > b:
        k += 1
        c = b
        a, b = i[0], i[1]
for i in data[1:]:
    if i[1] >= b:
        m = max(m, i[0] - c)
print(k, m)  # 26 20


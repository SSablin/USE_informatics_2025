"""with open('files/26.txt') as f:
    a = f.readlines()
s, d = map(int, a[0].split())
del a[0]
a = sorted(list(map(int, a)))  # сортировать, список, преобразовать в int

# enumerate() - обрабатывает и значение элемента, и его индекс
v = 0  # объем
for i, z in enumerate(a):
    if v + z > s:
        break
    v += z
print(i)  # 568

d = s - v  # 24 - остаток
b = [x for x in a if x - a[i-1] <= d]
print(max(b))  # 50"""

# №27883
"""Системный администратор раз в неделю создаёт архив пользовательских файлов. Однако объём
диска, куда он помещает архив, может быть меньше, чем суммарный объём архивируемых файлов.
Известно, какой объём занимает файл каждого пользователя.
По заданной информации об объёме файлов пользователей и свободном объёме на архивном
диске определите максимальное число пользователей, чьи файлы можно сохранить в архиве, а также
максимальный размер имеющегося файла, который может быть сохранён в архиве, при условии, что
сохранены файлы максимально возможного числа пользователей."""
"""with open('files/26_27883.txt') as f:
    a = f.readlines()
s, d = map(int, a[0].split())
del a[0]
a = sorted(list(map(int, a)))

v = 0
for i, n in enumerate(a):
    if v + n > s:
        break
    v += n
print(i)  # 149
d = s - v  # 0 - остаток
print(d)
b = [x for x in a if x - a[i - 1] <= d]
print(max(b))  # 7"""

# №36000
"""В текстовом файле записан набор натуральных чисел, не превышающих 10^9. Гарантируется, что
все числа различны. Необходимо определить, сколько в наборе таких пар чисел, что числа в паре
имеют разную чётность, а их сумма тоже присутствует в файле, и чему равна наибольшая из сумм
таких пар."""
"""with open('files/26_36000.txt') as f:
    v = f.readline()
    s = f.readlines()
s = list(map(int, s))
ns = set(s)
ans = []
for i in range(len(s) - 1):
    for j in range(i+1, len(s)):
        if (s[i] % 2 == 0 and s[j] % 2 != 0) or (s[i] % 2 != 0 and s[j] % 2 == 0):
            if (s[i] + s[j]) in ns:
                ans.append(s[i] + s[j])

print(len(ans), max(ans))  # 15 954387771"""

"""f = open('files/26_36000.txt')
k = f.readlines()
n = list(map(int, k))
m = 0
s = 0
c = 0
ns = set(n)
for i in range(1, len(n) - 1):
    for j in range(i + 1, len(n)):
        if (n[i] + n[j]) % 2 == 1:
            s = n[i] + n[j]
            if s in ns:
                c += 1
                if s > m:
                    m = s

print(c, m)  # 15 954387771"""

# ДЕМО 2024
"""with open('files/26_2024.txt') as f:
    n = int(f.readline())
    a = []
    for i in range(n):
        b, c = map(int, f.readline().split())
        a.append([b, c])

a.sort(key=lambda x: x[1])

s = [[a[0][0], a[0][1]]]

for start, end in a[1:]:
    if start >= s[-1][1]:
        s.append([start, end])

print(len(s))
print(s[-1][0] - s[-2][1])  # 32 15"""

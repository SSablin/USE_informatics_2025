# 16
f = [0] * 2030
for n in range(2030):
    if n == 1:
        f[n] = 1
    else:
        f[n] = n * f[n - 1]
print(((f[2025] // 25) + f[2024]) / f[2023])  # 165968

# 24
from re import *

s = open('files/24/24var01.txt').readline()
num = r'(0|[1-4]\d*)'
reg = rf'{num}([+-]{num})*'
m = max((x.group(0) for x in finditer(reg, s)), key=len)
print(len(m), m)  # 131

# 25
for x in range(700_000, 10**10):
    s = set()
    for i in range(17, x, 10):
        if x % i == 0 and i % 10 == 7:
            print(x, i)
            break
# 700002 27
# 700003 37
# 700005 6087
# 700007 77
# 700008 29167

# 26
# нумерация y - сверху вниз c 1
# нумерация x - слева направо c 1

f = open('files/26/26var01.txt')
n, m, k = map(int, f.readline().split())

# example
n, m, k = 6, 6, 7
f = ('1 1', '5 5', '5 6', '4 4', '2 2', '3 3')

field = [m + 1] * (k + 1)
for line in f:
    x, y = map(int, line.split())
    field[y] = min(field[y], x)
res = [0, 0]
for j in range(1, k):
    mr = min(field[j], field[j + 1]) - 1
    if mr > res[0] and mr > 0:
        res = [mr, j]
    elif mr == res[0] and mr > 0:
        res[1] = min(res[1], j)
print(*res)  # 4 5

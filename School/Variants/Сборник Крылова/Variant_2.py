# 24
from re import *

s = open('files/24/24var02.txt').readline()
num = r'(0|[5-8]\d*)'
reg = rf'(\+?{num}([-+]{num})*)'
m = max((x.group(0) for x in finditer(reg, s)), key=len)
print(len(m), m)  # 167

# 25
def m(x):
    s = set()
    for i in range(2, x):
        if x % i == 0 and i != 1 and i != x:
            s.add(i)
    if len(s) == 0:
        return 0
    return min(s) + max(s)

print(m(30))

for x in range(1_000_000, 10 ** 10):
    M = m(x)
    if M % 10 == 6:
        print(x, M)
# 1000008 500006
# 1000009 3706
# 1000013 142866
# 1000028 500016
# 1000029 333346

# 26
f = open('files/26/26var02.txt')
n, m, k = map(int, f.readline().split())

# f = ('1 1', '5 5', '5 6', '4 4', '2 2', '3 3')
# n, m, k = 6, 6, 8

field = [m + 1] * (k + 1)
for line in f:
    x, y = map(int, line.split())
    field[y] = min(field[y], x)
print(field)
mx = []
for i in range(1, k-1):
    r = min(field[i], field[i + 1], field[i+2]) - 1
    if r == 1804:
        print(i, i+1, i+2)
    mx.append(r)
print(max(mx))
# 4436 1804

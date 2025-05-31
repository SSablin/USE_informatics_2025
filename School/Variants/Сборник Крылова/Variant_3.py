# 24
from re import *
s = open('files/24/24var03.txt').readline()
num = r'(0|[1-9]\d*)'
reg = fr'({num}([-*]{num})+)'
m = max((x.group(0) for x in finditer(reg, s)), key=len)
print(len(m), m)  # 356

# 26
f = open('files/26/26var03.txt')
n, m, k = map(int, f.readline().split())
# m - r rows, k - p places
# f = ('2 1', '2 4', '4 2', '5 3', '6 1', '4 5', '5 6')
# n, m, k = 7, 6, 6
data = [[] for i in range(k + 1)]
for s in f:
    r, p = map(int, s.split())
    data[p].append(r)
ans = []
for i in range(1, k + 1):
    data[i] = sorted([0] + [m + 1] + data[i])
    # [0, 1783, 2751, 5914, 7325, 8006, 10001]
    for j in range(len(data[i]) - 1):
        up, down = data[i][j], data[i][j + 1]
        ans.append([down - up - 2, down - 1, i])
        # [1783 - 0 - 2, 1783 - 1, i]
        # -2 = -1(не включая up) -1(сами сядем => одно из свободных мест исчезнет)
ans.sort(reverse=True)
print(ans[:5])

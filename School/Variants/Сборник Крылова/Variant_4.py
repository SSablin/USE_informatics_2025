# 26
f = open('files/26/26var04.txt')
n, m, k = map(int, f.readline().split())
# m = y, k = x
f = ('2 1', '2 4', '4 2', '5 3', '6 1', '4 5', '5 6')
n, m, k = 7, 6, 6

# 1. как можно больше клеток над
# 2. min y

data = [[] for _ in range(k + 1)]
for line in f:
    y, x = map(int, line.split())
    data[x].append(y)
# print([(data.index(x), x) for x in data])
ans = []
for i in range(1, k + 1):
    data[i].sort()
    data[i] = sorted([0] + [m + 1] + data[i])
    # [0, 1783, 2751, 5914, 7325, 8006, 10001]
    for j in range(len(data[i]) - 1):
        up, down = data[i][j], data[i][j + 1]
        ans.append([down - up - 2, -(down - 1), -i])
ans.sort(reverse=True)
print(ans[:50])
# без учета границ
# 5000 4995
# с учетом границ
# 10000 4999


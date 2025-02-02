# 8
"""from itertools import product

for k in range(1, 20):
    cnt = 0
    for x in product('01', repeat=20):
        if x.count('0') == k:
            cnt += 1
    print(k, cnt)  # 125970"""

# 13
"""from ipaddress import *

ip = ip_address('222.121.128.0')

net = ip_network(f'{ip}/255.255.224.0', 0)

c = 0

for ip in net:
    b = f'{ip:b}'
    # if b[-2:] == '00' or b[-2:] == '11':
    if b[-1] == b[-2]:
        c += 1
print(c)  # 4096"""

# 14
"""from string import *

max_x = -float('inf')
for x in (digits + ascii_uppercase)[:25]:
    n = int(f'A4{x}7F2', 25) + int(f'N{x}G5{x}H', 25) + int(f'74{x}M26', 25)
    if n % 24 == 0:
        print(n // 24)"""

# 15
"""print('c j a f')
for c in range(2):
    for j in range(2):
        for a in range(2):
            f = (not (c or j)) <= (not a)
            if not f:
                print(c, j, a, f)"""

# 17
"""s = [int(x) for x in open('files/17_вариант#6.txt')]
m = min(s)
ans = []
for i in range(len(s) - 2):
    if sum(x >= 0 for x in s[i : i + 3]) >= 2 and abs(sum(s[i:i + 3])) % 10 == abs(m) % 10:
        ans.append(abs(sum(s[i:i + 3])))
print(len(ans), max(ans))  # 209 190954
"""

# 23
"""def f(x, end, p1, p2):
    if x >= end:
        return x == end and 0 < p1 + p2 < 2
    if x > end:
        return False
    if x == 30: p1 += 1
    if x == 60: p2 += 1
    if x < end:
        return f(x + 1, end, p1, p2) + f(x * 2, end, p1, p2) + f(x * 3, end, p1, p2)

print(f(10, 70, 0, 0))"""

"""def f(x, y, c):
    if x == y: return 1
    if x > y or x == c: return 0
    if x < y: return f(x + 1, y, c) + f(x * 2, y, c) + f(x * 3, y, c)
print(f(10, 30, 0) * f())
"""

# 24
# Разобраться!!!
# метод двух указателей
"""s = open('files/24_вариант#6.txt').readline().rstrip()
while '--' in s: s = s.replace('--', '- -')
m = 0
for s1 in s.split():
    if s1.strip('-'):
        nums = list(map(int, s1.strip('-').split('-')))
        l = total_sum = total_len = 0
        for r in range(len(nums)):
            total_sum += nums[r]
            total_len += len(str(nums[r]))
            while total_sum - nums[l] * 2 >= 20_000 and l < r:
                total_sum -= nums[l]
                total_len -= len(str(nums[l]))
                l += 1
            m = max(m, total_len + r - l + (total_sum < 20_000))
print(m)  # 1095"""

# 25
"""from fnmatch import fnmatch
for i in range(2025, 10**10, 2025):
    if fnmatch(str(i), '33?2*42?') and fnmatch(str(i), '*32??2?'):
        print(i, i // 2025)"""

# 26
# https://youtu.be/GYogg6TOxts?si=7eP6AqZvgah2ATYu&t=4059
f = open('files/26_18492.txt')
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
print(len(intervals), max(intervals)[1])

# 27 18585
# A
"""clastersA = [[], [], []]  # 2 361
for s in open('files/27_A_18585.txt'):
    x, y = [float(kl) for kl in s.split()]
    if x < 4 and y < 4:
        clastersA[0].append([x, y])
    if y > 6:
        clastersA[1].append([x, y])
    if x > 6 and y < 4:
        clastersA[2].append([x, y])

clastersA = [kl for kl in clastersA if len(kl) >= 361]
print([len(kl) for kl in clastersA])

def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def center(kl):
    m = []
    for p in kl:
        sm = sum(dist(p, p1) for p1 in kl)
        m.append([sm, p])
    return min(m)[1]

centerA = [center(kl) for kl in clastersA]
print(centerA)

pxA = sum(x for x, y in centerA) / len(clastersA) * 100_000
pyA = sum(y for x, y in centerA) / len(clastersA) * 100_000
print(int(pxA), int(pyA))  # 728724 506096"""
# B
# решить

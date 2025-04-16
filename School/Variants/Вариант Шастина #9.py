# 2
"""for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not((not x) or y) or (y == z) or (not w))
                if not f:
                    print(x, y, z, w, f)"""
# 0 0 1 1 False
# 0 1 0 1 False
# 1 1 0 1 False
# wzyx

# 5
"""r_mx = 0
for i in range(500):
    n = oct(i)[2:]
    if int(n) % 2 == 0:
        for num in '1357':
            n = n.replace(num, '2')
    else:
        n = n.replace(n[0], '3').replace(n[-1], '3')
    r = int(n, 8)
    if r < 300:
        r_mx = max(r_mx, r)
print(r_mx)  # 294"""
# 6
"""from turtle import *
screensize(5000, 5000)
# tracer(0)
lt(90)
c = 20
for i in range(777):
    fd(25 * c)
    lt(90)
    fd(34 * c)
    lt(90)

up()

fd(12 * c)
lt(90)
fd(17 * c)
rt(90)

down()

for i in range(1996):
    fd(25 * c)
    lt(90)
    fd(17 * c)
    lt(90)

up()

for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'red')

exitonclick()
update()"""

# 8
"""from itertools import product

c = 0
for x in product(sorted('СИНЕРГЯ'), repeat=6):
    c += 1
    s = ''.join(x)
    if s.count('ГИРЯ') > 0:
        print(c, s)  # 115381"""

# 7
"""from math import log2
print(log2(65536))  # 16
s = 1920 * 1080 * 16
print(s)
print(512 - 52)  # 460
for i in range(52, 460):
    if 460 % i == 0:
        print(i)  # 92
print((92 * s) / 8 / 1024 / 1024)  # 364"""

# 13 №20220
"""from ipaddress import *
ip = ip_address('111.233.75.16')
for mask in range(33):
    net = ip_network(f'{ip}/{mask}', 0)
    if str(net.network_address) == '111.233.75.0':
        print(net.num_addresses)  # 256"""

# 14 №19898
"""def r7(x, i):
    s = ''
    while x > 0:
        s = str(x % i) + s
        x //= i
    return s


mx0 = []
for x in range(1, 10_000):
    s = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    s7 = r7(s, 7)
    mx0.append(s7.count('0'))
print(max(mx0))  # 203
for x in range(1, 10_000):
    s = 7 ** 270 + 7 ** 170 + 7 ** 70 - x
    s7 = r7(s, 7)
    if s7.count('0') == 203:
        print(x)  # 9604"""

# 15 №19899
"""def mod(m, n):
    return m % n


for a in range(1, 300):
    f = True
    for x in range(1, 300):
        if not ((a + 2 * x) > (400 - a) and ((mod(a, 100) + mod(120, a)) > 140)):
            f = False
    if f:
        print(a)  # 221
        break"""

# 16 №20071
"""def f(n):
    if n > 2000:
        return 16
    if n <= 2000:
        return 2 * f(n + 3)


sp = [int(x) for x in str(int(f(50) / f(110)))]
ans = 1
for x in sp:
    if x != 0:
        ans *= x
print(ans)  # 6720"""

# 17 №19900
"""
s = [int(x) for x in open('files/17_19900.txt')]

znach4 = []
for x in s:
    if len(str(abs(x))) == 4:
        znach4.append(x)
znach4 = sum(znach4)


def znach3(sp):
    c = 0
    for x in sp:
        if len(str(abs(x))) == 3:
            c += 1
    if c == 2:
        return True
    return False


ans = []
for i in range(len(s) - 2):
    if znach3(s[i:i + 3]):
        if (s[i] * s[i + 1] * s[i + 2]) > znach4:
            ans.append(s[i] * s[i + 1] * s[i + 2])
print(len(ans), abs(min(ans)))  # 566 1462000"""

# 24
# №19884
# re - не верно
"""from re import findall
s = open('files/24_19884.txt').readline()
expr = findall(f'(?:0|[6-9][0, 6-9]*)(?:[*-](?:0|[6-9][0, 6-9]*))+', s)
print(expr)
print(len(expr))  # 584675"""

"""s = open('files/24_19884.txt').readline().strip()
s = s.replace('-', '*').replace('6', '7').replace('8', '7').replace('9', '7').replace('**', '* *').replace('**', '* *')

while '*00' in s:
    s = s.replace('*00', '*0 *0')
s = s.replace('*07', '*0 7')
count = 0
for x in s.split():
    sub = x.strip('*')
    cnt = sub.count('7') + sub.count('0')
    for t in sub.split('*'):
        cnt -= len(t)
        for i in range(len(t)):
            if t[i] == '7' or i == len(t) - 1:
                count += cnt
print(count)  # 30460483"""

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

# 27 №20168
"""from math import dist


def get_centroid(c):
    r = []
    for p in c:
        r += [(sum(dist(p, p1) for p1 in c), p)]
    return min(r)[1]


a = [tuple(map(float, x.split())) for x in open('files/27_B_20168.txt')]
c = []
while a:
    c += [[a.pop()]]
    for p1 in c[-1]:
        for p2 in a[:]:
            if dist(p1, p2) < 1:
                c[-1] += [p2]
                a.remove(p2)
print(len(c))
cs = [kl for kl in c if len(kl) >= 20]
cl = min(cs, key=len)
print(get_centroid(cl))
# A: 352342 343732
# B: 6446 857780"""

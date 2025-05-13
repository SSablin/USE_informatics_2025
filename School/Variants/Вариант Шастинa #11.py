# 9
"""for s in open('files/9_шастин10.txt'):
    a = list(map(int, s.split()))
    chet = []
    nchet = []
    for x in a:
        if x % 2 == 0:
            chet.append(x)
        else:
            nchet.append(x)
    if len(set(a)) == len(a) and sum(chet)**2 > sum(nchet)**3:
        print(a, sum(a))  # 246"""

# 13
"""from ipaddress import *
net = ip_network('98.71.254.171/255.248.0.0', 0)
for ip in net.hosts():
    b = f'{ip:b}'
    if b.count('1') % 5 == 0:
        print(ip)"""
# 9871255248

# 23
"""def f(x, end):
    if x < end or x == 20:
        return False
    if x == end:
        return True
    if x > end:
        return f(x - 2, end) + f(x - 3, end) + f(int(x ** 0.5), end)


print(f(26, 3))  # 276"""

# 24
"""from string import digits, ascii_uppercase
alf = (digits + ascii_uppercase)[:16]
nalf = (digits + ascii_uppercase)[16:]
s = open('files/24_шастин10.txt').readline()
for a in nalf:
    while a in s:
        s = s.replace(a, ' ')
ans = ''
for c in s.split():
    if len(c) > len(ans):
        cn, l = 0, 0
        for r in range(len(c)):
            if c[r] == 'B':
                cn += 1
            while cn > 10:
                if c[l] == 'B':
                    cn -= 1
                l += 1
            if cn == 10 and s[l] != '0':
                ans = max(ans, s[l:r + 1], key=len)
print(len(ans))
print(ans)  # 357"""

# 25
"""
def simple(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def F(x):
    s = set()
    for i in range(7, x, 10):
        if x % i == 0 and i % 10 == 7 and simple(i):
            s.add(i)

    if len(s) == 0:
        return 0
    return sum(s) // len(s)


print(119, F(119))

c = 0
for x in range(750_000, 0, -1):
    if c < 5:
        if F(x) != 0 and F(x) % 111 == 0:
            print(x, F(x))
            c += 1
    else:
        break
# 749039 7992
# 748679 3552
# 748663 333
# 746360 222
# 745109 2997"""

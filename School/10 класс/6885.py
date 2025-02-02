'''
№6885
min_r = 10 ** 100
c = '0123456789ABCDE'
def v15(n):
    r = ''
    while n > 0:
        r = c[n % 15] + r
        n //= 15
    return r

for i in range(15, 1000):
    r = v15(i)
    if i % 15 == 0:
        r = r + r[0:2]
    else:
        r = r + v15((i % 15) * 13)
    r = int(r, 15)
    if r > 700:
        min_r = min(min_r, r)

print(min_r)
'''
'''
№6861
minimum = 10**30

for j in range(1001, 1500):
    sp = []
    a = j
    while a > 0:
        sp.append(a % 45)
        a = a // 45
    sp.reverse()
    s1 = 0
    for i in range(0, len(sp), 2):
        s1 += sp[i]
    s2 = sum(sp) - s1
    sp = [min(s1, s2)] + sp + [max(s1, s2)]
    print(sp)
    sp.reverse()
    otvet = 0
    for i in range(len(sp)):
        otvet = otvet + sp[i]*45**i
    if otvet < minimum:
        minimum = otvet

print(minimum)
'''








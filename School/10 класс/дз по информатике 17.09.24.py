# №5
#1
'''x = '123456789'
#print(x[1::2])
for i in range(1, 10000):
    n = format(i, 'b')
    nh = int(n[1::2].count('1'))   #nh
    neh = int(n[::2].count('0'))      #neh
    #print(n, nh, neh)
    #ma = max(nh, neh)
    #mi = min(nh, neh)
    #r = ma - mi
    r = nh - neh
    if r == 5 or r == -5:
        print(i)
        break'''
#2
'''
for i in range(1, 10000):
    n = format(i, 'b')
    if int(n) % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'

    r = int(n, 2)
    if r > 441:
        print(i)
        break'''
#3
'''
for i in range(1, 200):
    n = format(i, 'b')
    if int(n) % 2 == 0:
        n = '1' + n + '0'
    else:
        n = '11' + '11'

    r = int(n, 2)
    if r > 52:
        print(r)
        break'''
#4
'''
for i in range(1, 10000):
    n = format(i, 'b')
    nk = n[:-1]
    #print(n, nk)
    if int(n) % 2 != 0:
        nk += '10'
    else:
        nk += '01'

    r = int(nk, 2)
    if r == 3022:
        print(i)
'''
#5
'''
for i in range(1, 1000):
    n = format(i, 'b')
    n += str(int(n.count('1')) % 2)
    n += str(int(n.count('1')) % 2)

    r = int(n, 2)
    if r > 396:
        print(r)
        break
'''
#6
'''
for i in range(0, 255):
    n = format(i, 'b')
    if len(n) < 8:
        n = (8 - len(n)) * '0' + n
    n = n.replace('1', '*', -1)
    n = n.replace('0', '1', -1)
    n = n.replace('*', '0', -1)
    n1 = int(n, 2)
    r = n1 - i
    if r == 131:
        print(i)'''
#7
'''
for i in range(0, 255):
    n = format(i, 'b')
    if len(n) < 8:
        n = (8 - len(n)) * '0' + n
    n = n.replace('1', '*', -1)
    n = n.replace('0', '1', -1)
    n = n.replace('*', '0', -1)
    n1 = int(n, 2)
    r = n1 - i
    if r == 131:
        print(i)
'''
#8
'''
for i in range(2, 200):
    n = format(i, 'b')
    n += n[-2]
    n += n[2]

    r = int(n, 2)
    if r > 150:
        print(i)
        break
'''
#9
'''
for i in range(0, 128):
    n = format(i, 'b')
    if len(n) < 8:
        n = (8 - len(n)) * '0' + n
    n = n.replace('1', '*', -1)
    n = n.replace('0', '1', -1)
    n = n.replace('*', '0', -1)

    r = int(n, 2) + 1
    if r == 153:
        print(i)'''
#10
'''
a = []
for x in range(500, 2000):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))
'''







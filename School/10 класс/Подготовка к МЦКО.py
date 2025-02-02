# №2 = №5 из ЕГЭ
for n in range(200):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '10'
    else:
        r = '1' + r + '00'
    r = int(r, 2)
    if r > 107:
        print(n)
        break

# №10
s = '3' * 6 + '4' * 27
while '3444' in s:
    s = s.replace('3444', '3', 1)
print(s)

# №11
a = '0123456789AB' # символы в 12 системе счисления
for x in a:
    c1 = int('154' + x + '3', 12)
    c2 = int('1' + x + '365', 12)
    if (c1 + c2) % 13 == 0:
        print((c1 + c2) // 13)


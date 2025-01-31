s = open('../../Downloads/Telegram Desktop/24.txt').readline()
s = s.replace('13579', '1')
s = s.replace('02468', '0')
indexcifr = [t for t in range(len(s)) if s[t] in '10']
kmax = 0
print(indexcifr)
for i in range(len(indexcifr)-1):
    if int(s[indexcifr[i]]) % 2 != int(s[indexcifr[i + 1]]) % 2:
        kmax = max(kmax, indexcifr[i + 1] - indexcifr[i] - 1)

print(kmax)
s = open('files/24_8579.txt').readline()
numbers = '0123456789'
chet = '02468'
nchet = '13579'
ai = 0
under = 0
answer = -10**10

for i in range(len(s)):
    ai -= 1
    if s[i] in chet:
        under += 1
        if s[ai] in nchet:
            answer = under
            break
    elif s[i] in nchet:
        under += 1
        if s[ai] in chet:
            answer = under
            break

print(answer)

'''https://uchebnik.mos.ru/exam/challenge/36785219?activityId=https%3A%2F%2Fuchebnik.mos.ru%2Fexam%2Fchallenge%2F36785219&actor=%7B%22objectType%22%3A%22Agent%22%2C%22account%22%3A%7B%22name%22%3A%227bfa6187-2497-4635-aa3c-31dec41bb68f%22%7D%7D&authurl=https%3A%2F%2Fschool.mos.ru&context=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ3dCI6IjEiLCJ3dGkiOjI0Nzg2ODM0NCwicGlkIjoiN2JmYTYxODctMjQ5Ny00NjM1LWFhM2MtMzFkZWM0MWJiNjhmIiwiZHQiOjE3MDUyNDkwMTI4ODcsIm1pIjoiZDcxYjQxODQtM2ZlMS0zNTBmLWFmMTYtYWZjOWExNzcxMDllIn0.XMekHxq5J8CVlYv3uAPjOrq_kpNr4432xb2lZfS-DVo&endpoint=https%3A%2F%2Fuchebnik.mos.ru%2Flrs-dhw%2F&fetch=https%3A%2F%2Fuchebnik.mos.ru%2Flrs-dhw%2F%2Ftoken%2Ffetch%2F09e4df2e1b208bdc27e721f7c4ffa2fe&registration=c40b41a7-f758-4c69-b870-48e8711ce2c0&role=student&utm_campaign=1&utm_medium=lesson&utm_source=familyw'''

'''№1 Сколько единиц содержится в двоичной записи значения выражения: 4^12 + 2^32 - 16?
x = 4**12 + 2**32 - 16
s = ''
while x != 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))'''
'''№2 Значение выражения 125^4 + 25^8 - 30 записали в системе счисления с основанием 5. 
Сколько цифр 4 содержится в этой записи?
x = 125**4 + 25**8 - 30
s = ''
while x != 0:
    s += str(x % 5)
    x //= 5
s = s[::-1]
print(s.count("4"))'''
'''№3 Значение выражения 4^16 + 2^34 — 8 записали в системе счисления с основанием 2. 
Сколько цифр 1 содержится в этой записи?
x = 4**16 + 2**34 - 8
s = ''
while x != 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))'''
'''№4 Значение выражения 5^36 + 5^24 — 25 записали в системе счисления с основанием 5. 
Сколько цифр ”4” содержится в этой записи?
x = 5**36 + 5**24 - 25
s = ''
while x != 0:
    s += str(x % 5)
    x //= 5
print(s)
s = s[::-1]
print(s)
print(s.count('4'))'''
'''№5 Значение выражения 36^8 + 6^20 — 12 записали в системе счисления с основанием 6. 
Сколько цифр ”5” содержится в этой записи?'''
x = 36**8 + 6**20 - 12
s = ''
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]
print(s.count('5'))
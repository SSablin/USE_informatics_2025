#№16
#1
'''
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n > 3:
        return f(n-3) + f(n-1)
print(f(12))'''
#2
'''
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return f(n-1)*n**2 - f(n-2)
print(f(6))'''
#3
'''
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return (f(n-1) - f(n-2))*n - 15
print(f(7))'''
#4
'''
def f(n):
    if n < 3:
        return 5
    if n % 2 == 0 and n > 3:
        return f(n-2) + 2 * n - 1
    if n % 2 != 0 and n > 3:
        return f(n-1) * f(n-2) + 2
print(f(12))'''
#5
'''
def f(n):
    if n <= 0:
        return n*n
    if n > 0 and n % 2 == 0:
        return 5*f(n//2)+2*f(n-1)
    if n > 0 and n % 2 != 0:
        return f(n-5)*f(n-8)
print((f(12)+f(6))//(f(7)-f(3)))'''
#6
'''
def f(n):
    if n <= 5:
        return 0
    if n % 2 != 0 and n > 5:
        return f(n-5) + (n+3)/2
    if n % 2 == 0 and n > 5:
        return 2*f(n-5) + 2
print((f(6)+f(8)+f(10))/f(9)+f(7))'''
#7
'''
def f(n):
    if n > 12:
        return n + 1
    if n <= 12:
        return f(n+1) + 3*n
print(f(5))'''
#8
'''
def f(n):
    if n == 1:
        return 2
    if n > 1:
        return g(n-1) * f(n-1) - n**n
def g(n):
    if n == 1:
        return 2
    if n > 1:
        return 5*f(n-1) - n*g(n-1)
print(g(5))'''
#9
'''
def F(n):
    if n <= 1:
        return n-3
    if n > 1:
        return F(n-3) + n + 1
for n in range(1000):
    if F(n)>700:
        print(n)
        break'''
#10
'''
def f(n):
    if n <= 5:
        return n
    if n > 5:
        return (f(n-1) - f(n-4)) * n - 10
print(f(23))'''
#11
'''
def f(n):
    if n <= 2:
        return 1
    if n > 2:
        return f(n-1) + g(n-2) - 2
def g(n):
    if n <= 3:
        return 2
    if n > 3:
        return g(n-1) - f(n-2) + 2
print(f(31))'''
#12
'''
def f(n):
    if n <= 5:
        return n - 1
    if n > 5:
        return f(n-1) * f(n-1) - g(n-4) - 2
def g(n):
    if n <= 5:
        return n - 4
    if n > 5:
        return g(n-3) * g(n-3) - f(n-3) + 2
print(f(9))'''
#13
'''
def f(n):
    if n <= 3:
        return 1
    if n > 3:
        return g(n-1) * f(n//4) - 12
def g(n):
    if n <= 1:
        return 1
    if n > 1:
        return f(n-3) + g(n//3) + 1
for n in range(10000):
    if f(n) == 14145:
        print(n)
        break'''
#14
'''
def f(n):
    if n <= 2:
        return n
    if n > 2:
        return g(n//2) + f(n-2)
def g(n):
    if n <= 2:
        return n - 1
    if n > 2:
        return f(n-2) - g(n//5) + 11
for n in range (10000):
    if g(n) == 7693:
        print(n)
        break'''
#15
'''
def f(n):
    if n <= 2:
        return n**2
    if n > 2:
        return g(n-2) - f(n-2) + 8
def g(n):
    if n <= 2:
        return n - 1
    if n > 2:
        return f(n-1) + g(n-1)
for n in range(10000):
    if f(n) == 6607:
        print(n)
        break'''
#№23
#16
'''Исполнитель Щелчок преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:

1. Прибавить 2.

2. Прибавить 5.

3. Умножить на 2.

Первая команда увеличивает число на 2, вторая – на 5, третья – умножает на 2. 
Сколько различных результатов можно получить из исходного числа 8 после выполнения программы, 
содержащей 13 команд, если известно, что запрещено повторять команду, сделанную на предыдущем шаге.'''
'''
a = [[8, '0']]
for i in range(13):
    n = len(a)
    for j in range(n):
        l = a.pop(0)
        last_command = l[1]
        if last_command == '0':
            a.append([l[0] + 2, '1'])
            a.append([l[0] + 5, '2'])
            a.append([l[0] * 2, '3'])
        elif last_command == '1':
            a.append([l[0] + 5, '2'])
            a.append([l[0] * 2, '3'])
        elif last_command == '2':
            a.append([l[0] + 2, '1'])
            a.append([l[0] * 2, '3'])
        else:
            a.append([l[0] + 2, '1'])
            a.append([l[0] + 5, '2'])
arr = set()
for i in range(len(a)):
    arr.add(a[i][0])
print(len(arr))'''

#17
'''Исполнитель Апрель преобразует число, записанное на доске. У исполнителя есть три команды:

1. Прибавить 2

2. Умножить на 3

3. Умножить на 4

Программа для исполнителя Апрель – это последовательность команд. 
Сколько различных результатов можно получить из исходного числа 6
 в ходе исполнения программы, содержащей ровно 12 команд?'''

a = [6]
for i in range(12):
    a = list(set(a))
    n = len(a)
    for j in range(n):
        l = a.pop(0)
        a.append(l + 2)
        a.append(l * 3)
        a.append(l * 4)

a = set(a)
print(len(a))


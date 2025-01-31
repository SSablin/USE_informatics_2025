#19
'''def F(x, y, p):
    if (x + y) >= 77 and p == 3: return True
    if (x + y) < 77 and p == 3: return False

    return F(x+1, y, p+1) or F(x*2, y, p+1) or F(x, y+1, p+1) or F(x, y*2, p+1)

for s in range(1, 70):
    if F(s, 7, 1):
        print(s)
        break'''
#20
'''def F(x, y, p):
    if (x + y) >= 77 and p == 4: return True
    if (x + y) < 77 and p == 4: return False
    if (x + y) >= 77: return False

    if p % 2 == 0:
        return F(x+1, y, p+1) and F(x*2, y, p+1) and F(x, y+1, p+1) and F(x, y*2, p+1)
    else:
        return F(x+1, y, p+1) or F(x*2, y, p+1) or F(x, y+1, p+1) or F(x, y*2, p+1)

for s in range(1, 70):
    if F(s, 7, 1):
        print(s)'''
#21
'''def F(x, y, p):
    if (x + y) >= 77 and (p == 3 or p == 5): return True
    if (x + y) < 77 and p == 5: return False
    if (x + y) >= 77: return False

    if p % 2 == 1:
        return F(x+1, y, p+1) and F(x*2, y, p+1) and F(x, y+1, p+1) and F(x, y*2, p+1)
    else:
        return F(x+1, y, p+1) or F(x*2, y, p+1) or F(x, y+1, p+1) or F(x, y*2, p+1)

for s in range(1, 70):
    if F(s, 7, 1):
        print(s)'''

#19
'''def F(x, p):
    if x >= 29 and p == 3: return True # выигрыш Вани за 1й ход
    if x < 29 and p == 3: return False # НЕ выигрыш Вани за 1й ход
    if x >= 29: return # Выиграл не тот, кто нужен

    if p % 2 == 1:
        return F(x+1, p+1) and F(x*2, p+1)
    else:
        return F(x+1, p+1) or F(x*2, p+1)

for s in range(1, 29):
    if F(s, 1):
        print(s)'''

'''def F(x, p):
    if x >= 29 and (p == 3 or p == 5): return True # выигрыш Вани за 1й или 2й ход
    if x < 29 and p == 5: return False # НЕ выигрыш Вани за 2й ход
    if x >= 29: return # Выиграл не тот, кто нужен

    if p % 2 == 1: # ходы Вани 
        return F(x+1, p+1) and F(x*2, p+1)
    else: # ходы Пети
        return F(x+1, p+1) or F(x*2, p+1)

for s in range(1, 29):
    if F(s, 1):
        print(s)'''

# 19 №27802
'''
def f(x, p):
    if x >= 68 and p == 3:
        return True
    if x < 68 and p == 3:
        return False
    if x >= 68:
        return False

    if p % 2 == 1: # Ходы вани
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 5, p + 1)
    else: # Ходы Пети
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 5, p + 1)


for s in range(1, 68):
    if f(s, 1):
        print(s)
        break'''

# 20 №27803
'''
def f(x, p):
    if x >= 68 and p == 4:
        return True
    if x < 68 and p == 4:
        return False
    if x >= 68:
        return False

    if p % 2 == 0:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 5, p + 1)
    else:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 5, p + 1)


for s in range(1, 68):
    if f(s, 1):
        print(s)'''

#21 №27804
'''
def f(x, p):
    if x >= 68 and (p == 3 or p == 5):
        return True
    if x < 68 and p == 5:
        return False
    if x >= 68:
        return False

    if p % 2 == 1:
        return f(x + 1, p + 1) and f(x + 4, p + 1) and f(x * 5, p + 1)
    else:
        return f(x + 1, p + 1) or f(x + 4, p + 1) or f(x * 5, p + 1)


for s in range(1, 68):
    if f(s, 1):
        print(s)'''

'''
# Исключим стратегию Вани, которая позволит ему гарантированно выиграть первым ходом:
def f(x, h):
    if (h == 3 or h == 5) and x >= 68:
        return 1
    elif h == 5 and x < 68:
        return 0
    elif x >= 68 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)  # стратегия победителя
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)  # стратегия проигравшего


def f1(x, h):
    if h == 3 and x >= 68:
        return 1
    elif h == 3 and x < 68:
        return 0
    elif x >= 68 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, h + 1) or f1(x + 4, h + 1) or f1(x * 5, h + 1)  # стратегия победителя
        else:
            return f1(x + 1, h + 1) and f1(x + 4, h + 1) and f1(x * 5, h + 1)  # стратегия проигравшего(любой ход)


for x in range(1, 68):
    if f(x, 1) == 1:v
        print(x)
print("====")
for x in range(1, 68):
    if f1(x, 1) == 1:
        print(x)  # Исключим эти значения из списка выше
'''

#  19

'''
def f(x, y, h):
    if h == 3 and (x + y) <= 20:
        return True
    if h == 3 and (x + y) > 20:
        return False
    if (x + y) <= 20:
        return False

    if h % 2 == 1:
        return f(x - 1, y, h + 1) or f(x // 2, y, h + 1) or f(x, y - 1, h + 1) or f(x, y // 2, h + 1)
    else:
        return f(x - 1, y, h + 1) or f(x // 2, y, h + 1) or f(x, y - 1, h + 1) or f(x, y // 2, h + 1)


for s in range(11, 1000):
    if f(s, 10, 1):
        print(s)  # 43
'''
#  20

'''
def f(x, y, h):
    if h == 4 and (x + y) <= 20:
        return True
    if h == 4 and (x + y) > 20:
        return False
    if (x + y) <= 20:
        return False

    if h % 2 == 0:
        return f(x - 1, y, h + 1) and f(x // 2, y, h + 1) and f(x, y - 1, h + 1) and f(x, y // 2, h + 1)
    else:
        return f(x - 1, y, h + 1) or f(x // 2, y, h + 1) or f(x, y - 1, h + 1) or f(x, y // 2, h + 1)


for s in range(11, 1000):
    if f(s, 10, 1):
        print(s) #  2324324445
'''
#  21

'''
def f(x, y, h):
    if (h == 3 or h == 5) and (x + y) <= 20:
        return True
    if h == 5 and (x + y) > 20:
        return False
    if (x + y) <= 20:
        return False

    if h % 2 == 1:
        return f(x - 1, y, h + 1) and f(x // 2, y, h + 1) and f(x, y - 1, h + 1) and f(x, y // 2, h + 1)
    else:
        return f(x - 1, y, h + 1) or f(x // 2, y, h + 1) or f(x, y - 1, h + 1) or f(x, y // 2, h + 1)


for s in range(11, 1000):
    if f(s, 10, 1):
        print(s)
'''
#  19
'''
def f(x, y, h):
    if h == 3 and (x + y) >= 91:
        return True
    if h == 3 and (x + y) < 91:
        return False
    if (x + y) >= 91:
        return False

    if h % 2 == 1:
        return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)
    else:
        return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)


for s in range(1, 86):
    if f(s, 5, 1):
        print(s)  # 6
'''
# 20

'''
def f(x, y, h):
    if h == 4 and (x + y) >= 91:
        return True
    if h == 4 and (x + y) < 91:
        return False
    if (x + y) >= 91:
        return False

    if h % 2 == 0:
        return f(x + 1, y, h + 1) and f(x * 4, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 4, h + 1)
    else:
        return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)


for s in range(1, 86):
    if f(s, 5, 1):
        print(s)  # 1021
'''
# 21

'''
def f(x, y, h):
    if (h == 3 or h == 5) and (x + y) >= 91:
        return True
    if h == 5 and (x + y) < 91:
        return False
    if (x + y) >= 91:
        return False

    if h % 2 == 1:
        return f(x + 1, y, h + 1) and f(x * 4, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 4, h + 1)
    else:
        return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)


for s in range(1, 86):
    if f(s, 5, 1):
        print(s)  #20
'''

#  19

'''
def f(x, h):
    if h == 3 and x >= 68:
        return True
    if h == 3 and x < 68:
        return False
    if x >= 68:
        return False

    if h % 2 == 1:
        return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
    else:
        return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)


for s in range(1, 68):
    if f(s, 1):
        print(s)
        break
'''

#  20

'''
def f(x, h):
    if h == 4 and x >= 68:
        return True
    if h == 4 and x < 68:
        return False
    if x >= 68:
        return False

    if h % 2 == 0:
        return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)
    else:
        return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)


for s in range(1, 68):
    if f(s, 1):
        print(s)  # 912
'''

#  21

'''
def f(x, h):
    if (h == 3 or h == 5) and x >= 68:
        return True
    if h == 5 and x < 68:
        return False
    if x >= 68:
        return False

    if h % 2 == 1:
        return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)
    else:
        return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)


for s in range(1, 68):
    if f(s, 1):
        print(s)  # 8
'''

# 19 №27844

'''
def f(x, h):
    if h == 3 and x > 49:
        return True
    if h == 3 and x <= 49:
        return False
    if x > 49:
        return False

    if h % 2 == 1:
        return f(x + 1, h + 1) or f(x + 3, h + 1) or f(x * 2, h + 1)
    else:
        return f(x + 1, h + 1) or f(x + 3, h + 1) or f(x * 2, h + 1)


for s in range(1, 50):
    if f(s, 1):
        print(s)  # 13
'''

# 20 №27845

'''
def f(x, h):
    if h == 4 and x > 49:
        return True
    if h == 4 and x <= 49:
        return False
    if x > 49:
        return False

    if h % 2 == 0:
        return f(x + 1, h + 1) and f(x + 3, h + 1) and f(x * 2, h + 1)
    else:
        return f(x + 1, h + 1) or f(x + 3, h + 1) or f(x * 2, h + 1)


for s in range(1, 50):
    if f(s, 1):
        print(s)  # 122123
'''

# 21 №27846

'''
def f(x, h):
    if (h == 3 or h == 5) and x > 49:
        return True
    if h == 5 and x <= 49:
        return False
    if x > 49:
        return False

    if h % 2 == 1:
        return f(x + 1, h + 1) and f(x + 3, h + 1) and f(x * 2, h + 1)
    else:
        return f(x + 1, h + 1) or f(x + 3, h + 1) or f(x * 2, h + 1)


for s in range(1, 50):
    if f(s, 1):
        print(s)  # 20
'''


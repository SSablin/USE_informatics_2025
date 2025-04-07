"""from math import ceil


def g(s1, s2, h):
    if ((s1 + s2) <= 108) and h == 3:
        return True
    if ((s1 + s2) <= 108) and h != 3:
        return False
    if ((s1 + s2) > 108) and h == 3:
        return False

    if h % 2 == 0:  # Петя
        return g(s1 - 2, s2, h + 1) or g(s1, s2 - 2, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2), h + 1)
    else:  # Ваня
        return g(s1 - 2, s2, h + 1) or g(s1, s2 - 2, h + 1) or g(ceil(s1 / 2), s2, h + 1) or g(s1, ceil(s2 / 2), h + 1)


for s2 in range(49, 1000):
    if g(60, s2, 1):
        print(s2)  # 192"""

# №19750
# Ермаков
"""№ 19750 (Уровень: Средний)
Задание 19.
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. 
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может выполнить любое из следующих действий:
1) убрать из кучи пять камней;
2) если количество камней в куче чётно, уменьшить его в два раза;
3) если количество камней в куче кратно трём, уменьшить его в три раза;
4) если количество камней в куче нечётно и не кратно трём, добавить один камень.
Например, если в куче 12 камней, то за один ход можно получить 7, 6 или 4 камня, а если в куче 11 камней, 
то за один ход можно получить 6 или 12 камней. Игра завершается, когда количество камней в куче становится не более 19. 
Победителем считается игрок, сделавший последний ход, 
то есть первым получивший кучу, в которой будет 19 или меньше камней. 
В начале игры в куче было S камней, S > 19
Укажите минимальное значение S, при котором Петя не может выиграть первым ходом, 
но при любом первом ходе Пети Ваня может выиграть своим первым ходом.
"""
"""def game(s, e, h):
    if s <= e and h == 2: return 1
    if s <= e and h != 2: return 0
    if s > e and h == 2: return 0
    if h % 2 != 0:
        if s % 6 == 0:
            return game(s - 5, e, h + 1) or game(s // 2, e, h + 1) or game(s // 3, e, h + 1)
        if s % 2 == 0:
            return game(s - 5, e, h + 1) or game(s // 2, e, h + 1)
        if s % 3 == 0:
            return game(s - 5, e, h + 1) or game(s // 3, e, h + 1)
        else:
            return game(s - 5, e, h + 1) or game(s + 1, e, h + 1)
    else:
        if s % 6 == 0:
            return game(s - 5, e, h + 1) and game(s // 2, e, h + 1) and game(s // 3, e, h + 1)
        if s % 2 == 0:
            return game(s - 5, e, h + 1) and game(s // 2, e, h + 1)
        if s % 3 == 0:
            return game(s - 5, e, h + 1) and game(s // 3, e, h + 1)
        else:
            return game(s - 5, e, h + 1) and game(s + 1, e, h + 1)


for s in range(20, 1000):
    if game(s, 19, 0) == 1:
        print(s)  # 25
        break"""
"""Задание 20.
Для игры, описанной в задании 19, найдите два наименьших значения S, при которых Петя не может выиграть первым ходом, 
но у Пети есть выигрышная стратегия, позволяющая ему выиграть вторым ходом при любой игре Вани.
В ответе запишите найденные значения в порядке возрастания."""

"""def game(s, e, h, w):
    if s <= e and h == w: return 1
    if s <= e and h != w: return 0
    if s > 19 and h == w: return 0
    if h % 2 == 0:
        if s % 6 == 0:
            return game(s - 5, e, h + 1, w) or game(s // 2, e, h + 1, w) or game(s // 3, e, h + 1, w)
        if s % 2 == 0:
            return game(s - 5, e, h + 1, w) or game(s // 2, e, h + 1, w)
        if s % 3 == 0:
            return game(s - 5, e, h + 1, w) or game(s // 3, e, h + 1, w)
        else:
            return game(s - 5, e, h + 1, w) or game(s + 1, e, h + 1, w)
    else:
        if s % 6 == 0:
            return game(s - 5, e, h + 1, w) and game(s // 2, e, h + 1) and game(s // 3, e, h + 1, w)
        if s % 2 == 0:
            return game(s - 5, e, h + 1, w) and game(s // 2, e, h + 1, w)
        if s % 3 == 0:
            return game(s - 5, e, h + 1, w) and game(s // 3, e, h + 1, w)
        else:
            return game(s - 5, e, h + 1, w) and game(s + 1, e, h + 1, w)


c = 0

for s in range(20, 100):
    if game(s, 19, 0, 3) == 1:
        if game(s, 19, 0, 1) == 0:
            c += 1
            print(s)
    if c == 2:
        break"""
"""Задание 21.
Для игры, описанной в задании 19, найдите минимальное значение S, при котором у Вани есть стратегия, 
позволяющая ему выиграть первым или вторым ходом при любой игре Пети, но у Вани нет стратегии, 
которая позволила бы ему гарантированно выиграть первым ходом."""

# М. Ивакин
"""def f(s, m):
  if s <= 19: return m % 2 == 0
  if m == 0: return 0
  h = []
  if s % 2 == 0:
      h = [f(s - 5, m - 1), f(s // 2, m - 1)]
  if s % 3 == 0:
      h = [f(s - 5, m - 1), f(s // 3, m - 1)]
  if s % 2 != 0 and s % 3 != 0:
      h = [f(s - 5, m - 1), f(s + 1, m - 1)]
  return any(h) if m % 2 != 0 else all(h)

print('19)', [s for s in range(20, 100) if f(s, 2)])
print('20)', [s for s in range(20, 100) if not f(s, 1) and f(s, 3)])
print('21)', [s for s in range(20, 100) if not f(s, 2) and f(s, 4)])"""

# горбачев6
# 19
"""def g(s1, s2, h, p):
    if s1 + s2 >= 132 and h == 2:
        return True
    if s1 + s2 >= 132 and h != 2:
        return False
    if s1 + s2 < 132 and h == 2:
        return False
    if p < 1:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p) or
                    g(s1 * 3, s2, h + 1, 1) or g(s1, s2 * 3, h + 1, 1))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p) and
                    g(s1 * 3, s2, h + 1, 1) and g(s1, s2 * 3, h + 1, 1))
    else:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p))


for s in range(1, 101):
    if g(31, s, 0, 0):
        print(s)  # 33"""

# 20
"""def g(s1, s2, h, p):
    if s1 + s2 >= 132 and h == 3:
        return True
    if s1 + s2 >= 132 and h != 3:
        return False
    if s1 + s2 < 132 and h == 3:
        return False
    if p < 1:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p) and
                    g(s1 * 3, s2, h + 1, 1) and g(s1, s2 * 3, h + 1, 1))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p) or
                    g(s1 * 3, s2, h + 1, 1) or g(s1, s2 * 3, h + 1, 1))
    else:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p))


for s in range(100, 0, -1):
    if g(31, s, 0, 0):
        print(s)  # 32 31"""

# 21
"""def g(s1, s2, h, p):
    if s1 + s2 >= 132 and (h == 2 or h == 4):
        return True
    if s1 + s2 >= 132 and (h != 2 and h != 4):
        return False
    if s1 + s2 < 132 and h == 4:
        return False
    if p < 1:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p) or
                    g(s1 * 3, s2, h + 1, 1) or g(s1, s2 * 3, h + 1, 1))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p) and
                    g(s1 * 3, s2, h + 1, 1) and g(s1, s2 * 3, h + 1, 1))
    else:
        if h % 2 != 0:  # Полина
            return (g(s1 + 2, s2, h + 1, p) or g(s1, s2 + 2, h + 1, p) or
                    g(s1 * 2, s2, h + 1, p) or g(s1, s2 * 2, h + 1, p))
        else:  # Вика
            return (g(s1 + 2, s2, h + 1, p) and g(s1, s2 + 2, h + 1, p) and
                    g(s1 * 2, s2, h + 1, p) and g(s1, s2 * 2, h + 1, p))


for s in range(1, 101):
    if g(31, s, 0, 0):
        print(s)  # 29"""
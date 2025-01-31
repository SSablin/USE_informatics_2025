'''
from turtle import *
tracer(0)
screensize(1000, 1000)

c = 30
left(90)
for i in range(20):
    forward(10*c)
    right(120)

update()
exitonclick()
'''

'''
from turtle import *
tracer(0)

left(90)
for i in range(16):
    left(36)
    forward(4*50)
    left(36)

penup()
for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*50, y*50)
        dot(4, 'red')

update()
exitonclick()'''

'''
from turtle import *
tracer(0)

c = 30

left(90)
for i in range(2):
    fd(10*c)
    rt(90)
    fd(18*c)
    rt(90)

penup()

fd(5*c)
rt(90)
fd(7*c)
rt(90)

pendown()

for i in range(2):
    fd(10*c)
    rt(90)
    fd(7*c)
    rt(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()'''
'''
from turtle import *
tracer(0)


c = 20

left(90)

for i in range(9):
    fd(22*c)
    rt(90)
    fd(6*c)
    rt(90)

penup()

fd(1*c)
rt(90)
fd(5*c)
lt(90)

pendown()

for i in range(9):
    fd(53*c)
    rt(90)
    fd(75*c)
    rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()'''

'''from turtle import *
tracer(0)
c = 30

lt(90)
for i in range(2):
    fd(13*c)
    rt(90)
    fd(18*c)
    rt(90)

penup()

fd(5*c)
rt(90)
fd(9*c)
lt(90)

pendown()

for i in range(2):
    fd(11*c)
    rt(90)
    fd(7*c)
    rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()'''
'''
from turtle import *
tracer(0)


c = 20

left(90)

for i in range(9):
    fd(22*c)
    rt(90)
    fd(6*c)
    rt(90)

penup()

fd(1*c)
rt(90)
fd(5*c)
lt(90)

pendown()

for i in range(9):
    fd(53*c)
    rt(90)
    fd(75*c)
    rt(90)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()
'''

'''
from turtle import *
tracer(0)
c = 30

lt(90)
for i in range(7):
    fd(10*c)
    rt(120)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()'''
'''
from turtle import *
tracer(0)

c = 30

lt(0)
for i in range(4):
    fd(6*c)
    rt(150)
    fd(6*c)
    rt(30)

penup()

for x in range(-c, c):
    for y in range(-c, c):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()'''

'''
from turtle import *
tracer(0)

screensize(10000, 10000)

c = 100

lt(0)
for i in range(4):
    fd(12*c)
    rt(150)
    fd(12*c)
    rt(30)

penup()

for x in range(-c, c):
    for y in range(-c, c):
        setpos(x*c, y*c)
        dot(4, 'red')

update()
exitonclick()'''
'''
from turtle import *
tracer(0)

screensize(10000, 10000)

c = 100

for i in range(10):
    fd(5*c)
    rt(60)

penup()

for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*c, y*c)
        dot(4, 'green')

update()
exitonclick()'''

'''
from turtle import *
tracer(0)

screensize(10000, 10000)

c = 70

lt(90)

for i in range(4):
    fd(7*c)
    rt(90)
    fd(7*c)
    rt(90)

penup()

for x in range(-10, 10):
    for y in range(-10, 10):
        setpos(x*c, y*c)
        dot(4, 'green')

update()
exitonclick()'''


'''
from turtle import *
tracer(0)

lt(90)
screensize(50000, 50000)
c = 30

penup()

fd(100*c)
rt(90)
fd(100*c)
rt(30)

pendown()

for i in range(10):
    fd(25*c)
    rt(90)

penup()

for x in range(-10, 130):
    for y in range(-10, 130):
        setpos(x * c, y * c)
        dot(4, 'green')

update()
exitonclick()'''

'''
k = 0
for x in range(1, 200):
    for y in range(1, 200):
        if (y < (3**0.5) * x + 100 * (1 - 3**0.5)) and \
        (y > (3**0.5) * x + 100 * (1 - 3**0.5) - 50) and \
        (y < (-3**0.5/3) * x + 100 * (1 + 3**0.5/3)) and \
        (y > (-3**0.5/3) * x + 100 * (1 + 3**0.5/3) - 50/3**0.5):
            k += 1
print(k)
'''
'''
c = 0
for x in range(1, 100):
    for y in range(1, 100):
        if (y < (-3**0.5/3) * x + 10) and \
        (y > (3**0.5/3) * x):
            c += 1
print(c)'''

'''
c = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if (y < (3**0.5/3) * x + 31) and \
        (y < (-3**0.5/3) * x + 62) and \
        (y > (-3**0.5/3) * x) and \
        (y > (3**0.5/3) * x - 31) and \
        (x > 0) and x < 31 * 3**0.5:
            c += 1
print(c)'''
'''
from turtle import *
tracer(0)

c = 30

lt(90)
screensize(10000,10000)

rt(315)
for i in range(7):
    fd(16 * c)
    rt(45)
    fd(8 * c)
    rt(135)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*c, y*c)
        dot(4, 'green')

update()
exitonclick()'''
'''
from turtle import *
tracer(0)
screensize(10000, 10000)
lt(90)
c = 30

for i in range(3):
    fd(7 * c)
    rt(90)

fd(8 * c)

for i in range(3):
    lt(90)
    fd(5 * c)

penup()

for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * c, y * c)
        dot(4, 'green')

update()
exitonclick()'''


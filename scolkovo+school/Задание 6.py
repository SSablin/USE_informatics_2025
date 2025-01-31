"""from turtle import *

tracer(0)
screensize(2000, 2000)

c = 40


for i in range(2):
    fd(24 * c)
    rt(90)
    fd(10 * c)
    rt(90)

fd(3 * c)
lt(90)
fd(13 * c)
rt(90)

for i in range(2):
    fd(9 * c)
    rt(90)
    fd(32 * c)
    rt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x*c, y*c)
        dot(4, 'orange')

exitonclick()
update()
"""
# print(11 * 13)


"""from turtle import *

tracer(0)
screensize(5000, 5000)


lt(90)
c = 10
rt(45)
for i in range(10):
    rt(45)
    fd(203 * c)
    rt(45)
fd(-40 * c)
rt(45)
down()
for i in range(5):
    fd(20 * c)
    lt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        setpos(x*c, y*c)
        dot(3, 'red')

exitonclick()
update()"""

"""from turtle import *

tracer(0)
screensize(2500, 2500)
up()

k = 20
lt(90)

for x in range(-5, 85):
    for y in range(-5, 60):
        goto(x * k, y * k)
        dot(3, 'red') if x * y % 5 == 0 else dot(2, 'green')

goto(0, 0)
down()
for _ in range(8):
    fd(16 * k)
    rt(90)
    fd(22 * k)
    rt(90)
up()
fd(5 * k)
rt(90)
fd(5 * k)
lt(90)
down()
for _ in range(8):
    fd(52 * k)
    rt(90)
    fd(77 * k)
    rt(90)

update()
exitonclick()


print(17 * 11)  # 187"""



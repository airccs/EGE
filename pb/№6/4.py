from turtle import *
k = 100
tracer(0)
left(90)
pendown()
screensize(5000, 5000)
right(45)
forward(5*k)
for x in range(7):
    right(45)
    forward(10 * k)
    right(135)
    forward(5 * k)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()

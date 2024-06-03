from turtle import *
k = 20
tracer(0)
left(90)
pendown()
screensize(5000, 5000)
for x in range(7):
    forward(11 * k)
    right(90)
penup()
forward(5 * k)
right(270)
forward(3 * k)
right(90)
pendown()
for x in range(11):
    forward(11 * k)
    right(90)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()
done()

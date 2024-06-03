from turtle import *

k = 100
tracer(0)
left(90)
pendown()
screensize(5000, 5000)
for x in range(4):
    forward(4 * k)
    right(90)
forward(7 * k)
for x in range(4):
    left(90)
    forward(6 * k)
penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()

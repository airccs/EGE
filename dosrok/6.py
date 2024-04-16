from turtle import *
left(90)
tracer(0)
screensize(2000,2000)
k = 20
pendown()
for i in range(2):
    forward(13*k)
    right(90)
    forward(18 * k)
    right(90)
penup()
forward(5*k)
right(90)
forward(9 * k)
left(90)
pendown()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7 * k)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        setpos(x*k,y*k)
        dot()
done()
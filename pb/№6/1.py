from turtle import *
k = 30
tracer(0)
left(90)
pendown()
for i in range(4):
    forward(11*k)
    right(90)
penup()
for x in range(-100,100):
    for y in range(-100, 100):
        setpos(x*k,y*k)
        dot()
done()
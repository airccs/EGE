from turtle import *
k = 100
screensize(5000,5000)
left(90)
tracer(0)
pendown()
for i in range(123):
    forward(7*k)
    right(240)
penup()
for x in range(-100,100):
    for y in range(-100, 100):
        setpos(x*k,y*k)
        dot()
done()

from turtle import *
k=40
tracer(0)
for i in range(24):
    forward(3*k)
    left(60)
penup()
for x in range(-10,10):
    for y in range(-10, 10):
        setpos(x*k,y*k)
        dot(3)
done()

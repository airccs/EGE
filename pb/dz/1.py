from turtle import *
k = 50
tracer(0)
left(90)
screensize(5000,5000)
pendown()

for i in range(4):
    forward(10 * k)
    right(270)
penup()
forward(3 * k)
right(270)
forward(5 * k)
right(90)
pendown()
for i in range(2):
    forward(10 * k)
    right(270)
    forward(12 * k)
    right(270)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        setpos(x*k,y*k)
        dot()
done()
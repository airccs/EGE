from turtle import *
k=30
tracer(0)
screensize(5000,5000)
pendown()
for i in range(9):
    circle(5*k,-180)
    left(180)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-20, 20):
        setpos(x*k,y*k)
        dot()
print(39*4+81)
done()
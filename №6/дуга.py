from turtle import *
k = 20
tracer(0)
pendown()
for i in range(4):
    circle(5*k,-180)
    left(90)
penup()
for x in range(-20,20):
    for y in range(-100, 100):
        setpos(x*k,y*k)
        dot()
done()


from turtle import *
k = 20
tracer(0)
pendown()
for i in range(4):
    circle(4*k,180)
    right(90)
penup()
for x in range(-20,20):
    for y in range(-100, 100):
        setpos(x*k,y*k)
        dot()
done()

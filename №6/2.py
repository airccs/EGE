from turtle import *
k=40
tracer(0)
begin_fill()
for i in range(6):
    forward(3*k)
    left(60)
end_fill()
canvas=getcanvas()
data=[]
for x in range(-10,10):
    for y in range(-10, 10):
        if canvas.find_overlapping(x*k,y*k,x*k,y*k):
            print(x,y,canvas.find_overlapping(x*k,y*k,x*k,y*k))
            data.append(canvas.find_overlapping(x*k,y*k,x*k,y*k))
print(data)
done()
from turtle import *

speed(0)
pendown()
k = 10
left(90)
begin_fill()
for i in range(2):
    right(90)
    forward(120 * k)
    right(90)
    forward(14 * k)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) != ():
            cnt += 1
print(cnt)
done()

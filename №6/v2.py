from turtle import *

tracer(0)
pendown()
right(90)
cnt = 0
k = 50
begin_fill()
for i in range(21):
    forward(137 * k)
    right(120)
end_fill()
canvas = getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1
print(cnt)
done()

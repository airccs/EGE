from turtle import *

pendown()
k = 30
begin_fill()
for i in range(6):
    forward(3 * k)
    left(60)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-10, 10):
    for y in range(-10, 10):
        if (5 in canvas.find_overlapping(x * k, y * k, x * k, y * k)
                and 4 not in canvas.find_overlapping(x * k, y * k, x * k, y * k)):
            cnt += 1
print(cnt)
done()

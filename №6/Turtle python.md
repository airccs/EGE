# **Turtle python**

```python
tracer(0) # ускорение вывода рисунка
pendown() # опустить хвост
	begin_fill() # применение заливки
end_fill() # соответственно окончание заливки
canvas = getcanvas() # создание пересечений
canvas.find_overlapping() # поиск пересечений
circle(5*k,180) #дуга (радиус,угол)
```

**Пример кода на счёт точек внутри фигуры:**

```python
from turtle import *

tracer(0)
pendown()
right(90)
cnt = 0
k = 100
begin_fill()
for i in range(123):
    forward(111 * k)
    right(120)
end_fill()
canvas = getcanvas()
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1
print(cnt)
done()
```

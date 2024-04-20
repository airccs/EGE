def f(x,y):
    return (x + 2 * y > a) or (y < x) or (x < 30)


for a in range(50, 300):
    if all(f(x,y) == 1 for x in range(1, 3000) for y in range(1, 3000)):
        print(a)

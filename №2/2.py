print("x y w z F")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (x and not y)or (x==z) or not w
                if F == 0:
                    print(x, y, w, z, int(F))

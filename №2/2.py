print("x y w z F")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                F = (w or x or y)<=((y or z)and x or y and(w or z))
                if F == 0:
                    print(x, y, w, z, int(F))

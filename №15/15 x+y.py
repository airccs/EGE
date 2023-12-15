for a in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x>=17)or(3*x<y))or(y*x<a)) == False:
                break
        if (((x>=17)or(3*x<y))or(y*x<a)) == False:
            break
    else:
        print(a)

for a in range(1, 1000):
    for x in range(1, 1000):
        if (((x & 14 != 0) and (x & 61 != 0)) <= ((x & a != 0) and (x & 78 != 0))) == False:
            break
    else:
        print(a)

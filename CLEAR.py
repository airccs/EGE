def Del(n, m):
    return n % m == 0


for a in range(1, 10000):
    for x in range(1, 10000):
        if ((Del(x, a) and Del(x, 16)) <= ((not(Del(x, 16))) or Del(x, 111) or Del(x, 77))) == False:
            break
    else:
        print(a)

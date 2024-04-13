def Del(n, m):
    return n % m == 0


for a in range(1, 10000):
    for x in range(1, 10000):
        if (Del(a, 5) and ((not (Del(2025, a))) <= (Del(x, 1888) <= Del(2023, a)))) == False:
            break
    else:
        print(a)


def Del(n, m):
    return n % m == 0


for a in range(1, 1000):
    s = True
    for x in range(1, 1000):
        if ((Del(x, a) and Del(x, 30)) <= ((not (Del(x, 30))) or Del(x, 40))) == False:
            s = False
            break
    if s:
        print(a)

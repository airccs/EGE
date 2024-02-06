for n in range(1, 1000):
    n2 = bin(n)[2:]
    if sum(map(int, str(n))) % 2 != 0:
        n2 += "1"
    else:
        n2 += "0"
    if sum(map(int, str(int(n2,2)))) % 2 != 0:
        n2 += "1"
    else:
        n2 += "0"
    r = int(n2, 2)
    if r > 1234:
        print(r)
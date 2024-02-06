'''for n in range(1, 1000):
    n2 = bin(n)[2:]
    n2 += n2[-1]
    if bin(n)[2:].count("1") % 2 == 0:
        n2 += "0"
    else:
        n2 += "1"
    if n2.count("1") % 2 == 0:
        n2 += "1"
    else:
        n2 += "0"
    R = int(n2, 2)
    if R > 553:
        print(n)
        break'''

'''for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 2 != 0:
        n2 += "0"
    else:
        n2 = "1" + n2
    if n2.count("1") % 2 == 0:
        n2 += "1"
    else:
        n2 += "0"
    r = int(n2, 2)
    if r > 300:
        print(n)
        break'''


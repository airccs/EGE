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


def to39(x):
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s = ""
    while x > 0:
        s += alph[x % 39]
        x = x // 39
    return s[::-1]


def from_to39(x):
    x = x[::-1]
    alph = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    s = 0
    for i in range(len(x)):
        s += alph.index(x[i]) * (39 ** i)
    return s


for n in range(100000000, 0,-1):
    n39 = to39(n)
    if n % 7 == 0:
        n39 = "F32" + n39 + "32Z"
    else:
        a = (n % 123) * 54
        n39 += to39(a)
    r = from_to39(n39)
    if r <1000000:
        print(n)
        break
def to4(x):
    s = ""
    while x > 0:
        s = str(x % 4) + s
        x = x // 4
    return s


t = []
for n in range(1, 1000):
    n3 = to4(n)
    if n % 4 == 0:
        n3 += n3[-2:]
    else:
        n3 += to4((n % 4) * 2)
    r = int(n3, 4)
    if r < 479:
        t.append(n)
print(max(t))

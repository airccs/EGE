def to5(x):
    s = ""
    while x > 0:
        s += str(x % 5)
        x = x // 5
    return s[::-1]

t=[]
for n in range(1, 10000):
    n5 = to5(n)
    if n % 7 == 0:
        n5 = n5[:4] + n5 + "0" * (4 - len(n5)) + n5[-4:]
    else:
        n5 += bin((n % 7) * 2)[2:]
    r = int(n5, 5)
    if r > 1000 and r % 760 == 0:
        t.append(r)
print(min(t))

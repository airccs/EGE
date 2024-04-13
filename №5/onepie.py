t = []
for n in range(1, 2500):
    n4 = n
    n_4 = ""
    while n4 != 0:
        n_4 += str(n4 % 4)
        n4 //= 4
    n_4 = n_4[::-1]
    if len(n_4) % 2 == 0:
        a = len(n_4) // 2
        r_4 = n_4[:a] + "0" + n_4[a:]
    if len(n_4) % 2 == 1:
        r_4 = n_4
    r = int(r_4)
    if r <= 180:
        t.append(n)
print(max(t))
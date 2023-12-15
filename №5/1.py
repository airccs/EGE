t = []
for n in range(4, 200):
    n_2 = bin(n)[2:]
    ost_2 = bin((n % 3) * 3)[2:]
    if n % 3 == 0:
        r_2 = n_2 + n_2[-3:]
    if n % 3 != 0:
        r_2 = n_2 + ost_2
    r = int(r_2, 2)
    if r > 151:
        t.append(r)
print(min(t))

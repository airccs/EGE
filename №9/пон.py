f = open("9_15321.csv")
k = 0
for j in f:
    t = list(map(int, j.split(";")))
    p = []
    n = []
    b = []
    for i in range(len(t)):
        if t.count(t[i]) == 4:
            p.append(t[i])
        if t.count(t[i]) == 2:
            n.append(t[i])
        if t.count(t[i]) == 2:
            b.append(t[i])
    if len(p) == 3:
        print(t, p, n)

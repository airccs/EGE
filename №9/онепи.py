f = open("9_15321.csv")
k = 0
for j in f:
    t = list(map(int, j.split(";")))
    p = []
    n = []
    for i in range(len(t)):
        if t.count(t[i]) == 3:
            p.append(t[i])
        if t.count(t[i]) == 1:
            n.append(t[i])
    if len(p)==3:
        print(t, p, n)
